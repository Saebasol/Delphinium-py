from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Parody(HeliotropeEntity):
    parody: str
    url: str
