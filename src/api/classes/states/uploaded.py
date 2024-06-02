from classes.abc import PasteState


class Uploaded(PasteState):
    def __init__(self, text: str, hash: str) -> None:
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
