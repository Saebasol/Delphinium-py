import pytest

from delphinium.client import Delphinium
from delphinium.entities.file import File


@pytest.mark.asyncio
async def test_image(client: Delphinium):
    image = await client.get_image(1)
    assert isinstance(image[0].url, str)
    assert isinstance(image[0].file, File)
