from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

from phlox.entities.artist import Artist
from phlox.entities.base import HeliotropeEntity
from phlox.entities.character import Character
from phlox.entities.file import File
from phlox.entities.group import Group
from phlox.entities.language import Language
from phlox.entities.parody import Parody
from phlox.entities.tag import Tag


@dataclass
class Galleryinfo(HeliotropeEntity):
    date: datetime
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
    datepublished: Optional[date]
    artists: list[Artist]
    characters: list[Character]
    files: list[File]
    groups: list[Group]
    languages: list[Language]
    parodys: list[Parody]
    related: list[int]
    scene_indexes: list[int]
    tags: list[Tag]
