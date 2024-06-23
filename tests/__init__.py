import os

from dotenv import find_dotenv, load_dotenv

ENV_PATH = "config/.env"

if not find_dotenv(ENV_PATH):
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv(ENV_PATH)


BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")
