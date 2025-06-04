from dataclasses import dataclass

from phlox.entities.base import HeliotropeEntity


@dataclass
class Artist(HeliotropeEntity):
    artist: str
    url: str
