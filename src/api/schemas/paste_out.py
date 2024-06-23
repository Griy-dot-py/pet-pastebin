from flasgger import fields

from .paste_base import PasteBaseSchema


class PasteOutSchema(PasteBaseSchema):
    text = fields.Str(example="Hello, world!")
