"""
Alumni Coordinator - Services Layer
====================================
Business logic for all Alumni Coordinator modules.
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
            "total_alumni": await get_collection("alumni_records").count_documents({}),
            "total_events": await get_collection("events").count_documents({}),
            "upcoming_events": await get_collection("events").count_documents({"date": {"$gte": datetime.utcnow()}, "status": "active"}),
            "total_communications": await get_collection("communications").count_documents({}),
            "active_reports": await get_collection("reports").count_documents({"status": "active"}),
            "recent_activities": await get_collection("activity_log").count_documents({}),
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


class AlumniRecordsService:

    @staticmethod
    async def create_alumni(data: dict) -> str:
        col = get_collection("alumni_records")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_alumni(department: Optional[str] = None, graduation_year: Optional[int] = None) -> List[Dict]:
        col = get_collection("alumni_records")
        query = {}
        if department:
            query["department"] = department
        if graduation_year:
            query["graduation_year"] = graduation_year
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_alumni(alumni_id: str) -> Optional[Dict]:
        col = get_collection("alumni_records")
        doc = await col.find_one({"_id": ObjectId(alumni_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_alumni(alumni_id: str, data: dict) -> bool:
        col = get_collection("alumni_records")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(alumni_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_alumni(alumni_id: str) -> bool:
        col = get_collection("alumni_records")
        result = await col.delete_one({"_id": ObjectId(alumni_id)})
        return result.deleted_count > 0

    @staticmethod
    async def search_alumni(query: str) -> List[Dict]:
        col = get_collection("alumni_records")
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

    @staticmethod
    async def register_attendee(event_id: str, data: dict) -> str:
        col = get_collection("event_registrations")
        data["event_id"] = event_id
        data["registration_date"] = datetime.utcnow()
        result = await col.insert_one(data)
        await get_collection("events").update_one({"_id": ObjectId(event_id)}, {"$inc": {"registered_count": 1}})
        return str(result.inserted_id)

    @staticmethod
    async def get_registrations(event_id: str) -> List[Dict]:
        col = get_collection("event_registrations")
        cursor = col.find({"event_id": event_id})
        return _serialize_list(await cursor.to_list(length=200))


class CommunicationService:

    @staticmethod
    async def create_communication(data: dict) -> str:
        col = get_collection("communications")
        data["sent_count"] = 0
        data["opened_count"] = 0
        data["clicked_count"] = 0
        data["failed_count"] = 0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_communications(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("communications")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_communication(comm_id: str) -> Optional[Dict]:
        col = get_collection("communications")
        doc = await col.find_one({"_id": ObjectId(comm_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_communication(comm_id: str, data: dict) -> bool:
        col = get_collection("communications")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(comm_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_communication(comm_id: str) -> bool:
        col = get_collection("communications")
        result = await col.delete_one({"_id": ObjectId(comm_id)})
        return result.deleted_count > 0

    @staticmethod
    async def send_communication(comm_id: str) -> bool:
        col = get_collection("communications")
        result = await col.update_one(
            {"_id": ObjectId(comm_id)},
            {"$set": {"status": "sent", "sent_at": datetime.utcnow()}}
        )
        return result.modified_count > 0


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
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)
