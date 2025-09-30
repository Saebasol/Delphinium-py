import pytest

from delphinium.client import Delphinium
from delphinium.dtos.search import SearchResultDTO
from delphinium.entities.info import Info


@pytest.mark.asyncio
async def test_search(client: Delphinium):
    response = await client.post_search(["sekigahara", "artist:tsukako"])
    assert isinstance(response, SearchResultDTO)
    assert isinstance(response.result, list)
    assert all(isinstance(info, Info) for info in response.result)
    assert isinstance(response.count, int)
