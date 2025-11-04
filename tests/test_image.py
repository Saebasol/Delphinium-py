import pytest
from yggdrasil.domain.entities.file import File

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_image(client: Delphinium):
    image = await client.get_image(1)
    assert isinstance(image[0].url, str)
    assert isinstance(image[0].file, File)
