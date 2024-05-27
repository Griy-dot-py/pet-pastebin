from typing import Protocol, Optional
from datetime import datetime

from .state import PasteState


class PasteProtocol(Protocol):   
    @property
    def state(self) -> str:
        ...
        
    @state.setter
    def state(self, state: PasteState) -> None:
        ...
    
    @property
    def text(self) -> Optional[datetime]:
        ...
    
    @property
    def hash(self) -> Optional[str]:
        ...
    
    def upload(self) -> None:
        ...
    
    def download(self) -> None:
        ...
