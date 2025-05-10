from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Dynalyz"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    API_PREFIX: str = "/api"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    DB_ENGINE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    TELEGRAM_BOT_TOKEN: str
    WEBHOOK_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()
