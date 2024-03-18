from os import getenv

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = getenv("APP_NAME", "backend")
    debug: bool = bool(getenv("DEBUG", False))
    database_uri: str  = getenv("DATABASE_URI", "sqlite+aiosqlite:///test.db")
    env: str = getenv("ENV", "dev")
    version: str = getenv("VERSION", "1.0.0")

    class Config:
        env_file = "/.env"

