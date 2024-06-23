import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv()


BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")
ICON_SRC = "https://cdn-icons-png.flaticon.com/128/2040/2040523.png"
GITHUB = "https://github.com/Griy-dot-py/pet-pastebin"
