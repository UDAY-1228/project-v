"""
Examination - Service Methods
==============================
Service layer for the Examination workspace.
"""

from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .mongodb_connection import get_collection


def serialize_doc(doc: dict) -> dict:
    """Convert MongoDB document to JSON-serializable format."""
    if doc is None:
        return None
    doc["_id"] = str(doc["_id"])
    if "created_at" in doc:
        doc["created_at"] = doc["created_at"].isoformat()
    if "updated_at" in doc:
        doc["updated_at"] = doc["updated_at"].isoformat()
    if "date" in doc:
        doc["date"] = doc["date"].isoformat()
    return doc


class ExamService:
    collection = "exams"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        data["is_active"] = True
        result = await get_collection(ExamService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ExamService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(exam_id: str) -> Optional[dict]:
        doc = await get_collection(ExamService.collection).find_one({"_id": ObjectId(exam_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(exam_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ExamService.collection).find_one_and_update(
            {"_id": ObjectId(exam_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(exam_id: str) -> bool:
        result = await get_collection(ExamService.collection).delete_one({"_id": ObjectId(exam_id)})
        return result.deleted_count > 0


class ExamScheduleService:
    collection = "exam_schedules"

    @staticmethod
    async def create(data: dict) -> dict:
        if "date" in data and isinstance(data["date"], str):
            data["date"] = datetime.fromisoformat(data["date"].replace("Z", "+00:00"))
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ExamScheduleService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ExamScheduleService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_exam(exam_id: str) -> List[dict]:
        cursor = get_collection(ExamScheduleService.collection).find({"exam_id": exam_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(schedule_id: str, data: dict) -> Optional[dict]:
        if "date" in data and isinstance(data["date"], str):
            data["date"] = datetime.fromisoformat(data["date"].replace("Z", "+00:00"))
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ExamScheduleService.collection).find_one_and_update(
            {"_id": ObjectId(schedule_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(schedule_id: str) -> bool:
        result = await get_collection(ExamScheduleService.collection).delete_one({"_id": ObjectId(schedule_id)})
        return result.deleted_count > 0


class HallTicketService:
    collection = "hall_tickets"

    @staticmethod
    async def create(data: dict) -> dict:
        data["status"] = "issued"
        data["issued_at"] = datetime.utcnow()
        result = await get_collection(HallTicketService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(HallTicketService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_student(student_id: str) -> List[dict]:
        cursor = get_collection(HallTicketService.collection).find({"student_id": student_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(ticket_id: str, data: dict) -> Optional[dict]:
        result = await get_collection(HallTicketService.collection).find_one_and_update(
            {"_id": ObjectId(ticket_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None


class ResultService:
    collection = "results"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ResultService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ResultService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_student(student_id: str) -> List[dict]:
        cursor = get_collection(ResultService.collection).find({"student_id": student_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(result_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(ResultService.collection).find_one_and_update(
            {"_id": ObjectId(result_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None


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
        total_exams = await get_collection(ExamService.collection).count_documents({"is_active": True})
        now = datetime.utcnow()
        upcoming_schedules = await get_collection(ExamScheduleService.collection).count_documents({"date": {"$gte": now}})
        hall_tickets_issued = await get_collection(HallTicketService.collection).count_documents({})
        results_declared = await get_collection(ResultService.collection).count_documents({})
        
        return {
            "total_exams": total_exams,
            "upcoming_schedules": upcoming_schedules,
            "hall_tickets_issued": hall_tickets_issued,
            "results_declared": results_declared
        }


class SettingsService:
    collection = "settings"

    @staticmethod
    async def get() -> Optional[dict]:
        doc = await get_collection(SettingsService.collection).find_one({"type": "examination"})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(data: dict) -> dict:
        result = await get_collection(SettingsService.collection).find_one_and_update(
            {"type": "examination"},
            {"$set": {**data, "updated_at": datetime.utcnow()}},
            upsert=True,
            return_document=True
        )
        return serialize_doc(result)
