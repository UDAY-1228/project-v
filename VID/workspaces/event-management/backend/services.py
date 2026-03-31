"""
Event Management - Services Layer
=================================
Business logic for all Event Management modules.
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
            "total_events": await get_collection("events").count_documents({}),
            "upcoming_events": await get_collection("events").count_documents({"status": "active"}),
            "total_registrations": await get_collection("registrations").count_documents({}),
            "completed_events": await get_collection("events").count_documents({"status": "completed"}),
            "total_revenue": 0.0,
            "average_attendance": 0.0,
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
            "action": action, "actor": actor, "module": module,
            "description": description, "timestamp": datetime.utcnow(),
        })


class EventService:
    @staticmethod
    async def create_event(data: dict) -> str:
        col = get_collection("events")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_events(status: Optional[str] = None, event_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("events")
        query = {}
        if status: query["status"] = status
        if event_type: query["event_type"] = event_type
        cursor = col.find(query).sort("start_date", 1)
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
    async def publish_event(event_id: str) -> bool:
        col = get_collection("events")
        result = await col.update_one({"_id": ObjectId(event_id)}, {"$set": {"status": "active", "updated_at": datetime.utcnow()}})
        return result.modified_count > 0


class RegistrationService:
    @staticmethod
    async def register_participant(data: dict) -> str:
        col = get_collection("registrations")
        data["created_at"] = datetime.utcnow()
        data["registration_date"] = datetime.utcnow()
        result = await col.insert_one(data)
        await get_collection("events").update_one({"_id": ObjectId(data["event_id"])}, {"$inc": {"registered_count": 1}})
        return str(result.inserted_id)

    @staticmethod
    async def get_registrations(event_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("registrations")
        query = {"event_id": event_id} if event_id else {}
        cursor = col.find(query).sort("registration_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_registration(registration_id: str) -> Optional[Dict]:
        col = get_collection("registrations")
        doc = await col.find_one({"_id": ObjectId(registration_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def check_in_participant(registration_id: str) -> bool:
        col = get_collection("registrations")
        result = await col.update_one(
            {"_id": ObjectId(registration_id)},
            {"$set": {"attended": True, "checked_in_at": datetime.utcnow()}}
        )
        if result.modified_count > 0:
            doc = await col.find_one({"_id": ObjectId(registration_id)})
            if doc:
                await get_collection("events").update_one({"_id": ObjectId(doc["event_id"])}, {"$inc": {"attended_count": 1}})
        return result.modified_count > 0

    @staticmethod
    async def cancel_registration(registration_id: str) -> bool:
        col = get_collection("registrations")
        result = await col.update_one({"_id": ObjectId(registration_id)}, {"$set": {"status": "cancelled"}})
        return result.modified_count > 0

    @staticmethod
    async def delete_registration(registration_id: str) -> bool:
        col = get_collection("registrations")
        result = await col.delete_one({"_id": ObjectId(registration_id)})
        return result.deleted_count > 0


class ScheduleService:
    @staticmethod
    async def create_schedule(data: dict) -> str:
        col = get_collection("schedules")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_schedules(event_id: str) -> List[Dict]:
        col = get_collection("schedules")
        cursor = col.find({"event_id": event_id}).sort("schedule_date", 1)
        return _serialize_list(await cursor.to_list(length=50))

    @staticmethod
    async def get_schedule(schedule_id: str) -> Optional[Dict]:
        col = get_collection("schedules")
        doc = await col.find_one({"_id": ObjectId(schedule_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_schedule(schedule_id: str, data: dict) -> bool:
        col = get_collection("schedules")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(schedule_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_schedule(schedule_id: str) -> bool:
        col = get_collection("schedules")
        result = await col.delete_one({"_id": ObjectId(schedule_id)})
        return result.deleted_count > 0

    @staticmethod
    async def add_slot(schedule_id: str, slot: dict) -> bool:
        col = get_collection("schedules")
        result = await col.update_one({"_id": ObjectId(schedule_id)}, {"$push": {"slots": slot}})
        return result.modified_count > 0


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

    @staticmethod
    async def generate_event_report(event_id: str) -> Dict:
        event = await EventService.get_event(event_id)
        registrations = await RegistrationService.get_registrations(event_id)
        return {
            "event": event,
            "total_registrations": len(registrations),
            "attended": sum(1 for r in registrations if r.get("attended")),
            "cancelled": sum(1 for r in registrations if r.get("status") == "cancelled"),
        }


class EventSettingsService:
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
