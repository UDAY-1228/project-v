"""
Application Configuration using Pydantic Settings
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    APP_NAME: str = "EIMS"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # MongoDB
    MONGO_URL: str = "mongodb://localhost:27017/eims_db"
    MONGO_DB_NAME: str = "eims_db"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # JWT
    JWT_SECRET: str = "eims_super_secret_key_change_in_production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY: int = 3600  # seconds
    REFRESH_TOKEN_EXPIRY: int = 604800  # 7 days

    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:4200",
        "http://localhost:80",
        "http://localhost",
    ]

    # File Storage
    UPLOAD_PATH: str = "./uploads"
    ML_MODEL_PATH: str = "./ml/models"
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB

    # Email (SMTP)
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    FROM_EMAIL: str = "noreply@eims.edu.in"

    # Twilio SMS
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE: str = ""

    # Feature Flags
    FACE_RECOGNITION_ENABLED: bool = True
    AI_TIMETABLE_ENABLED: bool = True
    AI_HOMEWORK_HELPER_ENABLED: bool = True

    # Localization
    DEFAULT_LANGUAGE: str = "en"
    SUPPORTED_LANGUAGES: List[str] = ["en", "te"]  # English + Telugu
    TIMEZONE: str = "Asia/Kolkata"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
