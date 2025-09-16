import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_thumbnail_single(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    print(thumbnail.url)
    assert thumbnail.url[0].startswith("https://")
    assert len(thumbnail.url) == 1


@pytest.mark.asyncio
async def test_thumbnail_multi(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall", single=False)
    assert len(thumbnail.url) >= 1
    assert all(url.startswith("https://") for url in thumbnail.url)


@pytest.mark.asyncio
async def test_thumbnail_smallsmall_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallsmall")
    assert thumbnail.url[0].startswith("https://")
    assert len(thumbnail.url) == 1
    assert all("smallsmall" in url for url in thumbnail.url)


@pytest.mark.asyncio
async def test_thumbnail_small_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "small")
    assert thumbnail.url[0].startswith("https://")
    assert len(thumbnail.url) == 1
    assert all("small" in url for url in thumbnail.url)


@pytest.mark.asyncio
async def test_thumbnail_smallbig_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "smallbig")
    assert thumbnail.url[0].startswith("https://")
    assert len(thumbnail.url) == 1
    assert all("smallbig" in url for url in thumbnail.url)


@pytest.mark.asyncio
async def test_thumbnail_big_size(client: Delphinium):
    thumbnail = await client.thumbnail(1, "big")
    assert thumbnail.url[0].startswith("https://")
    assert len(thumbnail.url) == 1
    assert all("big" in url for url in thumbnail.url)
