"""
Research Development - Services Layer
======================================
Business logic for Research Development modules.
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
            "total_projects": await get_collection("research_projects").count_documents({}),
            "active_projects": await get_collection("research_projects").count_documents({"status": "in_progress"}),
            "completed_projects": await get_collection("research_projects").count_documents({"status": "completed"}),
            "total_publications": await get_collection("publications").count_documents({}),
            "total_grants": await get_collection("grants").count_documents({}),
            "total_funding_received": 0.0,
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


class ResearchProjectService:

    @staticmethod
    async def create_project(data: dict) -> str:
        col = get_collection("research_projects")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_projects(status: Optional[str] = None, department: Optional[str] = None) -> List[Dict]:
        col = get_collection("research_projects")
        query = {}
        if status:
            query["status"] = status
        if department:
            query["pi_department"] = department
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_project(project_id: str) -> Optional[Dict]:
        col = get_collection("research_projects")
        doc = await col.find_one({"_id": ObjectId(project_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_project(project_id: str, data: dict) -> bool:
        col = get_collection("research_projects")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(project_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_project(project_id: str) -> bool:
        col = get_collection("research_projects")
        result = await col.delete_one({"_id": ObjectId(project_id)})
        return result.deleted_count > 0


class PublicationService:

    @staticmethod
    async def create_publication(data: dict) -> str:
        col = get_collection("publications")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_publications(pub_type: Optional[str] = None, department: Optional[str] = None) -> List[Dict]:
        col = get_collection("publications")
        query = {}
        if pub_type:
            query["publication_type"] = pub_type
        if department:
            query["department"] = department
        cursor = col.find(query).sort("publication_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_publication(publication_id: str) -> Optional[Dict]:
        col = get_collection("publications")
        doc = await col.find_one({"_id": ObjectId(publication_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_publication(publication_id: str, data: dict) -> bool:
        col = get_collection("publications")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(publication_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_publication(publication_id: str) -> bool:
        col = get_collection("publications")
        result = await col.delete_one({"_id": ObjectId(publication_id)})
        return result.deleted_count > 0


class GrantService:

    @staticmethod
    async def create_grant(data: dict) -> str:
        col = get_collection("grants")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_grants(status: Optional[str] = None, agency: Optional[str] = None) -> List[Dict]:
        col = get_collection("grants")
        query = {}
        if status:
            query["status"] = status
        if agency:
            query["funding_agency"] = agency
        cursor = col.find(query).sort("application_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_grant(grant_id: str) -> Optional[Dict]:
        col = get_collection("grants")
        doc = await col.find_one({"_id": ObjectId(grant_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_grant(grant_id: str, data: dict) -> bool:
        col = get_collection("grants")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(grant_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_grant(grant_id: str) -> bool:
        col = get_collection("grants")
        result = await col.delete_one({"_id": ObjectId(grant_id)})
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
