from flasgger import Schema, fields


class PasteHashSchema(Schema):
    hash = fields.Str(example="AAAAAAAAAAE=")
