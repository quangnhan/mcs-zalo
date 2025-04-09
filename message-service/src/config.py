from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET_KEY: str = "your_default_secret"
    JWT_ALGORITHM: str = "HS256"
    FIREBASE_CREDENTIALS_PATH: str = "firebase-credentials.json"

    class Config:
        env_file = ".env"

settings = Settings()
