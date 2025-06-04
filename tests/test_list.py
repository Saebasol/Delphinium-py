import pytest

from phlox.client import Phlox
from phlox.entities.info import Info


@pytest.mark.asyncio
async def test_list(client: Phlox):
    infos, total = await client.list(1)
    assert isinstance(infos, list)
    assert all(isinstance(info, Info) for info in infos)
    assert isinstance(total, int)
