from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity
from delphinium.entities.info import Info


@dataclass
class ListResultDTO(HeliotropeEntity):
    items: list[Info]
    count: int
