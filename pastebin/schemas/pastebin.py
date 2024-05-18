from database import Session, User

from marshmallow import Schema, fields, validates, ValidationError

import sys


class PastebinSchema(Schema):
    text = fields.Str(required=True)
    user_id = fields.Int(required=True, load_only=True)
    
    @validates("text")
    def text_size_validator(self, text: str) -> None:
        size_in_mb: float = sys.getsizeof(text) / 1024**2
        if size_in_mb > 10:
            raise ValidationError("Text size cannot be more than 10Mb")
    
    @validates("user_id")
    def existing_user_validator(self, user_id: int) -> None:
        with Session() as session:
            user = session.get(User, user_id)
            if user is None:
                raise ValidationError("User not found")
