import json
import sys

from pydantic import BaseModel, field_validator


class TimeDeltaForm(BaseModel):
    months: int | None = None
    days: int | None = None
    hours: int | None = None
    minutes: int | None = None


class NewPasteForm(BaseModel):
    text: str
    expires: str | TimeDeltaForm

    @field_validator("text")
    @classmethod
    def validate_text(cls, text: str) -> str:
        if sys.getsizeof(text) / 1024**2 > 10:
            raise ValueError("Max paste size - 10Mb")
        return text

    @field_validator("expires")
    @classmethod
    def validate_expiration(cls, expires: str | TimeDeltaForm) -> TimeDeltaForm:
        if isinstance(expires, str):
            model = TimeDeltaForm(**json.loads(expires))
        elif isinstance(expires, TimeDeltaForm):
            model = expires
        else:
            raise ValueError("Invalid 'expires' param type")

        return model
