from typing import Protocol, Optional


class PasteState(Protocol):
    def upload(self) -> None:
        ...
    
    @property
    def expires(self) -> Optional[str]:
        ...
    
    @property
    def hash(self) -> Optional[str]:
        ...
