from init import app
import routes #noqa


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
