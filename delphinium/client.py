from typing import Literal

from delphinium.entities import *
from delphinium.entities.resolved_image import ResolvedImage
from delphinium.entities.tags import Tags
from delphinium.http import DelphiniumHTTP


class Delphinium(DelphiniumHTTP):
    async def galleryinfo(self, index: int) -> Galleryinfo:
        response = await self.get_galleryinfo(index)
        return Galleryinfo.from_dict(response)

    async def image(self, index: int) -> list[ResolvedImage]:
        resp = await self.get_image(index)
        return [ResolvedImage.from_dict(image) for image in resp]

    async def search(self, query: list[str], offset: int = 1) -> tuple[list[Info], int]:
        resp = await self.post_search(query, offset)
        return (
            [Info.from_dict(info) for info in resp["result"]],
            resp["count"],
        )

    async def random(self, query: list[str]) -> Info:
        resp = await self.get_random(query)
        return Info.from_dict(resp)

    async def info(self, index: int) -> Info:
        resp = await self.get_info(index)
        return Info.from_dict(resp)

    async def tags(self) -> Tags:
        resp = await self.get_tags()
        return Tags.from_dict(resp)

    async def thumbnail(
        self,
        id: int,
        size: Literal["smallsmall", "small", "smallbig", "big"],
        single: bool = True,
    ) -> list[ResolvedImage]:
        resp = await self.get_thumbnail(id, size, single)
        return [ResolvedImage.from_dict(image) for image in resp]

    async def list(self, index: int) -> tuple[list[Info], int]:
        resp = await self.get_list(index)
        infos = [Info.from_dict(info) for info in resp["list"]]
        return infos, resp["count"]
