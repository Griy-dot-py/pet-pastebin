from flask import Flask, request


app = Flask(__name__)


from .hello_world import get_hello_world
