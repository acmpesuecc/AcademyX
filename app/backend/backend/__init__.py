from os import getenv

from dotenv import load_dotenv

from backend.core.settings import Settings

load_dotenv(getenv("/.env"))

settings = Settings()