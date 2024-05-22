from flasgger import swag_from

from resources import api
from flask_restful import Resource

from schemas import PasteInSchema, PasteOutSchema
import binascii

from classes import Paste


@api.resource("/pastebin/<string:hash>")
class PasteResource(Resource):
    schema = PasteInSchema()
    return_schema = PasteOutSchema()
    
    @swag_from("../../../docs/paste/get.yml")
    def get(self, hash: str):
        try:
            paste = Paste.download(hash)
        except (FileNotFoundError, binascii.Error):
            return "pastebin not found", 404
        
        return self.return_schema.dump(paste), 200
