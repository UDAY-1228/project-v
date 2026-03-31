"""
Disciplinary Committee - Services Layer
========================================
Business logic for Disciplinary Committee modules.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection


def _serialize(doc: dict) -> dict:
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


class DashboardService:

    @staticmethod
    async def get_stats() -> Dict[str, int]:
        stats = {
            "total_complaints": await get_collection("complaints").count_documents({}),
            "pending_complaints": await get_collection("complaints").count_documents({"status": "pending"}),
            "resolved_cases": await get_collection("case_records").count_documents({"status": "resolved"}),
            "active_cases": await get_collection("case_records").count_documents({"status": "investigating"}),
            "escalated_cases": await get_collection("complaints").count_documents({"status": "escalated"}),
        }
        return stats

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def log_activity(action: str, actor: str, module: str, description: str):
        col = get_collection("activity_log")
        await col.insert_one({
            "action": action,
            "actor": actor,
            "module": module,
            "description": description,
            "timestamp": datetime.utcnow(),
        })


class ComplaintService:

    @staticmethod
    async def create_complaint(data: dict) -> str:
        col = get_collection("complaints")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_complaints(status: Optional[str] = None, priority: Optional[str] = None) -> List[Dict]:
        col = get_collection("complaints")
        query = {}
        if status:
            query["status"] = status
        if priority:
            query["priority"] = priority
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_complaint(complaint_id: str) -> Optional[Dict]:
        col = get_collection("complaints")
        doc = await col.find_one({"_id": ObjectId(complaint_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_complaint(complaint_id: str, data: dict) -> bool:
        col = get_collection("complaints")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(complaint_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_complaint(complaint_id: str) -> bool:
        col = get_collection("complaints")
        result = await col.delete_one({"_id": ObjectId(complaint_id)})
        return result.deleted_count > 0

    @staticmethod
    async def assign_complaint(complaint_id: str, assigned_to: str) -> bool:
        col = get_collection("complaints")
        result = await col.update_one(
            {"_id": ObjectId(complaint_id)},
            {"$set": {"assigned_to": assigned_to, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0


class CaseRecordService:

    @staticmethod
    async def create_case_record(data: dict) -> str:
        col = get_collection("case_records")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_case_records(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("case_records")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_case_record(case_id: str) -> Optional[Dict]:
        col = get_collection("case_records")
        doc = await col.find_one({"_id": ObjectId(case_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def get_case_by_complaint(complaint_id: str) -> Optional[Dict]:
        col = get_collection("case_records")
        doc = await col.find_one({"complaint_id": complaint_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_case_record(case_id: str, data: dict) -> bool:
        col = get_collection("case_records")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(case_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_case_record(case_id: str) -> bool:
        col = get_collection("case_records")
        result = await col.delete_one({"_id": ObjectId(case_id)})
        return result.deleted_count > 0


class ActionService:

    @staticmethod
    async def create_action(data: dict) -> str:
        col = get_collection("actions")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_actions(case_id: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("actions")
        query = {}
        if case_id:
            query["case_id"] = case_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_action(action_id: str) -> Optional[Dict]:
        col = get_collection("actions")
        doc = await col.find_one({"_id": ObjectId(action_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_action(action_id: str, data: dict) -> bool:
        col = get_collection("actions")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(action_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_action(action_id: str) -> bool:
        col = get_collection("actions")
        result = await col.delete_one({"_id": ObjectId(action_id)})
        return result.deleted_count > 0


class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
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
