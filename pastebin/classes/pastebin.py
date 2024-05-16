from utils import hash_id, unhash_id
from database import Paste, Session
from sqlalchemy import select


class Pastebin(object):   
    def __init__(self, text: str, user_id: int) -> None:
        self.text = text
        self.__model = Paste(user_id=user_id)
        self.__session = Session()
    
    def __del__(self) -> None:
        self.__session.close()
    
    def __repr__(self) -> str:
        return f"Pastebin(hashed_id={self.hashed_id}, text={self.text})"
    
    @property
    def is_uploaded(self) -> bool:
        try:
            self.__model.id
        except AttributeError:
            return False
        return True
    
    @property
    def hashed_id(self) -> str:
        if not self.is_uploaded:
            raise AttributeError("Pastebin is not uploaded yet")
        return hash_id(self.__model.id)
    
    def upload(self) -> None:
        if self.is_uploaded:
            raise FileExistsError("Pastebin is already uploaded")
        path = ... # Загружаем текст в облако
        with self.__session.begin():
            self.__model.path = path
            self.__session.add(self.__model)
    
    @classmethod
    def download(cls, hashed_id: str) -> "Pastebin":
        model_id = unhash_id(hashed_id)
        with Session() as session:
            model = session.scalar(select(Paste).filter_by(id=model_id))
        text = ... #Выгружаем данные из облакa
        pastebin = cls(text=text, user_id=model.user_id)
        pastebin.__model = model
        return pastebin
    