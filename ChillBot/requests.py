import aiohttp

from .base_urls import base_api


class Request:
    def __init__(self, headers: dict[str, str], params: dict[str, str]) -> None:
        self._headers: dict[str, str] = headers
        self._params: dict[str, str] = params

    async def GET(self, endpoint: str) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.get(base_api + endpoint, params=self._params) as response:
                return response
