from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Thumbnail(HeliotropeEntity):
    url: list[str]
