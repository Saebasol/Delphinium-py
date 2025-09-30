from platform import python_version
from types import TracebackType
from typing import Any, Literal, Optional

from aiohttp import ClientSession
from aiohttp import __version__ as aiohttp_version

from delphinium import __version__ as delphinium_version
from delphinium.dtos.thumbnail import Size
from delphinium.error import DelphiniumHTTPError
from delphinium.types import (
    HeliotropeGalleryinfoJSON,
    HeliotropeInfoJSON,
    HeliotropeListResultDTOJSON,
    HeliotropeResolvedImageJSON,
    HeliotropeSearchResultDTOJSON,
    HeliotropeTagsJSON,
)


class DelphiniumHTTP:
    UA = f"Delphinium (https://github.com/Saebasol/Delphinium {delphinium_version}) Python/{python_version()} aiohttp/{aiohttp_version}"

    def __init__(
        self, base_url: str, client_session: Optional[ClientSession] = None
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.client_session = client_session

    async def request(
        self,
        method: Literal["GET", "POST"],
        path: str,
        json: Optional[dict[str, Any]] = None,
    ) -> Any:
        url = self.base_url + "/api/hitomi" + path

        if not self.client_session:
            self.client_session = ClientSession()

        async with self.client_session.request(
            method, url, json=json, headers={"user-agent": self.UA}
        ) as resp:
            body = await resp.json()

            if resp.status != 200:
                raise DelphiniumHTTPError(body["message"])

            return body

    async def get_galleryinfo(self, id: int) -> HeliotropeGalleryinfoJSON:
        return await self.request("GET", f"/galleryinfo/{id}")

    async def get_image(self, id: int) -> list[HeliotropeResolvedImageJSON]:
        return await self.request("GET", f"/image/{id}")

    async def get_info(self, id: int) -> HeliotropeInfoJSON:
        return await self.request("GET", f"/info/{id}")

    async def get_list(self, index: int) -> HeliotropeListResultDTOJSON:
        return await self.request("GET", f"/list/{index}")

    async def get_tags(self) -> HeliotropeTagsJSON:
        return await self.request("GET", "/tags")

    async def get_thumbnail(
        self,
        id: int,
        size: Size,
        single: bool,
    ) -> list[HeliotropeResolvedImageJSON]:
        single_str = "true" if single else "false"
        return await self.request(
            "GET", f"/thumbnail/{id}?size={size.value}&single={single_str}"
        )

    async def post_random(self, query: list[str]) -> HeliotropeInfoJSON:
        return await self.request("POST", "/random", {"query": query})

    async def post_search(
        self, query: list[str], offset: int
    ) -> HeliotropeSearchResultDTOJSON:
        return await self.request(
            "POST",
            f"/search?offset={offset}",
            {
                "query": query,
            },
        )

    async def __aenter__(self) -> "DelphiniumHTTP":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.client_session:
            await self.client_session.close()
