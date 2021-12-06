from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    title: str = "Title"
    description: str = (
        "Description"
    )
    version: str = "0.1.0"
    debug: bool = Field(False, env="DEBUG")

    API_PREFIX: str = "/api"
    JWT_TOKEN_PREFIX: str = "Token"
    
    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    database_url: str = Field(
        "postgresql://postgres:postgres@db:5432/postgres", env="DATABASE_URL"
    )

    class Config:
        env_file = ".env"


settings = Settings()