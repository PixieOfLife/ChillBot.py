import aiohttp
from .base_urls import base_api

class Request:
    def __init__(self, headers: dict[str, str], params: dict[str, str]):
        self._headers: dict[str, str] = headers
        self._params = params

        self._client: aiohttp.ClientSession = aiohttp.ClientSession(
            headers=self._headers
        )
    
    async def GET(self, endpoint: str):
        response: aiohttp.ClientSession = await self._client.get(base_api + endpoint, params=self._params)

        await self._client.close()
        return response