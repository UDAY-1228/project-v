"""
Course Coordinator - Services Layer
===================================
Business logic for all Course Coordinator modules.
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
            "total_courses": await get_collection("course_plans").count_documents({}),
            "total_subjects": await get_collection("subjects").count_documents({}),
            "total_faculty": await get_collection("faculty").count_documents({}),
            "active_plans": await get_collection("course_plans").count_documents({"status": "active"}),
            "pending_allocations": await get_collection("allocations").count_documents({"status": "pending"}),
            "upcoming_sessions": await get_collection("sessions").count_documents({"status": "scheduled"}),
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


class CoursePlanningService:

    @staticmethod
    async def create_course_plan(data: dict) -> str:
        col = get_collection("course_plans")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_course_plans(
        academic_year: Optional[str] = None,
        semester: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("course_plans")
        query = {}
        if academic_year:
            query["academic_year"] = academic_year
        if semester:
            query["semester"] = semester
        if status:
            query["status"] = status
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_course_plan(plan_id: str) -> Optional[Dict]:
        col = get_collection("course_plans")
        doc = await col.find_one({"_id": ObjectId(plan_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_course_plan(plan_id: str, data: dict) -> bool:
        col = get_collection("course_plans")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(plan_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_course_plan(plan_id: str) -> bool:
        col = get_collection("course_plans")
        result = await col.delete_one({"_id": ObjectId(plan_id)})
        return result.deleted_count > 0


class SessionService:

    @staticmethod
    async def create_session(data: dict) -> str:
        col = get_collection("sessions")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_sessions(
        plan_id: Optional[str] = None,
        faculty_id: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("sessions")
        query = {}
        if plan_id:
            query["plan_id"] = plan_id
        if faculty_id:
            query["faculty_id"] = faculty_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("date", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_session(session_id: str) -> Optional[Dict]:
        col = get_collection("sessions")
        doc = await col.find_one({"_id": ObjectId(session_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_session(session_id: str, data: dict) -> bool:
        col = get_collection("sessions")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(session_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_session(session_id: str) -> bool:
        col = get_collection("sessions")
        result = await col.delete_one({"_id": ObjectId(session_id)})
        return result.deleted_count > 0


class SubjectService:

    @staticmethod
    async def create_subject(data: dict) -> str:
        col = get_collection("subjects")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_subjects(
        course_id: Optional[str] = None,
        semester: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("subjects")
        query = {}
        if course_id:
            query["course_id"] = course_id
        if semester:
            query["semester"] = semester
        if status:
            query["status"] = status
        cursor = col.find(query).sort("subject_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_subject(subject_id: str) -> Optional[Dict]:
        col = get_collection("subjects")
        doc = await col.find_one({"_id": ObjectId(subject_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_subject(subject_id: str, data: dict) -> bool:
        col = get_collection("subjects")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(subject_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_subject(subject_id: str) -> bool:
        col = get_collection("subjects")
        result = await col.delete_one({"_id": ObjectId(subject_id)})
        return result.deleted_count > 0


class FacultyService:

    @staticmethod
    async def create_faculty(data: dict) -> str:
        col = get_collection("faculty")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_faculty(department: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("faculty")
        query = {}
        if department:
            query["department"] = department
        if status:
            query["status"] = status
        cursor = col.find(query).sort("faculty_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_faculty(faculty_id: str) -> Optional[Dict]:
        col = get_collection("faculty")
        doc = await col.find_one({"_id": ObjectId(faculty_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_faculty(faculty_id: str, data: dict) -> bool:
        col = get_collection("faculty")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(faculty_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_faculty(faculty_id: str) -> bool:
        col = get_collection("faculty")
        result = await col.delete_one({"_id": ObjectId(faculty_id)})
        return result.deleted_count > 0


class AllocationService:

    @staticmethod
    async def create_allocation(data: dict) -> str:
        col = get_collection("allocations")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_allocations(
        faculty_id: Optional[str] = None,
        subject_id: Optional[str] = None,
        academic_year: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("allocations")
        query = {}
        if faculty_id:
            query["faculty_id"] = faculty_id
        if subject_id:
            query["subject_id"] = subject_id
        if academic_year:
            query["academic_year"] = academic_year
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_allocation(allocation_id: str) -> Optional[Dict]:
        col = get_collection("allocations")
        doc = await col.find_one({"_id": ObjectId(allocation_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_allocation(allocation_id: str, data: dict) -> bool:
        col = get_collection("allocations")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(allocation_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_allocation(allocation_id: str) -> bool:
        col = get_collection("allocations")
        result = await col.delete_one({"_id": ObjectId(allocation_id)})
        return result.deleted_count > 0


class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("coordinator_reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(report_type: Optional[str] = None, academic_year: Optional[str] = None) -> List[Dict]:
        col = get_collection("coordinator_reports")
        query = {}
        if report_type:
            query["report_type"] = report_type
        if academic_year:
            query["academic_year"] = academic_year
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("coordinator_reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("coordinator_reports")
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
