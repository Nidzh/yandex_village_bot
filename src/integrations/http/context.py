from httpx import AsyncClient

from src.integrations.http.client import HTTPClient


async def get_http_client() -> HTTPClient:
    async with AsyncClient() as client:
        yield HTTPClient(client=client)
