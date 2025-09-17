from dataclasses import dataclass

from delphinium.entities.base import HeliotropeEntity
from delphinium.entities.file import File


@dataclass
class ResolvedImage(HeliotropeEntity):
    url: str
    file: File
