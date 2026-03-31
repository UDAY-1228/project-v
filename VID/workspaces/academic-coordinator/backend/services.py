"""
Academic Coordinator - Services Layer
======================================
Business logic for all Academic Coordinator modules.
Each service class handles CRUD + domain-specific operations.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection


# ── Helper ──────────────────────────────────────────────────────────────────────

def _serialize(doc: dict) -> dict:
    """Convert MongoDB document to JSON-serializable dict."""
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


# ── Dashboard Service ───────────────────────────────────────────────────────────

class DashboardService:

    @staticmethod
    async def get_stats() -> Dict[str, int]:
        stats = {
            "total_courses": await get_collection("courses").count_documents({}),
            "total_subjects": await get_collection("subjects").count_documents({}),
            "total_assessments": await get_collection("assessments").count_documents({}),
            "active_timetables": await get_collection("timetables").count_documents({"status": "active"}),
            "pending_reports": await get_collection("reports").count_documents({"status": "pending"}),
            "unread_notices": await get_collection("notices").count_documents({"status": "active"}),
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


# ── Academic Management Service ─────────────────────────────────────────────────

class AcademicManagementService:

    # Academic Years
    @staticmethod
    async def create_academic_year(data: dict) -> str:
        col = get_collection("academic_years")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_academic_years() -> List[Dict]:
        col = get_collection("academic_years")
        cursor = col.find().sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_academic_year(year_id: str) -> Optional[Dict]:
        col = get_collection("academic_years")
        doc = await col.find_one({"_id": ObjectId(year_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_academic_year(year_id: str, data: dict) -> bool:
        col = get_collection("academic_years")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(year_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_academic_year(year_id: str) -> bool:
        col = get_collection("academic_years")
        result = await col.delete_one({"_id": ObjectId(year_id)})
        return result.deleted_count > 0

    # Semesters
    @staticmethod
    async def create_semester(data: dict) -> str:
        col = get_collection("semesters")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_semesters(academic_year_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("semesters")
        query = {"academic_year_id": academic_year_id} if academic_year_id else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def update_semester(semester_id: str, data: dict) -> bool:
        col = get_collection("semesters")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(semester_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_semester(semester_id: str) -> bool:
        col = get_collection("semesters")
        result = await col.delete_one({"_id": ObjectId(semester_id)})
        return result.deleted_count > 0

    # Departments
    @staticmethod
    async def create_department(data: dict) -> str:
        col = get_collection("departments")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_departments() -> List[Dict]:
        col = get_collection("departments")
        cursor = col.find().sort("department_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def update_department(dept_id: str, data: dict) -> bool:
        col = get_collection("departments")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(dept_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_department(dept_id: str) -> bool:
        col = get_collection("departments")
        result = await col.delete_one({"_id": ObjectId(dept_id)})
        return result.deleted_count > 0


# ── Course Service ──────────────────────────────────────────────────────────────

class CourseService:

    @staticmethod
    async def create_course(data: dict) -> str:
        col = get_collection("courses")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_courses(department_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("courses")
        query = {"department_id": department_id} if department_id else {}
        cursor = col.find(query).sort("course_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_course(course_id: str) -> Optional[Dict]:
        col = get_collection("courses")
        doc = await col.find_one({"_id": ObjectId(course_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_course(course_id: str, data: dict) -> bool:
        col = get_collection("courses")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(course_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_course(course_id: str) -> bool:
        col = get_collection("courses")
        result = await col.delete_one({"_id": ObjectId(course_id)})
        return result.deleted_count > 0


# ── Subject Service ─────────────────────────────────────────────────────────────

class SubjectService:

    @staticmethod
    async def create_subject(data: dict) -> str:
        col = get_collection("subjects")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_subjects(course_id: Optional[str] = None, semester_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("subjects")
        query = {}
        if course_id:
            query["course_id"] = course_id
        if semester_id:
            query["semester_id"] = semester_id
        cursor = col.find(query).sort("subject_name", 1)
        return _serialize_list(await cursor.to_list(length=500))

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


# ── Timetable Service ───────────────────────────────────────────────────────────

class TimetableService:

    @staticmethod
    async def create_timetable(data: dict) -> str:
        col = get_collection("timetables")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_timetables(course_id: Optional[str] = None, semester_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("timetables")
        query = {}
        if course_id:
            query["course_id"] = course_id
        if semester_id:
            query["semester_id"] = semester_id
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_timetable(timetable_id: str) -> Optional[Dict]:
        col = get_collection("timetables")
        doc = await col.find_one({"_id": ObjectId(timetable_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_timetable(timetable_id: str, data: dict) -> bool:
        col = get_collection("timetables")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(timetable_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_timetable(timetable_id: str) -> bool:
        col = get_collection("timetables")
        result = await col.delete_one({"_id": ObjectId(timetable_id)})
        return result.deleted_count > 0


# ── Assessment Service ──────────────────────────────────────────────────────────

class AssessmentService:

    @staticmethod
    async def create_assessment(data: dict) -> str:
        col = get_collection("assessments")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_assessments(subject_id: Optional[str] = None, assessment_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("assessments")
        query = {}
        if subject_id:
            query["subject_id"] = subject_id
        if assessment_type:
            query["assessment_type"] = assessment_type
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_assessment(assessment_id: str) -> Optional[Dict]:
        col = get_collection("assessments")
        doc = await col.find_one({"_id": ObjectId(assessment_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_assessment(assessment_id: str, data: dict) -> bool:
        col = get_collection("assessments")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(assessment_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_assessment(assessment_id: str) -> bool:
        col = get_collection("assessments")
        result = await col.delete_one({"_id": ObjectId(assessment_id)})
        return result.deleted_count > 0

    # Assessment Results
    @staticmethod
    async def submit_result(data: dict) -> str:
        col = get_collection("assessment_results")
        data["submitted_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_results(assessment_id: str) -> List[Dict]:
        col = get_collection("assessment_results")
        cursor = col.find({"assessment_id": assessment_id})
        return _serialize_list(await cursor.to_list(length=500))


# ── Report Service ──────────────────────────────────────────────────────────────

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


# ── Notice Board Service ────────────────────────────────────────────────────────

class NoticeBoardService:

    @staticmethod
    async def create_notice(data: dict) -> str:
        col = get_collection("notices")
        data["views_count"] = 0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_notices(category: Optional[str] = None, pinned_first: bool = True) -> List[Dict]:
        col = get_collection("notices")
        query = {}
        if category:
            query["category"] = category
        sort_key = [("is_pinned", -1), ("created_at", -1)] if pinned_first else [("created_at", -1)]
        cursor = col.find(query).sort(sort_key)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_notice(notice_id: str) -> Optional[Dict]:
        col = get_collection("notices")
        # Increment view count
        await col.update_one({"_id": ObjectId(notice_id)}, {"$inc": {"views_count": 1}})
        doc = await col.find_one({"_id": ObjectId(notice_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_notice(notice_id: str, data: dict) -> bool:
        col = get_collection("notices")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(notice_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_notice(notice_id: str) -> bool:
        col = get_collection("notices")
        result = await col.delete_one({"_id": ObjectId(notice_id)})
        return result.deleted_count > 0

    @staticmethod
    async def toggle_pin(notice_id: str) -> bool:
        col = get_collection("notices")
        doc = await col.find_one({"_id": ObjectId(notice_id)})
        if doc:
            new_pin = not doc.get("is_pinned", False)
            await col.update_one({"_id": ObjectId(notice_id)}, {"$set": {"is_pinned": new_pin}})
            return True
        return False


# ── Settings Service ────────────────────────────────────────────────────────────

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
