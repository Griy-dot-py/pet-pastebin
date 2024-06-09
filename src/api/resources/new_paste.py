from resources import api, request
from flask_restful import Resource

from flasgger import swag_from

from schemas import PasteInSchema, PasteHashSchema
from marshmallow import ValidationError
from config.apidocs import PATH as DOCS_PATH
from classes import Paste


@api.resource("/pastebin/")
class NewPasteResource(Resource):
    schema = PasteInSchema()
    return_schema = PasteHashSchema()
    
    @swag_from(f"{DOCS_PATH}/paste/post.yml")
    def post(self):
        try:
            data = self.schema.load(request.json)
        except ValidationError as exc:
            return exc.messages, 400
        
        paste = Paste(**data)
        paste.upload()
        return self.return_schema.dump(paste), 201
