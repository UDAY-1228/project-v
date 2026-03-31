"""
AI-Yantra - Services Layer
===========================
Business logic for all AI-Yantra modules.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection
import secrets
import hashlib


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


class DashboardService:
    @staticmethod
    async def get_stats() -> Dict[str, Any]:
        return {
            "total_models": await get_collection("models").count_documents({}),
            "active_models": await get_collection("models").count_documents({"status": "running"}),
            "total_automations": await get_collection("automations").count_documents({}),
            "active_automations": await get_collection("automations").count_documents({"is_active": True}),
            "api_calls_today": 1247,
            "success_rate": 99.2,
        }

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class AuthService:
    @staticmethod
    async def logout(user_id: str) -> bool:
        col = get_collection("users")
        result = await col.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"session_token": None}}
        )
        return result.modified_count > 0


class AIToolService:
    @staticmethod
    async def create_tool(data: dict) -> str:
        col = get_collection("ai_tools")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_tools(category: Optional[str] = None) -> List[Dict]:
        col = get_collection("ai_tools")
        query = {"category": category} if category else {}
        cursor = col.find(query).sort("name", 1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_tool(tool_id: str) -> Optional[Dict]:
        col = get_collection("ai_tools")
        doc = await col.find_one({"_id": ObjectId(tool_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_tool(tool_id: str, data: dict) -> bool:
        col = get_collection("ai_tools")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(tool_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_tool(tool_id: str) -> bool:
        col = get_collection("ai_tools")
        result = await col.delete_one({"_id": ObjectId(tool_id)})
        return result.deleted_count > 0

    @staticmethod
    async def toggle_tool_status(tool_id: str) -> bool:
        col = get_collection("ai_tools")
        doc = await col.find_one({"_id": ObjectId(tool_id)})
        if doc:
            new_status = "active" if doc.get("status") == "inactive" else "inactive"
            await col.update_one({"_id": ObjectId(tool_id)}, {"$set": {"status": new_status, "updated_at": datetime.utcnow()}})
            return True
        return False


class AutomationService:
    @staticmethod
    async def create_automation(data: dict) -> str:
        col = get_collection("automations")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_automations(is_active: Optional[bool] = None) -> List[Dict]:
        col = get_collection("automations")
        query = {"is_active": is_active} if is_active is not None else {}
        cursor = col.find(query).sort("name", 1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_automation(automation_id: str) -> Optional[Dict]:
        col = get_collection("automations")
        doc = await col.find_one({"_id": ObjectId(automation_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_automation(automation_id: str, data: dict) -> bool:
        col = get_collection("automations")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(automation_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_automation(automation_id: str) -> bool:
        col = get_collection("automations")
        result = await col.delete_one({"_id": ObjectId(automation_id)})
        return result.deleted_count > 0

    @staticmethod
    async def toggle_automation(automation_id: str) -> bool:
        col = get_collection("automations")
        doc = await col.find_one({"_id": ObjectId(automation_id)})
        if doc:
            await col.update_one({"_id": ObjectId(automation_id)}, {"$set": {"is_active": not doc.get("is_active", True), "updated_at": datetime.utcnow()}})
            return True
        return False

    @staticmethod
    async def run_automation(automation_id: str) -> bool:
        col = get_collection("automations")
        await col.update_one({"_id": ObjectId(automation_id)}, {"$set": {"last_run": datetime.utcnow()}, "$inc": {"run_count": 1}})
        return True


class ModelControlService:
    @staticmethod
    async def create_model(data: dict) -> str:
        col = get_collection("models")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_models() -> List[Dict]:
        col = get_collection("models")
        cursor = col.find().sort("name", 1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_model(model_id: str) -> Optional[Dict]:
        col = get_collection("models")
        doc = await col.find_one({"_id": ObjectId(model_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_model(model_id: str, data: dict) -> bool:
        col = get_collection("models")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(model_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_model(model_id: str) -> bool:
        col = get_collection("models")
        result = await col.delete_one({"_id": ObjectId(model_id)})
        return result.deleted_count > 0

    @staticmethod
    async def start_model(model_id: str) -> bool:
        col = get_collection("models")
        result = await col.update_one({"_id": ObjectId(model_id)}, {"$set": {"status": "running", "updated_at": datetime.utcnow()}})
        return result.modified_count > 0

    @staticmethod
    async def stop_model(model_id: str) -> bool:
        col = get_collection("models")
        result = await col.update_one({"_id": ObjectId(model_id)}, {"$set": {"status": "stopped", "updated_at": datetime.utcnow()}})
        return result.modified_count > 0


class AnalyticsService:
    @staticmethod
    async def get_metrics(metric_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("analytics")
        query = {"metric_type": metric_type} if metric_type else {}
        cursor = col.find(query).sort("timestamp", -1).limit(100)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def record_metric(data: dict) -> str:
        col = get_collection("analytics")
        data["timestamp"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)


class ReportService:
    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["created_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(report_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("reports")
        query = {"report_type": report_type} if report_type else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
        return result.deleted_count > 0


class SettingsService:
    @staticmethod
    async def get_settings() -> Optional[Dict]:
        col = get_collection("settings")
        doc = await col.find_one({})
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        existing = await col.find_one({})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)