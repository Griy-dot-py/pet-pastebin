from typing import Optional
from datetime import datetime

from database import Paste as PasteModel
from database import database
from aws import cloud

from .states import Draft, Uploaded
from .abc import PasteProtocol

from utils import unhash_id


class Paste(PasteProtocol):
    _cloud = cloud
    _db = database
    
    def __init__(self, text: str, user_id: int, lifetime_days: int = 30) -> None:
        self.text = text
        self._model = PasteModel(user_id=user_id)
        self._state = Draft(self, lifetime_days)
    
    def __repr__(self) -> str:
        return f"Paste(text='{self.text}', hash='{self._state.hash}', expires='{self._state.expires}')"
    
    @property
    def expires(self) -> Optional[datetime]:
        return self._state.expires
    
    @property
    def hash(self) -> Optional[str]:
        return self._state.hash
    
    def upload(self) -> None:
        return self._state.upload()
    
    @classmethod
    def download(cls, hash: str) -> "Paste":
        model = cls._db.get(unhash_id(hash))
        if model is None:
            raise FileNotFoundError("Paste not found")
        text = cls._cloud.download(model.path)
        
        paste = cls(text=text, user_id=model.user_id)
        paste._state = Uploaded(paste)
        paste._model = model
        return paste
