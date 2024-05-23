from classes.abc import PasteProtocol as Paste

from dataclasses import dataclass
from classes.abc import PasteState

from utils import hash_id


@dataclass
class Uploaded(PasteState):
    paste: Paste
        
    def upload(self):
        raise FileExistsError("Pastebin is already uploaded")
    
    @property
    def expires(self):
        self.paste._cloud.check_expiration(self.paste._model.path)
    
    @property
    def hash(self):
        return hash_id(self.paste._model.id)
