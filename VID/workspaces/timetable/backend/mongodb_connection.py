"""
Timetable - MongoDB Connection
================================
Async MongoDB connection using Motor for the Timetable workspace.
"""

import os
import logging
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("timetable.db")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "vid_db")
COLLECTION_PREFIX = "tt_"

client = None
db = None


async def connect_to_database():
    global client, db
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        await client.admin.command("ping")
        logger.info(f"✅ Timetable DB connected → {DB_NAME}")
    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {e}")
        raise


async def close_database_connection():
    global client
    if client:
        client.close()
        logger.info("🔌 Timetable DB connection closed")


async def get_database():
    if db is None:
        await connect_to_database()
    return db


def get_collection(collection_name: str):
    if db is None:
        raise RuntimeError("Database not initialized. Call connect_to_database() first.")
    return db[f"{COLLECTION_PREFIX}{collection_name}"]
