from typing import Protocol, Optional


class PasteState(Protocol):
    @property
    def text(self) -> Optional[str]:
        ...
    
    @property
    def hash(self) -> Optional[str]:
        ...
    
    def upload(self) -> None:
        ...
    
    def download(self) -> None:
        ...
