import pytest

from delphinium.client import Delphinium
from delphinium.entities.info import Info


@pytest.mark.asyncio
async def test_list(client: Delphinium):
    infos, count = await client.list(1)
    assert isinstance(infos, list)
    assert all(isinstance(info, Info) for info in infos)
    assert isinstance(count, int)
