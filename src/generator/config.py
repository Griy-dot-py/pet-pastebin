import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv()

HASH_CACHE_HOST = os.getenv("HASH_CACHE_HOST")
HASH_CACHE_PORT = int(os.getenv("HASH_CACHE_PORT"))
