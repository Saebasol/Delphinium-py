from dataclasses import dataclass

from yggdrasil.application.dtos.list import ListResultDTO as YggdrasilListResultDTO
from yggdrasil.domain.deserializer import Deserializer


@dataclass
class ListResultDTO(YggdrasilListResultDTO, Deserializer): ...
