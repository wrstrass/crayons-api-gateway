import aiohttp

async def async_get(url: str, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            return await response.json()

async def async_post(url: str, data: str = None, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, **kwargs) as response:
            return await response.json()
