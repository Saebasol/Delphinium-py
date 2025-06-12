from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Artist(HeliotropeEntity):
    artist: str
    url: str
