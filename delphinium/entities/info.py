from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Info(HeliotropeEntity):
    id: int
    title: str
    thumbnail: str
    artist: list[str]
    group: list[str]
    type: str
    language: Optional[str]
    series: list[str]
    character: list[str]
    tag: list[str]
    date: datetime
