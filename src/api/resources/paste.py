import binascii

from classes import Paste
from config.apidocs import PATH as DOCS_PATH
from flasgger import swag_from
from flask_restful import Resource
from resources import api
from schemas import PasteInSchema, PasteOutSchema


@api.resource("/paste/<string:hash>")
class PasteResource(Resource):
    schema = PasteInSchema()
    return_schema = PasteOutSchema()

    @swag_from(f"{DOCS_PATH}/paste/get.yml")
    def get(self, hash: str):
        try:
            paste = Paste(hash=hash)
            paste.download()
        except (FileNotFoundError, binascii.Error):
            return "paste not found", 404

        return self.return_schema.dump(paste), 200
