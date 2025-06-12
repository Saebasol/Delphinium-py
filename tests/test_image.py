import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_image(client: Delphinium):
    image = await client.image(1)
    assert isinstance(image[0], str)
