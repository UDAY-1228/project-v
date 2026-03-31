"""
Common - Services Layer
========================
Business logic for all Common modules.
Each service class handles CRUD + domain-specific operations.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection
import hashlib
import secrets


def _serialize(doc: dict) -> dict:
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _verify_password(password: str, hashed: str) -> bool:
    return _hash_password(password) == hashed


def _generate_token() -> str:
    return secrets.token_urlsafe(32)


class AuthService:

    @staticmethod
    async def login(email: str, password: str) -> Optional[Dict]:
        col = get_collection("users")
        user = await col.find_one({"email": email.lower()})
        if user and _verify_password(password, user.get("password_hash", "")):
            token = _generate_token()
            await col.update_one(
                {"_id": user["_id"]},
                {"$set": {"last_login": datetime.utcnow(), "session_token": token}}
            )
            return {
                "user_id": str(user["_id"]),
                "email": user["email"],
                "name": f"{user.get('first_name', '')} {user.get('last_name', '')}".strip(),
                "role": user.get("role", "user"),
                "workspace": user.get("workspace"),
                "access_token": token,
            }
        return None

    @staticmethod
    async def register(data: dict) -> str:
        col = get_collection("users")
        existing = await col.find_one({"email": data["email"].lower()})
        if existing:
            raise ValueError("Email already registered")

        user_data = {
            "email": data["email"].lower(),
            "password_hash": _hash_password(data["password"]),
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "phone": data.get("phone"),
            "organization": data.get("organization"),
            "role": "user",
            "status": "pending",
            "is_verified": False,
            "verification_token": _generate_token(),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
        result = await col.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    async def verify_email(token: str) -> bool:
        col = get_collection("users")
        result = await col.update_one(
            {"verification_token": token},
            {"$set": {"is_verified": True, "status": "active", "verification_token": None}}
        )
        return result.modified_count > 0

    @staticmethod
    async def forgot_password(email: str) -> Optional[str]:
        col = get_collection("users")
        user = await col.find_one({"email": email.lower()})
        if user:
            reset_token = _generate_token()
            await col.update_one(
                {"_id": user["_id"]},
                {"$set": {"reset_token": reset_token, "reset_token_expires": datetime.utcnow()}}
            )
            return reset_token
        return None

    @staticmethod
    async def reset_password(token: str, new_password: str) -> bool:
        col = get_collection("users")
        result = await col.update_one(
            {"reset_token": token},
            {"$set": {"password_hash": _hash_password(new_password), "reset_token": None}}
        )
        return result.modified_count > 0

    @staticmethod
    async def logout(user_id: str) -> bool:
        col = get_collection("users")
        result = await col.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"session_token": None}}
        )
        return result.modified_count > 0


class NotificationService:

    @staticmethod
    async def create_notification(data: dict) -> str:
        col = get_collection("notifications")
        data["is_read"] = False
        data["created_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_user_notifications(user_id: str, unread_only: bool = False) -> List[Dict]:
        col = get_collection("notifications")
        query = {"user_id": user_id}
        if unread_only:
            query["is_read"] = False
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def mark_as_read(notification_id: str) -> bool:
        col = get_collection("notifications")
        result = await col.update_one(
            {"_id": ObjectId(notification_id)},
            {"$set": {"is_read": True, "read_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def mark_all_as_read(user_id: str) -> int:
        col = get_collection("notifications")
        result = await col.update_many(
            {"user_id": user_id, "is_read": False},
            {"$set": {"is_read": True, "read_at": datetime.utcnow()}}
        )
        return result.modified_count

    @staticmethod
    async def delete_notification(notification_id: str) -> bool:
        col = get_collection("notifications")
        result = await col.delete_one({"_id": ObjectId(notification_id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_unread_count(user_id: str) -> int:
        col = get_collection("notifications")
        return await col.count_documents({"user_id": user_id, "is_read": False})


class ProfileService:

    @staticmethod
    async def get_profile(user_id: str) -> Optional[Dict]:
        col = get_collection("profiles")
        doc = await col.find_one({"user_id": user_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def create_profile(user_id: str, data: dict) -> str:
        col = get_collection("profiles")
        profile_data = {
            "user_id": user_id,
            **data,
            "is_verified": False,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
        result = await col.insert_one(profile_data)
        return str(result.inserted_id)

    @staticmethod
    async def update_profile(user_id: str, data: dict) -> bool:
        col = get_collection("profiles")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"user_id": user_id}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def update_avatar(user_id: str, avatar_url: str) -> bool:
        col = get_collection("profiles")
        result = await col.update_one(
            {"user_id": user_id},
            {"$set": {"avatar_url": avatar_url, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def change_password(user_id: str, current_password: str, new_password: str) -> bool:
        users_col = get_collection("users")
        user = await users_col.find_one({"_id": ObjectId(user_id)})
        if not user or not _verify_password(current_password, user.get("password_hash", "")):
            return False
        result = await users_col.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password_hash": _hash_password(new_password), "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0


class SettingsService:

    @staticmethod
    async def get_settings(user_id: str) -> Optional[Dict]:
        col = get_collection("settings")
        doc = await col.find_one({"user_id": user_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(user_id: str, data: dict) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        existing = await col.find_one({"user_id": user_id})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["user_id"] = user_id
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)

    @staticmethod
    async def update_notification_preferences(user_id: str, preferences: dict) -> bool:
        col = get_collection("settings")
        result = await col.update_one(
            {"user_id": user_id},
            {"$set": {"notification_preferences": preferences, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def update_security_settings(user_id: str, security_data: dict) -> bool:
        col = get_collection("settings")
        result = await col.update_one(
            {"user_id": user_id},
            {"$set": {"security": security_data, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0
