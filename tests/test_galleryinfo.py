from datetime import date, datetime

import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_galleryinfo(client: Delphinium):
    galleryinfo = await client.get_galleryinfo(1)
    assert galleryinfo.tags[0].female
    assert isinstance(galleryinfo.date, datetime)
    assert isinstance(galleryinfo.datepublished, date)
