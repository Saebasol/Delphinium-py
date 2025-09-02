from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Tags(HeliotropeEntity):
    artists: list[str]
    groups: list[str]
    series: list[str]
    characters: list[str]
    tag: list[str]
    male: list[str]
    female: list[str]
    type: list[str]
    language: list[str]
