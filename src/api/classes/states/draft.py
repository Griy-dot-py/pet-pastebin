from classes.abc import PasteProtocol

from cache import HashCache
from aws import Cloud
from database import Database, PasteModel

from classes.abc import PasteState
from .uploaded import Uploaded


class Draft(PasteState):
    cloud: Cloud
    db: Database
    cache: HashCache
    
    def __init__(self, paste: PasteProtocol, text: str, user_id: int) -> None:
        self.__paste = paste
        self.__text = text
        self.__model = PasteModel(user_id=user_id)
    
    @property
    def text(self) -> str:
        return self.__text
    
    @property
    def hash(self) -> None:
        return None
    
    def upload(self) -> None:
        self.__model.hash = self.cache.get_hash()
        self.__model.path = self.cloud.upload(
            text=self.__text,
            user_id=self.__model.user_id
        )
        self.db.add(self.__model)
        self.__paste.state = Uploaded(
            text=self.__text,
            hash=self.__model.hash
        )
    
    def download(self) -> None:
        raise FileNotFoundError("Paste is not uploaded yet")
