from pymongo import MongoClient
import os

def get_db_connection():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongo_uri)
    db = client["vid_core_system"]
    return db
