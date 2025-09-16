import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_thumbnail_single(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    assert thumbnail[0].startswith("https://")
    assert len(thumbnail) == 1


@pytest.mark.asyncio
async def test_thumbnail_multi(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall", single=False)
    assert len(thumbnail) >= 1
    assert all(url.startswith("https://") for url in thumbnail)


@pytest.mark.asyncio
async def test_thumbnail_smallsmall_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    assert thumbnail[0].startswith("https://")
    assert len(thumbnail) == 1
    assert "smallsmall" in thumbnail[0]


@pytest.mark.asyncio
async def test_thumbnail_small_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "small")
    assert thumbnail[0].startswith("https://")
    assert len(thumbnail) == 1
    assert "small" in thumbnail[0]


@pytest.mark.asyncio
async def test_thumbnail_smallbig_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallbig")
    assert thumbnail[0].startswith("https://")
    assert len(thumbnail) == 1
    assert "smallbig" in thumbnail[0]


@pytest.mark.asyncio
async def test_thumbnail_big_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "big")
    assert thumbnail[0].startswith("https://")
    assert len(thumbnail) == 1
    assert "big" in thumbnail[0]
