from schemas import TimeDeltaSchema, PasteBaseSchema

from database import user_db

from flasgger import fields
from marshmallow import validates, ValidationError

import sys


class PasteInSchema(PasteBaseSchema):
    user_id = fields.Int(load_only=True)
    expires = fields.Nested(TimeDeltaSchema)
    
    @validates("text")
    def text_size_validator(self, text: str) -> None:
        size_in_mb: float = sys.getsizeof(text) / 1024**2
        if size_in_mb > 10:
            raise ValidationError("Text size cannot be more than 10Mb")
    
    @validates("user_id")
    def existing_user_validator(self, user_id: int) -> None:
        user = user_db.get(user_id)
        if user is None:
            raise ValidationError("User not found")
