"""
Alumni Management - Services Layer
===================================
Business logic for all Alumni Management modules.
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
            "total_alumni": await get_collection("alumni_database").count_documents({}),
            "verified_alumni": await get_collection("alumni_database").count_documents({"is_verified": True}),
            "total_donations": await get_collection("donations").count_documents({"status": "completed"}),
            "pending_donations": await get_collection("donations").count_documents({"status": "pending"}),
            "total_events": await get_collection("events").count_documents({}),
            "active_reports": await get_collection("reports").count_documents({"status": "active"}),
        }
        return stats

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class AlumniDatabaseService:

    @staticmethod
    async def create_alumni(data: dict) -> str:
        col = get_collection("alumni_database")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_alumni(department: Optional[str] = None, graduation_year: Optional[int] = None) -> List[Dict]:
        col = get_collection("alumni_database")
        query = {}
        if department:
            query["department"] = department
        if graduation_year:
            query["graduation_year"] = graduation_year
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_alumni(alumni_id: str) -> Optional[Dict]:
        col = get_collection("alumni_database")
        doc = await col.find_one({"_id": ObjectId(alumni_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_alumni(alumni_id: str, data: dict) -> bool:
        col = get_collection("alumni_database")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(alumni_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_alumni(alumni_id: str) -> bool:
        col = get_collection("alumni_database")
        result = await col.delete_one({"_id": ObjectId(alumni_id)})
        return result.deleted_count > 0

    @staticmethod
    async def verify_alumni(alumni_id: str) -> bool:
        col = get_collection("alumni_database")
        result = await col.update_one(
            {"_id": ObjectId(alumni_id)},
            {"$set": {"is_verified": True, "verified_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def search_alumni(query: str) -> List[Dict]:
        col = get_collection("alumni_database")
        search_query = {
            "$or": [
                {"first_name": {"$regex": query, "$options": "i"}},
                {"last_name": {"$regex": query, "$options": "i"}},
                {"email": {"$regex": query, "$options": "i"}},
                {"current_company": {"$regex": query, "$options": "i"}},
            ]
        }
        cursor = col.find(search_query).limit(50)
        return _serialize_list(await cursor.to_list(length=50))


class DonationsService:

    @staticmethod
    async def create_donation(data: dict) -> str:
        col = get_collection("donations")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_donations(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("donations")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("donation_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_donation(donation_id: str) -> Optional[Dict]:
        col = get_collection("donations")
        doc = await col.find_one({"_id": ObjectId(donation_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_donation(donation_id: str, data: dict) -> bool:
        col = get_collection("donations")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(donation_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_donation(donation_id: str) -> bool:
        col = get_collection("donations")
        result = await col.delete_one({"_id": ObjectId(donation_id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_total_donations() -> float:
        col = get_collection("donations")
        pipeline = [
            {"$match": {"status": "completed"}},
            {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
        ]
        result = await col.aggregate(pipeline).to_list(length=1)
        return result[0]["total"] if result else 0.0

    @staticmethod
    async def get_donations_by_donor(donor_id: str) -> List[Dict]:
        col = get_collection("donations")
        cursor = col.find({"donor_id": donor_id}).sort("donation_date", -1)
        return _serialize_list(await cursor.to_list(length=100))


class CampaignsService:

    @staticmethod
    async def create_campaign(data: dict) -> str:
        col = get_collection("campaigns")
        data["raised_amount"] = 0.0
        data["created_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_campaigns(active_only: bool = False) -> List[Dict]:
        col = get_collection("campaigns")
        query = {"is_active": True} if active_only else {}
        cursor = col.find(query).sort("start_date", -1)
        return _serialize_list(await cursor.to_list(length=50))

    @staticmethod
    async def get_campaign(campaign_id: str) -> Optional[Dict]:
        col = get_collection("campaigns")
        doc = await col.find_one({"_id": ObjectId(campaign_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_campaign(campaign_id: str, data: dict) -> bool:
        col = get_collection("campaigns")
        result = await col.update_one({"_id": ObjectId(campaign_id)}, {"$set": data})
        return result.modified_count > 0


class EventsService:

    @staticmethod
    async def create_event(data: dict) -> str:
        col = get_collection("events")
        data["registered_count"] = 0
        data["attended_count"] = 0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_events(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("events")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("date", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_event(event_id: str) -> Optional[Dict]:
        col = get_collection("events")
        doc = await col.find_one({"_id": ObjectId(event_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_event(event_id: str, data: dict) -> bool:
        col = get_collection("events")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(event_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_event(event_id: str) -> bool:
        col = get_collection("events")
        result = await col.delete_one({"_id": ObjectId(event_id)})
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
    async def update_report(report_id: str, data: dict) -> bool:
        col = get_collection("reports")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(report_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("reports")
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
            result = await col.insert_one(data)
            return str(result.inserted_id)
