from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flasgger import APISpec, Swagger
from flask import Flask, request  # noqa
from flask_restful import Api
from schemas import definitions

app = Flask(__name__)
api = Api(app, prefix="/api")
spec = APISpec(
    title="PastebinAPI",
    version="0.1.0",
    openapi_version="2.0",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


from .new_paste import NewPasteResource  # noqa
from .paste import PasteResource  # noqa

template = spec.to_flasgger(app, definitions)
Swagger(app, template=template)
