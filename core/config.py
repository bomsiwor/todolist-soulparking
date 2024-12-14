from typing import Literal
from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="SOULPARKING_BE_")

    APP_NAME: str = "Soulparking BE Todolist"
    APP_ENV: Literal["development", "production"] = "development"
    DEBUG: bool = True
    AUTHOR: str = "admin"
    PORT: PositiveInt = 8012


def get_config() -> Config:
    return Config()


config = get_config()
