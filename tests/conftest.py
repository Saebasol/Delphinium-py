import pytest_asyncio

from phlox.client import Phlox


@pytest_asyncio.fixture()
async def client():
    async with Phlox("https://api.saebasol.org") as client:
        yield client
