import pytest_asyncio

from delphinium.client import Delphinium


@pytest_asyncio.fixture()
async def client():
    async with Delphinium("https://api.saebasol.org") as client:
        yield client
