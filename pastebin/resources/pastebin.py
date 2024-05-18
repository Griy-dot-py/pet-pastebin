from resources import api, request
from flask_restful import Resource

from schemas import PastebinSchema
from marshmallow import ValidationError

from classes import Pastebin


@api.resource("/pastebin/", "/pastebin/<id>")
class PastebinResource(Resource):
    schema = PastebinSchema()
    
    def post(self):
        try:
            data = self.schema.load(request.json)
        except ValidationError as exc:
            return exc.messages, 400
        
        paste = Pastebin(**data)
        paste.upload()
        return {"id": paste.hashed_id}, 201
    
    def get(self, id: str = None):
        if id is None:
            return "pastebin ID is required", 400
        try:
            paste = Pastebin.download(id)
        except FileNotFoundError:
            return "pastebin not found", 404
        
        return self.schema.dump(paste), 200
