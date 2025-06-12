from dataclasses import dataclass
from typing import Optional

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Language(HeliotropeEntity):
    galleryid: Optional[int]
    language_localname: str
    name: str
    url: str
