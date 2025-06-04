from dataclasses import dataclass

from phlox.entities.base import HeliotropeEntity


@dataclass
class Parody(HeliotropeEntity):
    parody: str
    url: str
