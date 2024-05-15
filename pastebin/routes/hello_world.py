from routes import app


@app.get("/hello_world")
def get_hello_world():
    return {"message": "Hello, World!"}
