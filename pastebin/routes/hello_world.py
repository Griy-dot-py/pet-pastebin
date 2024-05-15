from routes import app
from config import POSTGRES_HOST


@app.get("/hello_world")
def get_hello_world():
    return {"message": "Hello, World!", "db_host": POSTGRES_HOST}
