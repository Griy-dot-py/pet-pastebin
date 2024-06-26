from datetime import datetime, timedelta
from typing import Optional, overload

from .abc import PasteProtocol, PasteState
from .states import Draft, Restored


class Paste(PasteProtocol):
    @property
    def state(self) -> str:
        return type(self.__state).__name__

    @state.setter
    def state(self, state: PasteState) -> None:
        self.__state = state

    @overload
    def __init__(
        self,
        text: str,
        user_id: Optional[int] = None,
        expires: Optional[timedelta] = None,
    ) -> None: ...

    @overload
    def __init__(self, hash: str) -> None: ...

    def __init__(
        self,
        text: Optional[str] = None,
        user_id: Optional[int] = None,
        expires: Optional[timedelta] = None,
        hash: Optional[str] = None,
    ) -> None:
        if hash is not None:
            self.state = Restored(paste=self, hash=hash)
        elif text is not None:
            self.state = Draft(paste=self, text=text, user_id=user_id, expires=expires)

    def __repr__(self) -> str:
        return f"Paste(text='{self.text}', hash='{self.hash}')"

    @property
    def text(self) -> Optional[datetime]:
        return self.__state.text

    @property
    def hash(self) -> Optional[str]:
        return self.__state.hash

    def upload(self) -> None:
        self.__state.upload()

    def download(self) -> None:
        self.__state.download()

    def delete(self) -> None:
        self.__state.delete()
