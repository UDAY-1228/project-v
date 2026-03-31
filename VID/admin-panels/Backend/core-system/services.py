from .mongodb_connection import get_db_connection
from datetime import datetime, timedelta
import jwt # PyJWT for token generation
import os

db = get_db_connection()
users_collection = db["users"] # For auth
notices_collection = db["notices"]
timetables_collection = db["timetables"]

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")
ALGORITHM = "HS256"

class AuthService:
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(hours=24))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def authenticate_user(username, password):
        user = users_collection.find_one({"username": username})
        if user and user["password_hash"] == password: # Simple hash comparison for demonstration
            return user
        return None

class NoticeBoardService:
    @staticmethod
    def get_notices():
        return list(notices_collection.find().sort("created_at", -1))
    
    @staticmethod
    def get_announcements():
        return list(notices_collection.find({"is_important": True}))

class TimetableService:
    @staticmethod
    def get_user_timetable(user_id):
        return timetables_collection.find_one({"user_id": user_id})

class ProfileService:
    @staticmethod
    def get_profile(user_id):
        return users_collection.find_one({"_id": user_id})
    @staticmethod
    def update_profile(user_id, data):
        return users_collection.update_one({"_id": user_id}, {"$set": data})
