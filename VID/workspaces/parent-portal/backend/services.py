"""
Parent Portal - Services Layer
==============================
Business logic for all Parent Portal modules.
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
            "total_students": await get_collection("student_progress").count_documents({}),
            "average_attendance": 85.5,
            "pending_fees": await get_collection("fee_status").count_documents({"status": "unpaid"}),
            "upcoming_events": 0,
            "unread_notifications": await get_collection("notifications").count_documents({"is_read": False}),
            "recent_activities": await get_collection("activity_log").count_documents({}),
        }
        return stats

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class StudentProgressService:

    @staticmethod
    async def create_progress(data: dict) -> str:
        col = get_collection("student_progress")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_progress(student_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("student_progress")
        query = {"student_id": student_id} if student_id else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_progress(progress_id: str) -> Optional[Dict]:
        col = get_collection("student_progress")
        doc = await col.find_one({"_id": ObjectId(progress_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_progress(progress_id: str, data: dict) -> bool:
        col = get_collection("student_progress")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(progress_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def get_student_subjects(student_id: str) -> List[Dict]:
        col = get_collection("student_progress")
        cursor = col.find({"student_id": student_id})
        return _serialize_list(await cursor.to_list(length=100))


class AttendanceService:

    @staticmethod
    async def mark_attendance(data: dict) -> str:
        col = get_collection("attendance")
        data["created_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_attendance(student_id: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[Dict]:
        col = get_collection("attendance")
        query = {"student_id": student_id}
        if start_date:
            query["date"] = {"$gte": start_date}
        if end_date:
            if "date" in query:
                query["date"]["$lte"] = end_date
            else:
                query["date"] = {"$lte": end_date}
        cursor = col.find(query).sort("date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_attendance_summary(student_id: str) -> Optional[Dict]:
        col = get_collection("attendance")
        records = await col.find({"student_id": student_id}).to_list(length=1000)
        total = len(records)
        present = sum(1 for r in records if r.get("status") == "present")
        absent = sum(1 for r in records if r.get("status") == "absent")
        leave = sum(1 for r in records if r.get("status") == "leave")
        percentage = (present / total * 100) if total > 0 else 0
        return {
            "student_id": student_id,
            "total_days": total,
            "present_days": present,
            "absent_days": absent,
            "leave_days": leave,
            "attendance_percentage": round(percentage, 2),
        }


class FeeStatusService:

    @staticmethod
    async def create_fee(data: dict) -> str:
        col = get_collection("fee_status")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_fees(student_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("fee_status")
        query = {"student_id": student_id} if student_id else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_fee(fee_id: str) -> Optional[Dict]:
        col = get_collection("fee_status")
        doc = await col.find_one({"_id": ObjectId(fee_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_fee(fee_id: str, data: dict) -> bool:
        col = get_collection("fee_status")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(fee_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def make_payment(fee_id: str, payment_data: dict) -> bool:
        col = get_collection("fee_status")
        payment_data["payment_date"] = datetime.utcnow()
        await get_collection("fee_payments").insert_one({
            "fee_id": fee_id,
            **payment_data,
        })
        result = await col.update_one(
            {"_id": ObjectId(fee_id)},
            {
                "$set": {
                    "status": "paid",
                    "paid_date": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                },
                "$inc": {"paid_amount": payment_data.get("amount", 0)}
            }
        )
        return result.modified_count > 0

    @staticmethod
    async def get_payment_history(fee_id: str) -> List[Dict]:
        col = get_collection("fee_payments")
        cursor = col.find({"fee_id": fee_id}).sort("payment_date", -1)
        return _serialize_list(await cursor.to_list(length=100))


class NotificationService:

    @staticmethod
    async def create_notification(data: dict) -> str:
        col = get_collection("notifications")
        data["created_at"] = datetime.utcnow()
        data["is_read"] = False
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_notifications(recipient_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("notifications")
        query = {}
        if recipient_id:
            query["recipient_ids"] = recipient_id
        cursor = col.find(query).sort("created_at", -1).limit(50)
        return _serialize_list(await cursor.to_list(length=50))

    @staticmethod
    async def mark_as_read(notification_id: str) -> bool:
        col = get_collection("notifications")
        result = await col.update_one(
            {"_id": ObjectId(notification_id)},
            {"$set": {"is_read": True}}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete_notification(notification_id: str) -> bool:
        col = get_collection("notifications")
        result = await col.delete_one({"_id": ObjectId(notification_id)})
        return result.deleted_count > 0


class SettingsService:

    @staticmethod
    async def get_settings(parent_id: Optional[str] = None) -> Optional[Dict]:
        col = get_collection("settings")
        query = {"parent_id": parent_id} if parent_id else {}
        doc = await col.find_one(query)
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict, parent_id: Optional[str] = None) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        if parent_id:
            data["parent_id"] = parent_id
        existing = await col.find_one({"parent_id": parent_id} if parent_id else {})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            result = await col.insert_one(data)
            return str(result.inserted_id)
