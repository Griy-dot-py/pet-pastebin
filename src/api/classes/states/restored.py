from typing import Optional
from os import PathLike

from classes.abc import PasteProtocol

from cache import DataCache
from aws import Cloud
from database import Database, PasteModel

from classes.abc import PasteState
from .uploaded import Uploaded


class Restored(PasteState):
    cloud: Cloud
    db: Database
    metadata_cache: DataCache
    text_cache: DataCache
    
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
        path = self.__find_path()
        text = self.__find_text(path)
        
        self.__paste.state = Uploaded(text=text, hash=self.__hash)
    
    def __find_path(self) -> Optional[PathLike]:
        cached = self.metadata_cache.get(self.__hash)
        if cached is not None:
            return cached
        
        model: Optional[PasteModel] = self.db.get(self.__hash)
        if model is not None:
            self.metadata_cache.set(self.__hash, model.path)
            return model.path
        
        raise FileNotFoundError("Paste not found")
    
    def __find_text(self, path: PathLike) -> str:
        cached = self.text_cache.get(path)
        if cached is not None:
            return cached
        
        text = self.cloud.download(path)
        self.text_cache.set(path, text)
        return text
