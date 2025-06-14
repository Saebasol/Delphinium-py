from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Info(HeliotropeEntity):
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
    date: datetime
