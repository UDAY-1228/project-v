"""
Placement Cell - Services Layer
================================
Business logic for all Placement Cell modules.
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
    async def get_stats() -> Dict[str, Any]:
        stats = {
            "total_companies": await get_collection("companies").count_documents({}),
            "active_drives": await get_collection("job_drives").count_documents({"status": "completed"}),
            "total_applications": await get_collection("applications").count_documents({}),
            "placed_students": await get_collection("applications").count_documents({"final_status": "selected"}),
            "pending_applications": await get_collection("applications").count_documents({"status": "pending"}),
            "upcoming_drives": await get_collection("job_drives").count_documents({"status": "pending"}),
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


class CompanyService:

    @staticmethod
    async def create_company(data: dict) -> str:
        col = get_collection("companies")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_companies(industry: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("companies")
        query = {}
        if industry:
            query["industry"] = industry
        if status:
            query["status"] = status
        cursor = col.find(query).sort("company_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_company(company_id: str) -> Optional[Dict]:
        col = get_collection("companies")
        doc = await col.find_one({"_id": ObjectId(company_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_company(company_id: str, data: dict) -> bool:
        col = get_collection("companies")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(company_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_company(company_id: str) -> bool:
        col = get_collection("companies")
        result = await col.delete_one({"_id": ObjectId(company_id)})
        return result.deleted_count > 0


class JobDriveService:

    @staticmethod
    async def create_job_drive(data: dict) -> str:
        col = get_collection("job_drives")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_job_drives(
        status: Optional[str] = None,
        company_id: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict]:
        col = get_collection("job_drives")
        query = {}
        if status:
            query["status"] = status
        if company_id:
            query["company_id"] = company_id
        cursor = col.find(query).sort("drive_date", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def get_job_drive(drive_id: str) -> Optional[Dict]:
        col = get_collection("job_drives")
        doc = await col.find_one({"_id": ObjectId(drive_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_job_drive(drive_id: str, data: dict) -> bool:
        col = get_collection("job_drives")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(drive_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_job_drive(drive_id: str) -> bool:
        col = get_collection("job_drives")
        result = await col.delete_one({"_id": ObjectId(drive_id)})
        return result.deleted_count > 0


class ApplicationService:

    @staticmethod
    async def create_application(data: dict) -> str:
        col = get_collection("applications")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_applications(
        student_id: Optional[str] = None,
        drive_id: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 200
    ) -> List[Dict]:
        col = get_collection("applications")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if drive_id:
            query["drive_id"] = drive_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("applied_date", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def get_application(application_id: str) -> Optional[Dict]:
        col = get_collection("applications")
        doc = await col.find_one({"_id": ObjectId(application_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_application(application_id: str, data: dict) -> bool:
        col = get_collection("applications")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(application_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_application(application_id: str) -> bool:
        col = get_collection("applications")
        result = await col.delete_one({"_id": ObjectId(application_id)})
        return result.deleted_count > 0

    @staticmethod
    async def bulk_update_status(application_ids: List[str], status: str) -> int:
        col = get_collection("applications")
        result = await col.update_many(
            {"_id": {"$in": [ObjectId(aid) for aid in application_ids]}},
            {"$set": {"status": status, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count


class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("placement_reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(report_type: Optional[str] = None, academic_year: Optional[str] = None) -> List[Dict]:
        col = get_collection("placement_reports")
        query = {}
        if report_type:
            query["report_type"] = report_type
        if academic_year:
            query["academic_year"] = academic_year
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("placement_reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("placement_reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
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
