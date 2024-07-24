from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "iK-kPOtlhIHgj3yu5f7xYbI2K7X7QL2qZ2izLdoEiEnXT9u34aas1KuPFTcdvW_KPdvJJwWRwM9D5IGnT3kBCQ"
    DATABASE_URL: str = "sqlite:///./master.db"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


settings = Settings()