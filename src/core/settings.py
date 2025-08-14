import os
from functools import cache

from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings


class Config(BaseModel):
    HOST: str
    PORT: int
    DEBUG: bool
    DEV_ENV: str
    LOG_LEVEL: str
    WORKERS_COUNT: int


class PostgreSQL(BaseModel):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    DATABASE: str

    @computed_field
    def URL(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"


class Redis(BaseModel):
    HOST: str
    PORT: int
    USER: str | None = None
    PASSWORD: str | None = None
    DATABASE: int

    @computed_field
    def URL(self) -> str:
        if self.USER and self.PASSWORD:
            return f"redis://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"
        return f"redis://{self.HOST}:{self.PORT}/{self.DATABASE}"


class Bot(BaseModel):
    RUN: bool
    TOKEN: str
    WEBHOOK_URL: str
    NAME: str


class Scheduler(BaseModel):
    RUN: bool


class Settings(BaseSettings):
    postgresql: PostgreSQL
    scheduler: Scheduler
    config: Config
    redis: Redis
    bot: Bot

    class Config:
        extra = "ignore"


@cache
def get_settings():
    env_file = os.getenv("ENV_FILE", ".env")
    return Settings(
        _env_file=env_file,
        _env_file_encoding="utf-8",
        _env_nested_delimiter="__",
    )


settings = get_settings()
