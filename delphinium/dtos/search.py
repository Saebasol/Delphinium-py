from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity
from delphinium.entities.info import Info


@dataclass
class SearchResultDTO(HeliotropeEntity):
    result: list[Info]
    count: int
