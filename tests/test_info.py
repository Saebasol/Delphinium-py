from datetime import datetime

import pytest

from delphinium.client import Delphinium


@pytest.mark.asyncio
async def test_info(client: Delphinium):
    info = await client.info(1)
    assert info.id == 4271
    assert isinstance(info.date, datetime)
