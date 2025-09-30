from typing import Any, Optional

from aiohttp import ClientSession

from delphinium.dtos.list import ListResultDTO
from delphinium.dtos.search import SearchResultDTO
from delphinium.dtos.thumbnail import Size
from delphinium.entities import *
from delphinium.entities.resolved_image import ResolvedImage
from delphinium.entities.tags import Tags
from delphinium.http import DelphiniumHTTP


class Delphinium:
    def __init__(
        self, base_url: str, client_session: Optional[ClientSession] = None
    ) -> None:
        self.http = DelphiniumHTTP(base_url, client_session)

    async def get_galleryinfo(self, id: int) -> Galleryinfo:
        data = await self.http.get_galleryinfo(id)
        return Galleryinfo.from_dict(data)

    async def get_image(self, id: int) -> list[ResolvedImage]:
        data = await self.http.get_image(id)
        return [ResolvedImage.from_dict(item) for item in data]

    async def get_info(self, id: int) -> Info:
        data = await self.http.get_info(id)
        return Info.from_dict(data)

    async def get_list(self, index: int) -> ListResultDTO:
        data = await self.http.get_list(index)
        return ListResultDTO.from_dict(data)

    async def get_tags(self) -> Tags:
        data = await self.http.get_tags()
        return Tags.from_dict(data)

    async def get_thumbnail(
        self, id: int, size: Size = Size.SMALL, single: bool = True
    ) -> list[ResolvedImage]:
        data = await self.http.get_thumbnail(id, size, single)
        return [ResolvedImage.from_dict(item) for item in data]

    async def post_random(self, query: list[str]) -> Info:
        data = await self.http.post_random(query)
        return Info.from_dict(data)

    async def post_search(self, query: list[str], offset: int = 0) -> SearchResultDTO:
        data = await self.http.post_search(query, offset)
        return SearchResultDTO.from_dict(data)

    async def close(self) -> None:
        if self.http.client_session:
            await self.http.client_session.close()

    async def __aenter__(self) -> "Delphinium":
        await self.http.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.http.__aexit__(*args)
