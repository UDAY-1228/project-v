"""
Library Management - Services Layer
====================================
Business logic for all Library Management modules.
"""

from bson import ObjectId
from datetime import datetime, timedelta
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
            "total_catalog_books": await get_collection("catalog").count_documents({}),
            "total_issues": await get_collection("issues").count_documents({}),
            "active_members": await get_collection("members").count_documents({"status": "active"}),
            "reserved_books": await get_collection("catalog").count_documents({"status": "reserved"}),
            "overdue_returns": await get_collection("issues").count_documents({"status": "overdue"}),
            "monthly_issues": await DashboardService._get_monthly_issues(),
        }
        return stats

    @staticmethod
    async def _get_monthly_issues() -> int:
        col = get_collection("issues")
        start_of_month = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return await col.count_documents({"issue_date": {"$gte": start_of_month}})

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class BookCatalogService:

    @staticmethod
    async def add_book(data: dict) -> str:
        col = get_collection("catalog")
        data["accession_number"] = f"ACC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        data["copies_total"] = data.get("copies_total", 1)
        data["copies_available"] = data.get("copies_available", 1)
        data["times_issued"] = 0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_books(category: Optional[str] = None, search: Optional[str] = None) -> List[Dict]:
        col = get_collection("catalog")
        query = {}
        if category:
            query["category"] = category
        if search:
            query["$or"] = [
                {"title": {"$regex": search, "$options": "i"}},
                {"author": {"$regex": search, "$options": "i"}},
                {"isbn": {"$regex": search, "$options": "i"}}
            ]
        cursor = col.find(query).sort("title", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_book(book_id: str) -> Optional[Dict]:
        col = get_collection("catalog")
        doc = await col.find_one({"_id": ObjectId(book_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_book(book_id: str, data: dict) -> bool:
        col = get_collection("catalog")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(book_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_book(book_id: str) -> bool:
        col = get_collection("catalog")
        result = await col.delete_one({"_id": ObjectId(book_id)})
        return result.deleted_count > 0


class IssueReturnService:

    @staticmethod
    async def issue_book(data: dict) -> str:
        col = get_collection("issues")
        data["issue_date"] = datetime.utcnow()
        data["due_date"] = datetime.utcnow() + timedelta(days=14)
        data["status"] = "issued"
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        await IssueReturnService._increment_book_issues(data["book_id"])
        await IssueReturnService._update_member_issued(data["member_id"], 1)
        return str(result.inserted_id)

    @staticmethod
    async def return_book(issue_id: str, remarks: Optional[str] = None) -> bool:
        col = get_collection("issues")
        doc = await col.find_one({"_id": ObjectId(issue_id)})
        if doc:
            update_data = {"return_date": datetime.utcnow(), "status": "returned", "updated_at": datetime.utcnow()}
            if remarks:
                update_data["remarks"] = remarks
            await col.update_one({"_id": ObjectId(issue_id)}, {"$set": update_data})
            await IssueReturnService._update_member_issued(doc["member_id"], -1)
            return True
        return False

    @staticmethod
    async def _increment_book_issues(book_id: str) -> None:
        col = get_collection("catalog")
        await col.update_one({"_id": ObjectId(book_id)}, {"$inc": {"times_issued": 1}})

    @staticmethod
    async def _update_member_issued(member_id: str, change: int) -> None:
        col = get_collection("members")
        await col.update_one({"_id": ObjectId(member_id)}, {"$inc": {"books_issued": change}})

    @staticmethod
    async def get_all_issues(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("issues")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("issue_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_issue(issue_id: str) -> Optional[Dict]:
        col = get_collection("issues")
        doc = await col.find_one({"_id": ObjectId(issue_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def get_member_history(member_id: str) -> List[Dict]:
        col = get_collection("issues")
        cursor = col.find({"member_id": member_id}).sort("issue_date", -1)
        return _serialize_list(await cursor.to_list(length=100))


class MemberRecordsService:

    @staticmethod
    async def create_member(data: dict) -> str:
        col = get_collection("members")
        data["member_id"] = f"MBR-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        data["books_issued"] = 0
        data["fines_pending"] = 0.0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_members(member_type: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("members")
        query = {}
        if member_type:
            query["member_type"] = member_type
        if status:
            query["status"] = status
        cursor = col.find(query).sort("member_name", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_member(member_id: str) -> Optional[Dict]:
        col = get_collection("members")
        doc = await col.find_one({"_id": ObjectId(member_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_member(member_id: str, data: dict) -> bool:
        col = get_collection("members")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(member_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_member(member_id: str) -> bool:
        col = get_collection("members")
        result = await col.delete_one({"_id": ObjectId(member_id)})
        return result.deleted_count > 0


class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["generated_at"] = datetime.utcnow()
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
