"""
Faculty - Services Layer
=========================
Business logic for all Faculty modules.
Each service class handles CRUD + domain-specific operations.
"""

from bson import ObjectId
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection


def _serialize(doc: dict) -> dict:
    """Convert MongoDB document to JSON-serializable dict."""
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


class DashboardService:

    @staticmethod
    async def get_stats(faculty_id: Optional[str] = None) -> Dict[str, int]:
        query = {"faculty_id": faculty_id} if faculty_id else {}
        
        total_classes = await get_collection("classes").count_documents(query)
        total_students = await get_collection("classes").distinct("total_students", query) if total_classes > 0 else []
        if isinstance(total_students, list):
            total_students = sum(total_students)
        
        total_assignments = await get_collection("assignments").count_documents(query)
        pending_assignments = await get_collection("assignments").count_documents({**query, "status": "active"})
        
        upcoming_exams = await get_collection("exams").count_documents({
            **query,
            "status": "draft",
            "exam_date": {"$gte": datetime.utcnow()}
        })
        
        attendance_records = await get_collection("attendance").count_documents({
            "faculty_id": faculty_id,
            "status": "present"
        })
        total_attendance = await get_collection("attendance").count_documents({"faculty_id": faculty_id})
        average_attendance = (attendance_records / total_attendance * 100) if total_attendance > 0 else 0.0
        
        return {
            "total_classes": total_classes,
            "total_students": total_students,
            "total_assignments": total_assignments,
            "pending_assignments": pending_assignments,
            "upcoming_exams": upcoming_exams,
            "average_attendance": round(average_attendance, 1)
        }

    @staticmethod
    async def get_recent_activity(faculty_id: Optional[str] = None, limit: int = 10) -> List[Dict]:
        query = {"faculty_id": faculty_id} if faculty_id else {}
        col = get_collection("activity_log")
        cursor = col.find(query).sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def log_activity(action: str, actor: str, module: str, description: str, faculty_id: Optional[str] = None):
        col = get_collection("activity_log")
        doc = {
            "action": action,
            "actor": actor,
            "module": module,
            "description": description,
            "timestamp": datetime.utcnow(),
        }
        if faculty_id:
            doc["faculty_id"] = faculty_id
        await col.insert_one(doc)


class ProfileService:

    @staticmethod
    async def create_profile(data: dict) -> str:
        col = get_collection("profiles")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_profile(faculty_id: str) -> Optional[Dict]:
        col = get_collection("profiles")
        doc = await col.find_one({"faculty_id": faculty_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_profile(faculty_id: str, data: dict) -> bool:
        col = get_collection("profiles")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"faculty_id": faculty_id}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def get_profile_by_id(profile_id: str) -> Optional[Dict]:
        col = get_collection("profiles")
        doc = await col.find_one({"_id": ObjectId(profile_id)})
        return _serialize(doc) if doc else None


class ClassesService:

    @staticmethod
    async def create_class(data: dict) -> str:
        col = get_collection("classes")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_classes(faculty_id: Optional[str] = None, semester_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("classes")
        query = {}
        if faculty_id:
            query["faculty_id"] = faculty_id
        if semester_id:
            query["semester_id"] = semester_id
        cursor = col.find(query).sort("schedule_day", 1, "start_time", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_class(class_id: str) -> Optional[Dict]:
        col = get_collection("classes")
        doc = await col.find_one({"_id": ObjectId(class_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_class(class_id: str, data: dict) -> bool:
        col = get_collection("classes")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(class_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_class(class_id: str) -> bool:
        col = get_collection("classes")
        result = await col.delete_one({"_id": ObjectId(class_id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_class_students(class_id: str) -> List[Dict]:
        col = get_collection("students")
        class_doc = await get_collection("classes").find_one({"_id": ObjectId(class_id)})
        if not class_doc:
            return []
        query = {
            "course_id": class_doc.get("course_id"),
            "semester": class_doc.get("semester_name"),
            "section": class_doc.get("section")
        }
        cursor = col.find(query).sort("roll_number", 1)
        return _serialize_list(await cursor.to_list(length=200))


class AttendanceService:

    @staticmethod
    async def mark_attendance(class_id: str, date: datetime, records: List[dict], faculty_id: Optional[str] = None) -> str:
        col = get_collection("attendance")
        class_doc = await get_collection("classes").find_one({"_id": ObjectId(class_id)})
        
        documents = []
        for record in records:
            doc = {
                "class_id": class_id,
                "subject_id": class_doc.get("subject_id") if class_doc else None,
                "subject_name": class_doc.get("subject_name") if class_doc else None,
                "student_id": record["student_id"],
                "student_name": record.get("student_name"),
                "roll_number": record.get("roll_number"),
                "date": date,
                "status": record["status"],
                "remarks": record.get("remarks"),
                "faculty_id": faculty_id,
            }
            if faculty_id:
                doc["faculty_id"] = faculty_id
            documents.append(doc)
        
        await col.insert_many(documents)
        
        await get_collection("classes").update_one(
            {"_id": ObjectId(class_id)},
            {"$set": {"last_attendance_date": date, "updated_at": datetime.utcnow()}}
        )
        
        return class_id

    @staticmethod
    async def get_attendance_records(class_id: str, date: Optional[datetime] = None) -> List[Dict]:
        col = get_collection("attendance")
        query = {"class_id": class_id}
        if date:
            query["date"] = date
        cursor = col.find(query).sort("roll_number", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_attendance_summary(class_id: str) -> List[Dict]:
        col = get_collection("attendance")
        pipeline = [
            {"$match": {"class_id": class_id}},
            {"$group": {
                "_id": "$student_id",
                "student_name": {"$first": "$student_name"},
                "roll_number": {"$first": "$roll_number"},
                "total_classes": {"$sum": 1},
                "classes_attended": {"$sum": {"$cond": [{"$eq": ["$status", "present"]}, 1, 0]}},
                "classes_absent": {"$sum": {"$cond": [{"$eq": ["$status", "absent"]}, 1, 0]}},
            }},
            {"$addFields": {
                "percentage": {"$multiply": [{"$divide": ["$classes_attended", "$total_classes"]}, 100]}
            }},
            {"$sort": {"roll_number": 1}}
        ]
        cursor = col.aggregate(pipeline)
        results = []
        async for doc in cursor:
            doc["percentage"] = round(doc["percentage"], 1)
            results.append(_serialize(doc))
        return results

    @staticmethod
    async def get_attendance_report(class_id: str, start_date: datetime, end_date: datetime) -> Dict:
        col = get_collection("attendance")
        class_doc = await get_collection("classes").find_one({"_id": ObjectId(class_id)})
        
        query = {
            "class_id": class_id,
            "date": {"$gte": start_date, "$lte": end_date}
        }
        
        total_sessions = await col.count_documents(query)
        
        present_count = await col.count_documents({**query, "status": "present"})
        average_attendance = (present_count / total_sessions * 100) if total_sessions > 0 else 0.0
        
        student_summaries = await AttendanceService.get_attendance_summary(class_id)
        
        return {
            "class_id": class_id,
            "subject_name": class_doc.get("subject_name") if class_doc else None,
            "date_range_start": start_date,
            "date_range_end": end_date,
            "total_sessions": total_sessions,
            "average_attendance": round(average_attendance, 1),
            "student_summaries": student_summaries
        }

    @staticmethod
    async def update_attendance_record(record_id: str, data: dict) -> bool:
        col = get_collection("attendance")
        result = await col.update_one({"_id": ObjectId(record_id)}, {"$set": data})
        return result.modified_count > 0


class AssignmentsService:

    @staticmethod
    async def create_assignment(data: dict) -> str:
        col = get_collection("assignments")
        data["total_submissions"] = 0
        data["evaluated_count"] = 0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_assignments(faculty_id: Optional[str] = None, class_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("assignments")
        query = {}
        if faculty_id:
            query["faculty_id"] = faculty_id
        if class_id:
            query["class_id"] = class_id
        cursor = col.find(query).sort("due_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_assignment(assignment_id: str) -> Optional[Dict]:
        col = get_collection("assignments")
        doc = await col.find_one({"_id": ObjectId(assignment_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_assignment(assignment_id: str, data: dict) -> bool:
        col = get_collection("assignments")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(assignment_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_assignment(assignment_id: str) -> bool:
        col = get_collection("assignments")
        result = await col.delete_one({"_id": ObjectId(assignment_id)})
        return result.deleted_count > 0

    @staticmethod
    async def submit_evaluation(assignment_id: str, data: dict) -> str:
        col = get_collection("assignment_submissions")
        data["evaluated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        
        await get_collection("assignments").update_one(
            {"_id": ObjectId(assignment_id)},
            {"$inc": {"evaluated_count": 1}}
        )
        return str(result.inserted_id)

    @staticmethod
    async def get_submissions(assignment_id: str) -> List[Dict]:
        col = get_collection("assignment_submissions")
        cursor = col.find({"assignment_id": assignment_id}).sort("submission_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_submission(assignment_id: str, student_id: str) -> Optional[Dict]:
        col = get_collection("assignment_submissions")
        doc = await col.find_one({"assignment_id": assignment_id, "student_id": student_id})
        return _serialize(doc) if doc else None


class ExamsService:

    @staticmethod
    async def create_exam(data: dict) -> str:
        col = get_collection("exams")
        data["total_students"] = 0
        data["evaluated_count"] = 0
        data["average_score"] = 0.0
        data["highest_score"] = 0.0
        data["lowest_score"] = 0.0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_exams(faculty_id: Optional[str] = None, class_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("exams")
        query = {}
        if faculty_id:
            query["faculty_id"] = faculty_id
        if class_id:
            query["class_id"] = class_id
        cursor = col.find(query).sort("exam_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_exam(exam_id: str) -> Optional[Dict]:
        col = get_collection("exams")
        doc = await col.find_one({"_id": ObjectId(exam_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_exam(exam_id: str, data: dict) -> bool:
        col = get_collection("exams")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(exam_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_exam(exam_id: str) -> bool:
        col = get_collection("exams")
        result = await col.delete_one({"_id": ObjectId(exam_id)})
        return result.deleted_count > 0

    @staticmethod
    async def submit_results(exam_id: str, results: List[dict]) -> bool:
        col = get_collection("exam_results")
        documents = []
        for result in results:
            result["exam_id"] = exam_id
            result["evaluated_at"] = datetime.utcnow()
            documents.append(result)
        
        if documents:
            await col.insert_many(documents)
            
            exam_doc = await get_collection("exams").find_one({"_id": ObjectId(exam_id)})
            if exam_doc:
                all_results = await col.find({"exam_id": exam_id}).to_list(length=1000)
                if all_results:
                    scores = [r["marks_obtained"] for r in all_results if not r.get("is_absent")]
                    if scores:
                        avg_score = sum(scores) / len(scores)
                        await get_collection("exams").update_one(
                            {"_id": ObjectId(exam_id)},
                            {"$set": {
                                "average_score": round(avg_score, 2),
                                "highest_score": max(scores),
                                "lowest_score": min(scores),
                                "evaluated_count": len(all_results)
                            }}
                        )
            return True
        return False

    @staticmethod
    async def get_results(exam_id: str) -> List[Dict]:
        col = get_collection("exam_results")
        cursor = col.find({"exam_id": exam_id}).sort("roll_number", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_result(exam_id: str, student_id: str) -> Optional[Dict]:
        col = get_collection("exam_results")
        doc = await col.find_one({"exam_id": exam_id, "student_id": student_id})
        return _serialize(doc) if doc else None


class ReportsService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(faculty_id: Optional[str] = None, report_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("reports")
        query = {}
        if faculty_id:
            query["generated_by"] = faculty_id
        if report_type:
            query["report_type"] = report_type
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

    @staticmethod
    async def generate_performance_report(faculty_id: str, class_id: str) -> Dict:
        class_doc = await get_collection("classes").find_one({"_id": ObjectId(class_id)})
        if not class_doc:
            return {"error": "Class not found"}
        
        assignments = await get_collection("assignment_submissions").find({
            "assignment_id": {"$in": [a["_id"] for a in await get_collection("assignments").find({"class_id": class_id}).to_list(length=100)]}
        }).to_list(length=1000)
        
        exams = await get_collection("exam_results").find({
            "exam_id": {"$in": [e["_id"] for e in await get_collection("exams").find({"class_id": class_id}).to_list(length=100)]}
        }).to_list(length=1000)
        
        return {
            "class_id": class_id,
            "subject_name": class_doc.get("subject_name"),
            "total_assignments": len(assignments),
            "total_exam_results": len(exams),
            "average_assignment_score": sum(a.get("marks_obtained", 0) for a in assignments) / len(assignments) if assignments else 0,
            "average_exam_score": sum(e.get("marks_obtained", 0) for e in exams) / len(exams) if exams else 0,
        }


class SettingsService:

    @staticmethod
    async def get_settings(faculty_id: Optional[str] = None) -> Optional[Dict]:
        col = get_collection("settings")
        query = {"faculty_id": faculty_id} if faculty_id else {}
        doc = await col.find_one(query)
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict, faculty_id: Optional[str] = None) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        if faculty_id:
            data["faculty_id"] = faculty_id
        
        existing = await col.find_one({"faculty_id": faculty_id} if faculty_id else {})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)
