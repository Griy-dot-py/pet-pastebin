from typing import Protocol, Optional
from datetime import datetime

from aws import Cloud
from database import Database

from database import Paste as PasteModel

from .state import PasteState


class PasteProtocol(Protocol):
    text: str
    _model: PasteModel
    
    _cloud: Cloud
    _db: Database
    
    _state: PasteState
    
    @property
    def expires(self) -> Optional[datetime]:
        ...
    
    @property
    def hash(self) -> Optional[str]:
        ...
    
    def upload(self) -> None:
        ...
    
    @classmethod
    def download(cls) -> str:
        ...
