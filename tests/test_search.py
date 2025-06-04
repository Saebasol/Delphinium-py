import pytest

from phlox.client import Phlox
from phlox.entities.info import Info


@pytest.mark.asyncio
async def test_search(client: Phlox):
    infos, count = await client.search(["sekigahara", "artist:tsukako"])
    assert isinstance(infos, list)
    assert all(isinstance(info, Info) for info in infos)
    assert isinstance(count, int)
