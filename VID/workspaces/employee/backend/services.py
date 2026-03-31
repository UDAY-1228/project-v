"""
Employee - Services Layer
==========================
Business logic for all Employee modules.
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
            "total_tasks": await get_collection("tasks").count_documents({}),
            "completed_tasks": await get_collection("tasks").count_documents({"status": "completed"}),
            "pending_leaves": await get_collection("leave_requests").count_documents({"status": "pending"}),
            "attendance_rate": 95.5,
            "upcoming_events": await get_collection("events").count_documents({"status": "upcoming"}),
            "total_hours_worked": 160.0,
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


class AttendanceService:
    @staticmethod
    async def check_in(employee_id: str) -> str:
        col = get_collection("attendance")
        now = datetime.utcnow()
        existing = await col.find_one({"employee_id": employee_id, "date": now.date()})
        if existing:
            raise ValueError("Already checked in today")
        data = {"employee_id": employee_id, "date": now, "check_in": now.strftime("%H:%M"), "status": "present"}
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def check_out(employee_id: str) -> bool:
        col = get_collection("attendance")
        now = datetime.utcnow()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        record = await col.find_one({"employee_id": employee_id, "date": {"$gte": today_start}})
        if not record:
            return False
        check_in_time = record.get("check_in")
        if check_in_time:
            from datetime import datetime as dt
            in_hour, in_min = map(int, check_in_time.split(":"))
            check_in_dt = now.replace(hour=in_hour, minute=in_min)
            hours = (now - check_in_dt).total_seconds() / 3600
            await col.update_one({"_id": record["_id"]}, {"$set": {"check_out": now.strftime("%H:%M"), "hours_worked": round(hours, 2)}})
            return True
        return False

    @staticmethod
    async def get_attendance_records(employee_id: str, month: Optional[int] = None) -> List[Dict]:
        col = get_collection("attendance")
        query = {"employee_id": employee_id}
        if month:
            from datetime import datetime as dt
            year = datetime.utcnow().year
            start = dt(year, month, 1)
            if month == 12:
                end = dt(year + 1, 1, 1)
            else:
                end = dt(year, month + 1, 1)
            query["date"] = {"$gte": start, "$lt": end}
        cursor = col.find(query).sort("date", -1)
        return _serialize_list(await cursor.to_list(length=100))


class TaskService:
    @staticmethod
    async def create_task(data: dict) -> str:
        col = get_collection("tasks")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_tasks(employee_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("tasks")
        query = {"assigned_to": employee_id} if employee_id else {}
        cursor = col.find(query).sort("due_date", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_task(task_id: str) -> Optional[Dict]:
        col = get_collection("tasks")
        doc = await col.find_one({"_id": ObjectId(task_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_task(task_id: str, data: dict) -> bool:
        col = get_collection("tasks")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(task_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_task(task_id: str) -> bool:
        col = get_collection("tasks")
        result = await col.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count > 0


class LeaveRequestService:
    @staticmethod
    async def create_leave_request(data: dict) -> str:
        col = get_collection("leave_requests")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_leave_requests(employee_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("leave_requests")
        query = {"employee_id": employee_id} if employee_id else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_leave_request(request_id: str) -> Optional[Dict]:
        col = get_collection("leave_requests")
        doc = await col.find_one({"_id": ObjectId(request_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def approve_leave_request(request_id: str, approver_id: str) -> bool:
        col = get_collection("leave_requests")
        result = await col.update_one(
            {"_id": ObjectId(request_id)},
            {"$set": {"status": "approved", "approved_by": approver_id, "approved_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def reject_leave_request(request_id: str) -> bool:
        col = get_collection("leave_requests")
        result = await col.update_one({"_id": ObjectId(request_id)}, {"$set": {"status": "rejected"}})
        return result.modified_count > 0

    @staticmethod
    async def get_leave_balance(employee_id: str) -> Dict:
        balance = {
            "employee_id": employee_id,
            "casual_leave": 12, "sick_leave": 10, "earned_leave": 15, "unpaid_leave": 0
        }
        used = await get_collection("leave_requests").aggregate([
            {"$match": {"employee_id": employee_id, "status": "approved"}},
            {"$group": {"_id": "$leave_type", "count": {"$sum": 1}}}
        ]).to_list(length=10)
        for item in used:
            if item["_id"] == "casual": balance["casual_leave"] -= item["count"]
            elif item["_id"] == "sick": balance["sick_leave"] -= item["count"]
            elif item["_id"] == "earned": balance["earned_leave"] -= item["count"]
        return balance


class ProfileService:
    @staticmethod
    async def get_profile(employee_id: str) -> Optional[Dict]:
        col = get_collection("profiles")
        doc = await col.find_one({"employee_id": employee_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def create_profile(data: dict) -> str:
        col = get_collection("profiles")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def update_profile(employee_id: str, data: dict) -> bool:
        col = get_collection("profiles")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"employee_id": employee_id}, {"$set": data})
        return result.modified_count > 0


class SettingsService:
    @staticmethod
    async def get_settings(employee_id: str) -> Optional[Dict]:
        col = get_collection("settings")
        doc = await col.find_one({"employee_id": employee_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict, employee_id: str) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        existing = await col.find_one({"employee_id": employee_id})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["employee_id"] = employee_id
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)
