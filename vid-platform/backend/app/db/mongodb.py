import os
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = "vid_platform"

settings = Settings()

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_obj = MongoDB()

async def connect_to_mongo():
    db_obj.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db_obj.db = db_obj.client[settings.DATABASE_NAME]
    print(f"Connected to MongoDB at {settings.MONGODB_URL}")

async def close_mongo_connection():
    db_obj.client.close()
    print("Closed MongoDB connection")

def get_database():
    return db_obj.db
