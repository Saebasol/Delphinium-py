from typing import Optional, TypedDict


class BaseHeliotropeJSON(TypedDict): ...


class HeliotropeFileJSON(BaseHeliotropeJSON):
    hasavif: bool
    hash: str
    height: int
    name: str
    width: int
    hasjxl: bool
    haswebp: bool
    single: bool


class HeliotropeTagJSON(BaseHeliotropeJSON):
    tag: str
    url: str
    female: bool
    male: bool


class HeliotropeParodysJSON(BaseHeliotropeJSON):
    parody: str
    url: str


class HeliotropeArtistsJSON(BaseHeliotropeJSON):
    artist: str
    url: str


class HeliotropeCharactersJSON(BaseHeliotropeJSON):
    character: str
    url: str


class HeliotropeGroupsJSON(BaseHeliotropeJSON):
    group: str
    url: str


class HeliotropeLanguagesJSON(BaseHeliotropeJSON):
    galleryid: str
    language_localname: str
    name: str
    url: str


class HeliotropeGalleryinfoJSON(BaseHeliotropeJSON):
    galleryurl: str
    id: int
    japanese_title: Optional[str]
    language_localname: str
    language_url: str
    language: str
    title: str
    type: str
    video: Optional[str]
    videofilename: Optional[str]
    blocked: bool
    datepublished: Optional[str]
    artists: list[HeliotropeArtistsJSON]
    characters: list[HeliotropeCharactersJSON]
    files: list[HeliotropeFileJSON]
    groups: list[HeliotropeGroupsJSON]
    languages: list[HeliotropeLanguagesJSON]
    parodys: list[HeliotropeParodysJSON]
    related: list[int]
    scene_indexes: list[int]
    tags: list[HeliotropeTagJSON]
    date: str


class HeliotropeInfoJSON(BaseHeliotropeJSON):
    id: int
    title: str
    thumbnail: str
    artists: list[str]
    groups: list[str]
    type: str
    language: Optional[str]
    series: list[str]
    characters: list[str]
    tags: list[str]
    date: str


class HeliotropeResolvedImageJSON(BaseHeliotropeJSON):
    url: str
    file: HeliotropeFileJSON


class HeliotropeListResultDTOJSON(BaseHeliotropeJSON):
    items: list[HeliotropeInfoJSON]
    count: int


class HeliotropeSearchResultDTOJSON(BaseHeliotropeJSON):
    result: list[HeliotropeInfoJSON]
    count: int


class HeliotropeTagsJSON(BaseHeliotropeJSON):
    artists: list[str]
    groups: list[str]
    series: list[str]
    characters: list[str]
    tag: list[str]
    male: list[str]
    female: list[str]
    type: list[str]
    language: list[str]
