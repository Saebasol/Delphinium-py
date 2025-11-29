from dataclasses import dataclass

from yggdrasil.application.dtos.search import (
    SearchResultDTO as YggdrasilSearchResultDTO,
)
from yggdrasil.domain.deserializer import Deserializer


@dataclass
class SearchResultDTO(YggdrasilSearchResultDTO, Deserializer): ...
