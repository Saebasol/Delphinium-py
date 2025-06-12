import pytest

from delphinium.client import Delphinium
from delphinium.entities.info import Info


@pytest.mark.asyncio
async def test_search(client: Delphinium):
    infos, count = await client.search(["sekigahara", "artist:tsukako"])
    assert isinstance(infos, list)
    assert all(isinstance(info, Info) for info in infos)
    assert isinstance(count, int)
