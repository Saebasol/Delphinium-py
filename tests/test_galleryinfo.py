from datetime import date, datetime

import pytest

from phlox.client import Phlox


@pytest.mark.asyncio
async def test_galleryinfo(client: Phlox):
    galleryinfo = await client.galleryinfo(1)
    assert galleryinfo.tags[0].female
    assert isinstance(galleryinfo.date, datetime)
    assert isinstance(galleryinfo.datepublished, date)
