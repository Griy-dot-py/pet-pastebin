from flasgger import Schema, fields


class PasteBaseSchema(Schema):
    text = fields.Str(required=True, example="Hello, world!")
