import pytest

from phlox.client import Phlox


@pytest.mark.asyncio
async def test_image(client: Phlox):
    image = await client.image(1)
    assert isinstance(image[0], str)
