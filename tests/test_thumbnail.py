import pytest

from delphinium.client import Delphinium
from delphinium.dtos.thumbnail import Size
from delphinium.entities.file import File


@pytest.mark.asyncio
async def test_thumbnail_single(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.SMALLSMALL)
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_multi(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.SMALLSMALL, single=False)
    assert len(thumbnail) >= 1
    assert all(image.url.startswith("https://") for image in thumbnail)
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_smallsmall_size(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.SMALLSMALL)
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert Size.SMALLSMALL.value in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_small_size(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.SMALL)
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert Size.SMALL.value in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_smallbig_size(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.SMALLBIG)
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert Size.SMALLBIG.value in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)


@pytest.mark.asyncio
async def test_thumbnail_big_size(client: Delphinium):
    thumbnail = await client.get_thumbnail(1, Size.BIG)
    assert thumbnail[0].url.startswith("https://")
    assert len(thumbnail) == 1
    assert Size.BIG.value in thumbnail[0].url
    assert isinstance(thumbnail[0].file, File)
