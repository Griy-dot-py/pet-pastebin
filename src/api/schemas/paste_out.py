from flasgger import fields
from schemas import PasteBaseSchema


class PasteOutSchema(PasteBaseSchema):
    text = fields.Str(example="Hello, world!")
