from typing import Optional

from utils import hash_id, unhash_id

from database import Paste as PasteModel
from database import Session
from sqlalchemy import select

from aws import upload_to_cloud, download_from_cloud


class Paste(object):   
    def __init__(self, text: str, user_id: int) -> None:
        self.text = text
        self.__model = PasteModel(user_id=user_id)
        self.__session = Session()
    
    def __del__(self) -> None:
        self.__session.close()
    
    def __repr__(self) -> str:
        return f"Paste(hash='{self.hash}', text='{self.text}')"
    
    @property
    def is_uploaded(self) -> bool:
        return self.__model.id is not None
    
    @property
    def hash(self) -> Optional[str]:
        if self.is_uploaded:
            return hash_id(self.__model.id)
        return None
    
    def upload(self) -> None:
        if self.is_uploaded:
            raise FileExistsError("Pastebin is already uploaded")
        path = upload_to_cloud(self.text, self.__model.user_id)
        with self.__session.begin():
            self.__model.path = path
            self.__session.add(self.__model)
    
    @classmethod
    def download(cls, hash: str) -> "Paste":
        with Session() as session:
            model = session.scalar(select(PasteModel).filter_by(id=unhash_id(hash)))
        if model is None:
            raise FileNotFoundError("Pastebin not found")
        text = download_from_cloud(model.path)
        pastebin = cls(text=text, user_id=model.user_id)
        pastebin.__model = model
        return pastebin
