import asyncio
import sys
from enum import Enum
from typing import Any

from mymark.adapter import Adapter, Request
from mymark.adapter_server import GPTModel, GPTRole
from aiohttp import ClientSession

class GPTModel(Enum):
    """
    Enum for models of GPT API.
    """

    GPT3_5TURBO = "gpt-3.5-turbo"
    GPT3_5TURBOLATEST = "gpt-3.5-turbo-0125"
    # Not suitable for high traffic
    GPT3_5TURBO_UNLIMITED = "gpt-3.5-turbo"
    GPT4 = "gpt-4"  # Never ever use this
    GPT4LATEST = "gpt-4-turbo-preview"

    # for testing
    MOCKED_MODEL = "mocked_model"

class GPTRequest(Request):  # pylint: disable=too-few-public-methods
    def __init__(
        self,
        query: list[dict[str, Any]],
        model: GPTModel = GPTModel.GPT3_5TURBOLATEST,
        temperature: float = 0.3,
    ) -> None:
        """Initialises with a query, the GPTRole and the GPTModel"""
        super().__init__()
        self._query = query
        self.model = model
        self.temperature = temperature

    @property
    def query(self) -> list[dict[str, Any]]:
        return self._query

    @staticmethod
    def from_json(obj: dict[str, Any]) -> "GPTRequest":
        query = [
            {"role": GPTRole[q["role"].upper()], "content": q["content"]} for q in obj["query"]
        ]
        model = GPTModel[obj["model"].upper()]
        temperature = obj["temperature"]
        return GPTRequest(query=query, model=model, temperature=temperature)


class GPTAdapter(Adapter):
    def __init__(self, gpt_api_key):
        self.gpt_api_key = gpt_api_key

    def get_response(self, request: GPTRequest) -> str:
        """Processes a GPTRequest and returns the response"""
        result: list[str] = asyncio.run(self.__get_responses_async([request]))
        return result[0]

    async def __get_single_response(self, session: ClientSession, request: GPTRequest) -> Any:
        """Returns an async task for request that holds the GPT response"""
        # Post the request
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            json={
                "model": request.model.value,
                "messages": [
                    {
                        "role": (
                            message["role"]
                            if isinstance(message["role"], str)
                            else message["role"].value
                        ),
                        "content": message["content"],
                    }
                    for message in request.query
                ],
                "temperature": request.temperature,
            },
            headers={
                "Authorization": f"Bearer {self.gpt_api_key}",
                "Content-Type": "application/json",
            },
            timeout=30,
        ) as response:
            # Get the result as json
            result = await response.json()
            return result

    def get_responses(self, requests: list[GPTRequest]) -> list[str]:
        """Processes many GPTRequests and the response"""
        return asyncio.run(self.__get_responses_async(requests))

    async def __get_responses_async(self, requests: list[GPTRequest]) -> Any:
        async with ClientSession() as session:

            for retry in range(3):
                # Map each request to an async task
                tasks = [self.__get_single_response(session, request) for request in requests]

                results: list[dict[str, Any]] = await asyncio.gather(*tasks)
                try:
                    # Extract content from each json response dict
                    return [
                        completion["choices"][0]["message"]["content"] for completion in results
                    ]
                except Exception as e:
                    print(
                        "Error! Something went wrong with OpenAI call. Response:\n", file=sys.stderr
                    )
                    print(results, file=sys.stderr)
                    if retry == 0:
                        await asyncio.sleep(1)
                    elif retry == 1:
                        print("Rate limit reached, waiting...", file=sys.stderr)
                        await asyncio.sleep(30)
                    else:
                        raise e
