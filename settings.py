from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_DB_URL: str
    DB: str
    MY_COLLECTION: str
    mode: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    if settings.mode == "test":
        settings.DB = "test-" + settings.DB
    return settings
