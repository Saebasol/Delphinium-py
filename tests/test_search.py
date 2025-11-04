import pytest
from yggdrasil.domain.entities.info import Info

from delphinium.client import Delphinium
from delphinium.dtos.search import SearchResultDTO


@pytest.mark.asyncio
async def test_search(client: Delphinium):
    response = await client.post_search(["sekigahara", "artist:tsukako"])
    assert isinstance(response, SearchResultDTO)
    assert isinstance(response.results, list)
    assert all(isinstance(info, Info) for info in response.results)
    assert isinstance(response.count, int)
