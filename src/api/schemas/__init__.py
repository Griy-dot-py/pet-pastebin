from .timedelta import TimeDeltaSchema
from .paste_base import PasteBaseSchema

from .paste_in import PasteInSchema
from .paste_out import PasteOutSchema
from .paste_hash import PasteHashSchema

definitions = [
    TimeDeltaSchema,
    PasteInSchema,
    PasteOutSchema,
    PasteHashSchema
]
