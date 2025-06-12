from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Group(HeliotropeEntity):
    group: str
    url: str
