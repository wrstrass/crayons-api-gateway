import json
from typing import Mapping
import aiohttp
from fastapi.responses import JSONResponse


class AsyncResponse:
    def __init__(self, status: int, headers: Mapping, body: dict) -> None:
        self.status = status
        self.headers = headers
        self.body = body

    def to_response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status,
            headers=self.headers,
            content=self.body,
        )

    def __str__(self) -> str:
        return f"{self.__dict__}"


async def async_get(url: str, **kwargs) -> AsyncResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            body = await response.json()
            return AsyncResponse(
                status=response.status,
                headers=response.headers,
                body=body,
            )

async def async_post(url: str, data: dict = None, **kwargs) -> AsyncResponse:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, **kwargs) as response:
            body = await response.json()
            return AsyncResponse(
                status=response.status,
                headers=response.headers,
                body=body,
            )
