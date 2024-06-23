from classes.abc import PasteState


class Deleted(PasteState):
    @property
    def text(self) -> None:
        return None

    @property
    def hash(self) -> None:
        return None

    def upload(self) -> None:
        raise FileNotFoundError("Paste is deleted")

    def download(self) -> None:
        raise FileNotFoundError("Paste is deleted")

    def delete(self) -> None:
        raise FileNotFoundError("Paste is already deleted")
