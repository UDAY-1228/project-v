"""
VID API Gateway – Configuration Settings
"""
import os
from datetime import timedelta


class Config:
    """Base configuration."""

    # ── App ──────────────────────────────────────────────────────────────
    APP_NAME = "VID API Gateway"
    VERSION  = "1.0.0"
    DEBUG    = False
    TESTING  = False

    # ── Security ──────────────────────────────────────────────────────────
    SECRET_KEY     = os.environ.get("SECRET_KEY", "vid-secret-change-in-production")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "vid-jwt-secret-change-in-production")
    JWT_ACCESS_TOKEN_EXPIRES  = timedelta(hours=int(os.environ.get("JWT_ACCESS_EXPIRE_HOURS", 1)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.environ.get("JWT_REFRESH_EXPIRE_DAYS", 30)))

    # ── Database ─────────────────────────────────────────────────────────
    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "postgresql://vid_user:vid_password@localhost:5432/vid_db"
    )

    # ── CORS ─────────────────────────────────────────────────────────────
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "http://localhost:3000").split(",")

    # ── Rate Limiting ─────────────────────────────────────────────────────
    RATELIMIT_DEFAULT          = "200 per day;50 per hour"
    RATELIMIT_STORAGE_URL      = os.environ.get("REDIS_URL", "memory://")
    RATELIMIT_HEADERS_ENABLED  = True

    # ── Microservice URLs ─────────────────────────────────────────────────
    AUTH_SERVICE_URL            = os.environ.get("AUTH_SERVICE_URL",           "http://localhost:8001")
    STUDENT_SERVICE_URL         = os.environ.get("STUDENT_SERVICE_URL",        "http://localhost:8002")
    FACULTY_SERVICE_URL         = os.environ.get("FACULTY_SERVICE_URL",        "http://localhost:8003")
    ACADEMIC_SERVICE_URL        = os.environ.get("ACADEMIC_SERVICE_URL",       "http://localhost:8004")
    EXAMINATION_SERVICE_URL     = os.environ.get("EXAMINATION_SERVICE_URL",    "http://localhost:8005")
    ATTENDANCE_SERVICE_URL      = os.environ.get("ATTENDANCE_SERVICE_URL",     "http://localhost:8006")
    PAYMENT_SERVICE_URL         = os.environ.get("PAYMENT_SERVICE_URL",        "http://localhost:8007")
    TIMETABLE_SERVICE_URL       = os.environ.get("TIMETABLE_SERVICE_URL",      "http://localhost:8008")
    NOTICE_SERVICE_URL          = os.environ.get("NOTICE_SERVICE_URL",         "http://localhost:8009")
    INSTITUTION_SERVICE_URL     = os.environ.get("INSTITUTION_SERVICE_URL",    "http://localhost:8010")

    # ── Logging ───────────────────────────────────────────────────────────
    LOG_LEVEL  = os.environ.get("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = "postgresql://vid_user:vid_password@localhost:5432/vid_test_db"


class ProductionConfig(Config):
    pass


config_map = {
    "development": DevelopmentConfig,
    "testing":     TestingConfig,
    "production":  ProductionConfig,
}


def get_config() -> Config:
    env = os.environ.get("FLASK_ENV", "development")
    return config_map.get(env, DevelopmentConfig)()
