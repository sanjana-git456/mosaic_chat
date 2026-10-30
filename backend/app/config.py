import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MosaicChat"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "super-secret-mosaic-key-2024")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql://postgres:protoXdummydb@db.ubkfcuroqilgrzzitmrm.supabase.co:5432/postgres")
    CORS_ORIGINS: str = os.environ.get("CORS_ORIGINS", "*")

settings = Settings()