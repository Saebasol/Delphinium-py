from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Character(HeliotropeEntity):
    character: str
    url: str
