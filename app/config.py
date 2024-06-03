from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm_hash: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()