from datetime import datetime, timedelta
from typing import Optional

import tasks.tasks as tasks
from aws import cloud
from cache import hash_cache
from classes.abc import PasteProtocol, PasteState
from database import PasteModel
from database import paste_db as db

from .uploaded import Uploaded


class Draft(PasteState):
    def __init__(
        self,
        paste: PasteProtocol,
        text: str,
        user_id: Optional[int] = None,
        expires: Optional[timedelta] = None,
    ) -> None:
        self.__paste = paste
        self.__text = text
        self.__model = PasteModel(user_id=user_id)
        self.__expires = expires

    @property
    def text(self) -> str:
        return self.__text

    @property
    def hash(self) -> None:
        return None

    def upload(self) -> None:
        self.__model.hash = hash_cache.get_hash()
        self.__model.path = cloud.upload(self.__text, self.__model.user_id)
        db.add(self.__model)
        self.__paste.state = Uploaded(
            paste=self.__paste, text=self.__text, hash=self.__model.hash
        )
        if self.__expires is not None:
            self.__set_paste_expiration()

    def download(self) -> None:
        raise FileNotFoundError("Paste is not uploaded yet")

    def delete(self) -> None:
        raise FileNotFoundError("Paste is not uploaded")

    def __set_paste_expiration(self) -> None:
        secs = self.__expires.total_seconds()
        if secs < 1800:
            tasks.del_paste.apply_async(args=(self.__paste,), countdown=secs - 3)
        else:
            exipres_on = datetime.now() + self.__expires - timedelta(seconds=1)
            tasks.del_paste.apply_async(args=(self.__paste,), eta=exipres_on)
