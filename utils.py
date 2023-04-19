import json
import aiohttp
from fastapi import Response


class AsyncResponse:
    def __init__(self, status: int, body: dict) -> None:
        self.status = status
        self.body = body

    def to_response(self) -> Response:
        return Response(
            content=json.dumps(self.body),
            status_code=self.status,
        )


async def async_get(url: str, **kwargs) -> AsyncResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            body = await response.json()
            return AsyncResponse(
                status=response.status,
                body=body,
            )

async def async_post(url: str, data: dict = None, **kwargs) -> AsyncResponse:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, **kwargs) as response:
            body = await response.json()
            return AsyncResponse(
                status=response.status,
                body=body,
            )
