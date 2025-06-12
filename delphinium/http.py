from platform import python_version
from types import TracebackType
from typing import Any, Literal, Optional

from aiohttp import ClientSession
from aiohttp import __version__ as aiohttp_version

from delphinium import __version__ as delphinium_version
from delphinium.error import PhloxHTTPError
from delphinium.types import (
    HeliotropeFilesJSON,
    HeliotropeGalleryinfoJSON,
    HeliotropeInfoJSON,
    HeliotropeListJSON,
    HeliotropeSearchJSON,
)


class PhloxHTTP:
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
        url = self.base_url + path

        if not self.client_session:
            self.client_session = ClientSession()

        async with self.client_session.request(
            method, url, json=json, headers={"user-agent": self.UA}
        ) as resp:
            body = await resp.json()

            if resp.status != 200:
                raise PhloxHTTPError(body["message"])

            return body

    async def get_galleryinfo(self, index: int) -> HeliotropeGalleryinfoJSON:
        return await self.request("GET", f"/api/hitomi/galleryinfo/{index}")

    async def get_image(self, index: int) -> HeliotropeFilesJSON:
        return await self.request("GET", f"/api/hitomi/image/{index}")

    async def get_info(self, index: int) -> HeliotropeInfoJSON:
        return await self.request("GET", f"/api/hitomi/info/{index}")

    async def get_list(self, index: int) -> HeliotropeListJSON:
        return await self.request("GET", f"/api/hitomi/list/{index}")

    async def get_random(self, query: list[str]) -> HeliotropeInfoJSON:
        return await self.request("POST", "/api/hitomi/random", {"query": query})

    async def post_search(self, query: list[str], offset: int) -> HeliotropeSearchJSON:
        return await self.request(
            "POST",
            "/api/hitomi/search",
            {
                "query": query,
                "offset": offset,
            },
        )

    async def __aenter__(self) -> "PhloxHTTP":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.client_session:
            await self.client_session.close()
