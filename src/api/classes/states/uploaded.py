from aws import cloud
from cache import metadata_cache, text_cache
from classes.abc import PasteProtocol, PasteState
from database import paste_db as db

from .deleted import Deleted


class Uploaded(PasteState):
    def __init__(self, paste: PasteProtocol, text: str, hash: str) -> None:
        self.__paste = paste
        self.__text = text
        self.__hash = hash

    @property
    def text(self) -> str:
        return self.__text

    @property
    def hash(self) -> str:
        return self.__hash

    def upload(self) -> None:
        raise FileExistsError("Paste is already uploaded")

    def download(self) -> None:
        raise FileExistsError("Paste is already downloaded")

    def delete(self) -> None:
        path = (
            cached
            if (cached := metadata_cache.get(self.__hash)) is not None
            else db.get(self.__hash).path
        )
        metadata_cache.delete(self.__hash)
        text_cache.delete(path)
        cloud.delete(path)
        db.delete(self.__hash)

        self.__paste.state = Deleted()
