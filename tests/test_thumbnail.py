import pytest

from delphinium.client import Delphinium
from delphinium.entities.file import File


@pytest.mark.asyncio
async def test_thumbnail_single(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_multi(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall", single=False)
    assert len(thumbnail) >= 1
    assert all(image.url.startswith("https://") for image in thumbnail)
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_smallsmall_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert "smallsmall" in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_small_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "small")
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert "small" in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_smallbig_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallbig")
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert "smallbig" in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_big_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "big")
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert "big" in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)
