"""
Hostel Admin - Services Layer
=============================
Business logic for all Hostel Admin modules.
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
        total_rooms = await get_collection("rooms").count_documents({})
        occupied_rooms = await get_collection("rooms").count_documents({"status": "occupied"})
        vacant_rooms = total_rooms - occupied_rooms
        total_students = await get_collection("students").count_documents({})
        pending_complaints = await get_collection("complaints").count_documents({"status": "pending"})
        pending_fees = await get_collection("fee_records").count_documents({"status": "unpaid"})
        occupancy_rate = (occupied_rooms / total_rooms * 100) if total_rooms > 0 else 0
        
        return {
            "total_rooms": total_rooms,
            "occupied_rooms": occupied_rooms,
            "vacant_rooms": vacant_rooms,
            "total_students": total_students,
            "pending_complaints": pending_complaints,
            "pending_fees": pending_fees,
            "occupancy_rate": round(occupancy_rate, 1),
        }

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class RoomService:
    @staticmethod
    async def create_room(data: dict) -> str:
        col = get_collection("rooms")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_rooms(block_name: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("rooms")
        query = {}
        if block_name:
            query["block_name"] = block_name
        if status:
            query["status"] = status
        cursor = col.find(query).sort("room_number", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_room(room_id: str) -> Optional[Dict]:
        col = get_collection("rooms")
        doc = await col.find_one({"_id": ObjectId(room_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_room(room_id: str, data: dict) -> bool:
        col = get_collection("rooms")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(room_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_room(room_id: str) -> bool:
        col = get_collection("rooms")
        result = await col.delete_one({"_id": ObjectId(room_id)})
        return result.deleted_count > 0


class StudentService:
    @staticmethod
    async def create_student(data: dict) -> str:
        col = get_collection("students")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_students(room_id: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("students")
        query = {}
        if room_id:
            query["room_id"] = room_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("student_name", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_student(student_id: str) -> Optional[Dict]:
        col = get_collection("students")
        doc = await col.find_one({"_id": ObjectId(student_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_student(student_id: str, data: dict) -> bool:
        col = get_collection("students")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(student_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_student(student_id: str) -> bool:
        col = get_collection("students")
        result = await col.delete_one({"_id": ObjectId(student_id)})
        return result.deleted_count > 0


class FeeRecordService:
    @staticmethod
    async def create_fee_record(data: dict) -> str:
        col = get_collection("fee_records")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_fee_records(student_id: Optional[str] = None, status: Optional[str] = None, academic_year: Optional[str] = None) -> List[Dict]:
        col = get_collection("fee_records")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if status:
            query["status"] = status
        if academic_year:
            query["academic_year"] = academic_year
        cursor = col.find(query).sort("due_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_fee_record(record_id: str) -> Optional[Dict]:
        col = get_collection("fee_records")
        doc = await col.find_one({"_id": ObjectId(record_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_fee_record(record_id: str, data: dict) -> bool:
        col = get_collection("fee_records")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(record_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def record_payment(record_id: str, paid_amount: float, payment_method: str, transaction_id: str) -> bool:
        col = get_collection("fee_records")
        result = await col.update_one(
            {"_id": ObjectId(record_id)},
            {"$set": {
                "paid_amount": paid_amount,
                "paid_date": datetime.utcnow(),
                "payment_method": payment_method,
                "transaction_id": transaction_id,
                "status": "paid",
                "updated_at": datetime.utcnow()
            }}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete_fee_record(record_id: str) -> bool:
        col = get_collection("fee_records")
        result = await col.delete_one({"_id": ObjectId(record_id)})
        return result.deleted_count > 0


class ComplaintService:
    @staticmethod
    async def create_complaint(data: dict) -> str:
        col = get_collection("complaints")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_complaints(student_id: Optional[str] = None, status: Optional[str] = None, complaint_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("complaints")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if status:
            query["status"] = status
        if complaint_type:
            query["complaint_type"] = complaint_type
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

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
    async def resolve_complaint(complaint_id: str, resolution_notes: str) -> bool:
        col = get_collection("complaints")
        result = await col.update_one(
            {"_id": ObjectId(complaint_id)},
            {"$set": {"status": "resolved", "resolved_at": datetime.utcnow(), "resolution_notes": resolution_notes, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete_complaint(complaint_id: str) -> bool:
        col = get_collection("complaints")
        result = await col.delete_one({"_id": ObjectId(complaint_id)})
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
