from dataclasses import dataclass

from phlox.entities.base import HeliotropeEntity


@dataclass
class Character(HeliotropeEntity):
    character: str
    url: str
