"""
Library Admin - Services Layer
==============================
Business logic for all Library Admin modules.
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
            "total_books": await get_collection("books").count_documents({}),
            "issued_books": await get_collection("issues").count_documents({"status": "issued"}),
            "available_books": await get_collection("books").count_documents({"status": "available"}),
            "total_members": await get_collection("members").count_documents({}),
            "overdue_books": await get_collection("issues").count_documents({"status": "overdue"}),
            "total_fines_collected": await DashboardService._get_total_fines(),
        }
        return stats

    @staticmethod
    async def _get_total_fines() -> float:
        col = get_collection("fines")
        pipeline = [{"$group": {"_id": None, "total": {"$sum": "$amount"}}}]
        cursor = col.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        return result[0]["total"] if result else 0.0

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class BookControlService:

    @staticmethod
    async def create_book(data: dict) -> str:
        col = get_collection("books")
        data["accession_number"] = f"ACC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_books(category: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("books")
        query = {}
        if category:
            query["category"] = category
        if status:
            query["status"] = status
        cursor = col.find(query).sort("title", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_book(book_id: str) -> Optional[Dict]:
        col = get_collection("books")
        doc = await col.find_one({"_id": ObjectId(book_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_book(book_id: str, data: dict) -> bool:
        col = get_collection("books")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(book_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_book(book_id: str) -> bool:
        col = get_collection("books")
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
        await IssueReturnService._update_book_availability(data["book_id"], -1)
        return str(result.inserted_id)

    @staticmethod
    async def return_book(issue_id: str, fine_amount: float = 0.0) -> bool:
        col = get_collection("issues")
        doc = await col.find_one({"_id": ObjectId(issue_id)})
        if doc:
            await col.update_one(
                {"_id": ObjectId(issue_id)},
                {"$set": {"return_date": datetime.utcnow(), "status": "returned", "fine_amount": fine_amount, "updated_at": datetime.utcnow()}}
            )
            await IssueReturnService._update_book_availability(doc["book_id"], 1)
            return True
        return False

    @staticmethod
    async def _update_book_availability(book_id: str, change: int) -> None:
        col = get_collection("books")
        await col.update_one({"_id": ObjectId(book_id)}, {"$inc": {"available_copies": change}})

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
    async def get_member_issues(member_id: str) -> List[Dict]:
        col = get_collection("issues")
        cursor = col.find({"member_id": member_id}).sort("issue_date", -1)
        return _serialize_list(await cursor.to_list(length=100))


class FineControlService:

    @staticmethod
    async def create_fine(data: dict) -> str:
        col = get_collection("fines")
        data["issued_date"] = datetime.utcnow()
        data["created_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_fines(member_id: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("fines")
        query = {}
        if member_id:
            query["member_id"] = member_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("issued_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_fine(fine_id: str) -> Optional[Dict]:
        col = get_collection("fines")
        doc = await col.find_one({"_id": ObjectId(fine_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_fine(fine_id: str, data: dict) -> bool:
        col = get_collection("fines")
        result = await col.update_one({"_id": ObjectId(fine_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def pay_fine(fine_id: str) -> bool:
        col = get_collection("fines")
        result = await col.update_one(
            {"_id": ObjectId(fine_id)},
            {"$set": {"status": "paid", "paid_date": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def calculate_fine(issue_id: str, fine_per_day: float) -> float:
        col = get_collection("issues")
        doc = await col.find_one({"_id": ObjectId(issue_id)})
        if doc and doc.get("status") == "issued":
            days_overdue = (datetime.utcnow() - doc["due_date"]).days
            return max(0, days_overdue * fine_per_day)
        return 0.0


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
