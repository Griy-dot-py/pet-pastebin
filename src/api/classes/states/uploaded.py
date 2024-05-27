from classes.abc import PasteProtocol

from classes.abc import PasteState
from database import PasteModel


class Uploaded(PasteState):
    def __init__(self, paste: PasteProtocol, text: str, model: PasteModel) -> None:
        self.__paste = paste
        self.__text = text
        self.__model = model
    
    @property
    def text(self) -> str:
        return self.__text
    
    @property
    def hash(self) -> str:
        return self.__model.hash
            
    def upload(self) -> None:
        raise FileExistsError("Paste is already uploaded")
    
    def download(self) -> None:
        raise FileExistsError("Paste is already uploaded")
