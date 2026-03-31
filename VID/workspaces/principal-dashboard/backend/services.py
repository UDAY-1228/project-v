"""
Principal Dashboard - Services Layer
=====================================
Business logic for Principal Dashboard modules.
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
            "total_students": await get_collection("student_stats").count_documents({}),
            "total_staff": await get_collection("staff_stats").count_documents({}),
            "total_departments": await get_collection("institution_overview").count_documents({}),
            "total_courses": await get_collection("reports").count_documents({}),
            "pending_approvals": await get_collection("policies").count_documents({"status": "pending"}),
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


class InstitutionOverviewService:

    @staticmethod
    async def create_overview(data: dict) -> str:
        col = get_collection("institution_overview")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_overviews() -> List[Dict]:
        col = get_collection("institution_overview")
        cursor = col.find().sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_overview(overview_id: str) -> Optional[Dict]:
        col = get_collection("institution_overview")
        doc = await col.find_one({"_id": ObjectId(overview_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_overview(overview_id: str, data: dict) -> bool:
        col = get_collection("institution_overview")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(overview_id)}, {"$set": data})
        return result.modified_count > 0


class StaffStatsService:

    @staticmethod
    async def create_stats(data: dict) -> str:
        col = get_collection("staff_stats")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_stats() -> List[Dict]:
        col = get_collection("staff_stats")
        cursor = col.find().sort("department_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_stats_by_department(department_id: str) -> List[Dict]:
        col = get_collection("staff_stats")
        cursor = col.find({"department_id": department_id})
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def update_stats(stats_id: str, data: dict) -> bool:
        col = get_collection("staff_stats")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(stats_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_stats(stats_id: str) -> bool:
        col = get_collection("staff_stats")
        result = await col.delete_one({"_id": ObjectId(stats_id)})
        return result.deleted_count > 0


class StudentStatsService:

    @staticmethod
    async def create_stats(data: dict) -> str:
        col = get_collection("student_stats")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_stats() -> List[Dict]:
        col = get_collection("student_stats")
        cursor = col.find().sort("course_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_stats_by_course(course_id: str) -> List[Dict]:
        col = get_collection("student_stats")
        cursor = col.find({"course_id": course_id})
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def update_stats(stats_id: str, data: dict) -> bool:
        col = get_collection("student_stats")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(stats_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_stats(stats_id: str) -> bool:
        col = get_collection("student_stats")
        result = await col.delete_one({"_id": ObjectId(stats_id)})
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


class PolicyService:

    @staticmethod
    async def create_policy(data: dict) -> str:
        col = get_collection("policies")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_policies(policy_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("policies")
        query = {"policy_type": policy_type} if policy_type else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_policy(policy_id: str) -> Optional[Dict]:
        col = get_collection("policies")
        doc = await col.find_one({"_id": ObjectId(policy_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_policy(policy_id: str, data: dict) -> bool:
        col = get_collection("policies")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(policy_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_policy(policy_id: str) -> bool:
        col = get_collection("policies")
        result = await col.delete_one({"_id": ObjectId(policy_id)})
        return result.deleted_count > 0


class SettingsService:

    @staticmethod
    async def get_settings(institution_id: Optional[str] = None) -> Optional[Dict]:
        col = get_collection("settings")
        query = {"institution_id": institution_id} if institution_id else {}
        doc = await col.find_one(query)
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict, institution_id: Optional[str] = None) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        if institution_id:
            data["institution_id"] = institution_id
        existing = await col.find_one({"institution_id": institution_id} if institution_id else {})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)
