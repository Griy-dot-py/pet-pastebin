from schemas import PasteBaseSchema
from flasgger import fields


class PasteOutSchema(PasteBaseSchema):
    text = fields.Str(example="Hello, world!")
