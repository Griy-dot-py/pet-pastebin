from typing import Optional
from os import PathLike

from classes.abc import PasteProtocol, PasteState
from .uploaded import Uploaded
from .deleted import Deleted

from cache import metadata_cache, text_cache
from aws import cloud
from database import PasteModel, paste_db as db


class Restored(PasteState):
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
        path = self.__find_path(cache_result=True)
        text = self.__find_text(path, cache_result=True)
        self.__paste.state = Uploaded(
            paste=self.__paste,
            text=text,
            hash=self.__hash
        )
    
    def delete(self) -> None:
        path = self.__find_path()
        metadata_cache.delete(self.__hash)
        text_cache.delete(path)
        cloud.delete(path)
        db.delete(self.__hash)
        
        self.__paste.state = Deleted()
    
    def __find_path(self, *, cache_result: bool = False) -> Optional[PathLike]:
        path = metadata_cache.get(self.__hash)
        if path is None:
            model: Optional[PasteModel] = db.get(self.__hash)
            if model is not None:
                path = model.path
        
        if path is not None:
            if cache_result:
                metadata_cache.set(self.__hash, path)
            return path
        
        raise FileNotFoundError("Paste not found")
    
    def __find_text(self, path: PathLike, *, cache_result: bool = False) -> str:
        text = text_cache.get(path)
        if text is None:
            text = cloud.download(path)
        
        if text is not None:
            if cache_result:
                text_cache.set(path, text)
            return text
        
        raise FileNotFoundError("Paste not found")
