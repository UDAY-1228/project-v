"""
Principal Dashboard - MongoDB Connection
=========================================
Async MongoDB connection using Motor for the Principal Dashboard workspace.
"""

import os
import logging
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("principal_dashboard.db")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "vid_db")
COLLECTION_PREFIX = "pd_"

client = None
db = None


async def connect_to_database():
    """Initialize MongoDB connection on application startup."""
    global client, db
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        await client.admin.command("ping")
        logger.info(f"✅ Principal Dashboard DB connected → {DB_NAME}")
    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {e}")
        raise


async def close_database_connection():
    """Close MongoDB connection on application shutdown."""
    global client
    if client:
        client.close()
        logger.info("🔌 Principal Dashboard DB connection closed")


async def get_database():
    """Dependency injection for database access."""
    if db is None:
        await connect_to_database()
    return db


def get_collection(collection_name: str):
    """Get a prefixed collection from the database."""
    if db is None:
        raise RuntimeError("Database not initialized. Call connect_to_database() first.")
    return db[f"{COLLECTION_PREFIX}{collection_name}"]
