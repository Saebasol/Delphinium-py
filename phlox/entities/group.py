from dataclasses import dataclass

from phlox.entities.base import HeliotropeEntity


@dataclass
class Group(HeliotropeEntity):
    group: str
    url: str
