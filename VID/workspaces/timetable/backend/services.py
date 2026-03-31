"""
Timetable - Service Methods
===========================
Service layer for the Timetable workspace.
"""

from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .mongodb_connection import get_collection


def serialize_doc(doc: dict) -> dict:
    if doc is None:
        return None
    doc["_id"] = str(doc["_id"])
    if "created_at" in doc:
        doc["created_at"] = doc["created_at"].isoformat()
    if "updated_at" in doc:
        doc["updated_at"] = doc["updated_at"].isoformat()
    return doc


class ScheduleService:
    collection = "schedules"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        if "slots" not in data:
            data["slots"] = []
        result = await get_collection(ScheduleService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ScheduleService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(schedule_id: str) -> Optional[dict]:
        doc = await get_collection(ScheduleService.collection).find_one({"_id": ObjectId(schedule_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(schedule_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ScheduleService.collection).find_one_and_update(
            {"_id": ObjectId(schedule_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(schedule_id: str) -> bool:
        result = await get_collection(ScheduleService.collection).delete_one({"_id": ObjectId(schedule_id)})
        return result.deleted_count > 0


class ClassAllocationService:
    collection = "class_allocations"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ClassAllocationService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ClassAllocationService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(allocation_id: str) -> Optional[dict]:
        doc = await get_collection(ClassAllocationService.collection).find_one({"_id": ObjectId(allocation_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def get_by_class(class_id: str) -> Optional[dict]:
        doc = await get_collection(ClassAllocationService.collection).find_one({"class_id": class_id})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(allocation_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ClassAllocationService.collection).find_one_and_update(
            {"_id": ObjectId(allocation_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(allocation_id: str) -> bool:
        result = await get_collection(ClassAllocationService.collection).delete_one({"_id": ObjectId(allocation_id)})
        return result.deleted_count > 0


class RoomAllocationService:
    collection = "room_allocations"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        if "amenities" not in data:
            data["amenities"] = []
        result = await get_collection(RoomAllocationService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(RoomAllocationService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(room_id: str) -> Optional[dict]:
        doc = await get_collection(RoomAllocationService.collection).find_one({"_id": ObjectId(room_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(room_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(RoomAllocationService.collection).find_one_and_update(
            {"_id": ObjectId(room_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(room_id: str) -> bool:
        result = await get_collection(RoomAllocationService.collection).delete_one({"_id": ObjectId(room_id)})
        return result.deleted_count > 0


class ReportService:
    collection = "reports"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        result = await get_collection(ReportService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ReportService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_type(report_type: str) -> List[dict]:
        cursor = get_collection(ReportService.collection).find({"report_type": report_type})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]


class DashboardService:
    @staticmethod
    async def get_stats() -> dict:
        total_schedules = await get_collection(ScheduleService.collection).count_documents({})
        total_classes = await get_collection(ClassAllocationService.collection).count_documents({})
        total_rooms = await get_collection(RoomAllocationService.collection).count_documents({})
        
        total_slots = 0
        cursor = get_collection(ScheduleService.collection).find()
        async for doc in cursor:
            total_slots += len(doc.get("slots", []))
        
        return {
            "total_schedules": total_schedules,
            "total_classes": total_classes,
            "total_rooms": total_rooms,
            "total_slots": total_slots
        }


class SettingsService:
    collection = "settings"

    @staticmethod
    async def get() -> Optional[dict]:
        doc = await get_collection(SettingsService.collection).find_one({"type": "timetable"})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(data: dict) -> dict:
        result = await get_collection(SettingsService.collection).find_one_and_update(
            {"type": "timetable"},
            {"$set": {**data, "updated_at": datetime.utcnow()}},
            upsert=True,
            return_document=True
        )
        return serialize_doc(result)
