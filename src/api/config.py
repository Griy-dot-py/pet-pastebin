import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv()


POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

REGION_NAME = os.getenv("REGION_NAME")
S3_STORAGE_URL = os.getenv("S3_STORAGE_URL")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

HASH_CACHE_HOST = os.getenv("HASH_CACHE_HOST")
HASH_CACHE_PORT = int(os.getenv("HASH_CACHE_PORT"))
