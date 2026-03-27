import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
app_db_name = os.getenv("MONGO_DB", "vid_database")

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_mongo(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[app_db_name]
        print(f"Connected to MongoDB at {MONGO_URI}")

    async def close_mongo_connection(self):
        if self.client:
            self.client.close()
            print("Closed MongoDB connection")

db = MongoDB()

async def get_database():
    return db.db
