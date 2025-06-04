from datetime import datetime

import pytest

from phlox.client import Phlox


@pytest.mark.asyncio
async def test_info(client: Phlox):
    info = await client.info(1)
    assert info.id == 4271
    assert isinstance(info.date, datetime)
