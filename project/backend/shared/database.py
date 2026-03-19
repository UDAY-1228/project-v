"""
MongoDB async connection using Motor
"""
from motor.motor_asyncio import AsyncIOMotorClient
from loguru import logger
from .config import settings

client: AsyncIOMotorClient = None


async def connect_db():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URL)
    logger.info(f"Connected to MongoDB: {settings.MONGO_URL}")


async def disconnect_db():
    global client
    if client:
        client.close()
        logger.info("Disconnected from MongoDB")


def get_db():
    return client[settings.MONGO_DB_NAME]


def get_collection(name: str):
    return get_db()[name]
