from classes.abc import PasteProtocol

from aws import Cloud
from database import Database

from classes.abc import PasteState
from .uploaded import Uploaded


class Restored(PasteState):
    cloud: Cloud
    db: Database
    
    def __init__(self, paste: PasteProtocol, hash: str) -> None:
        self.__paste = paste
        self.__hash = hash
    
    @property
    def text(self) -> None:
        return None
    
    @property
    def hash(self) -> None:
        return self.__hash
    
    def upload(self) -> None:
        raise FileExistsError("Paste is already uploaded")
    
    def download(self) -> None:
        model = self.db.get(self.__hash)
        if model is None:
            raise FileNotFoundError("Paste not found")
        text = self.cloud.download(model.path)
        
        self.__paste.state = Uploaded(paste=self.__paste, text=text, model=model)
