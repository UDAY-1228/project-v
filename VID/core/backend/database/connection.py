import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

class Database:
    client: Optional[AsyncIOMotorClient] = None
    db = None

    @classmethod
    async def connect_to_mongodb(cls):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.getenv("DB_NAME", "vid_db")
        cls.client = AsyncIOMotorClient(mongo_url)
        cls.db = cls.client[db_name]
        print(f"Connected to MongoDB: {db_name}")

    @classmethod
    async def close_mongodb_connection(cls):
        if cls.client:
            cls.client.close()
            print("Closed MongoDB connection")

db = Database()
