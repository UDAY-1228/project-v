from bson import ObjectId
from .mongodb_connection import get_db_connection
from .models import User, Notice
from datetime import datetime

db = get_db_connection()
users_collection = db["users"]
workspaces_collection = db["workspaces"]
notices_collection = db["notices"]

class UserService:
    @staticmethod
    def create_user(data: dict):
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = users_collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_user_by_id(user_id: str):
        return users_collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_all_users():
        return list(users_collection.find())

    @staticmethod
    def update_user(user_id: str, data: dict):
        data["updated_at"] = datetime.utcnow()
        result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    def toggle_user_activation(user_id: str, is_active: bool):
        result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"is_active": is_active}})
        return result.modified_count > 0

    @staticmethod
    def assign_workspace(user_id: str, workspace_ids: list):
        result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$addToSet": {"workspaces": {"$each": workspace_ids}}})
        return result.modified_count > 0

class WorkspaceService:
    @staticmethod
    def get_all_workspaces():
        return list(workspaces_collection.find())

    @staticmethod
    def update_workspace_access(workspace_id: str, data: dict):
        result = workspaces_collection.update_one({"_id": ObjectId(workspace_id)}, {"$set": data})
        return result.modified_count > 0

class NoticeService:
    @staticmethod
    def create_notice(data: dict):
        data["created_at"] = datetime.utcnow()
        result = notices_collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_all_notices():
        return list(notices_collection.find())

    @staticmethod
    def delete_notice(notice_id: str):
        result = notices_collection.delete_one({"_id": ObjectId(notice_id)})
        return result.deleted_count > 0

class AnalyticsService:
    @staticmethod
    def get_admin_dashboard_stats():
        return {
            "institution_overview": {"total_users": users_collection.count_documents({}), "active_workspaces": workspaces_collection.count_documents({})},
            "trending_analytics": [],
            "user_activity_summary": {"new_registrations": 0},
            "workspace_activity_summary": {"most_active": "workspace_1"},
            "recent_operations": []
        }
