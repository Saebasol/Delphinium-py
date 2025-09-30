import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_info(client: Delphinium):
    tags = await client.get_tags()
    assert isinstance(tags.artists, list)
    assert isinstance(tags.groups, list)
    assert isinstance(tags.series, list)
    assert isinstance(tags.characters, list)
    assert isinstance(tags.tag, list)
    assert isinstance(tags.male, list)
    assert isinstance(tags.female, list)
    assert isinstance(tags.type, list)
    assert isinstance(tags.language, list)
