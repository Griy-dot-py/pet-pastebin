from classes.abc import PasteProtocol as Paste

from dataclasses import dataclass
from classes.abc import PasteState
from .uploaded import Uploaded


@dataclass
class Draft(PasteState):
    paste: Paste
    lifetime_days: int
    
    def upload(self):
        path = self.paste._cloud.upload(
            text=self.paste.text,
            user_id=self.paste._model.user_id,
            lifetime_days=self.lifetime_days
        )
        self.paste._model.path = path
        self.paste._db.add(self.paste._model)
        
        self.paste._state = Uploaded(self.paste)
        
    @property
    def expires(self):
        return None
    
    @property
    def hash(self):
        return None
