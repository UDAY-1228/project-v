"""
Student Workspace - Services
===========================
Business logic layer for Student workspace.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from bson import ObjectId
from .mongodb_connection import get_collection


def get_profile_collection():
    return get_collection("profiles")


def get_courses_collection():
    return get_collection("courses")


def get_enrollments_collection():
    return get_collection("enrollments")


def get_attendance_collection():
    return get_collection("attendance")


def get_exams_collection():
    return get_collection("exams")


def get_results_collection():
    return get_collection("results")


def get_fees_collection():
    return get_collection("fees")


def get_notifications_collection():
    return get_collection("notifications")


def get_settings_collection():
    return get_collection("settings")


class ProfileService:
    @staticmethod
    async def get_profile(student_id: str) -> Optional[Dict]:
        collection = get_profile_collection()
        profile = await collection.find_one({"student_id": student_id})
        if profile:
            profile["_id"] = str(profile["_id"])
        return profile

    @staticmethod
    async def update_profile(student_id: str, update_data: Dict) -> bool:
        collection = get_profile_collection()
        update_data["updated_at"] = datetime.utcnow()
        result = await collection.update_one(
            {"student_id": student_id},
            {"$set": update_data}
        )
        return result.modified_count > 0

    @staticmethod
    async def create_profile(profile_data: Dict) -> str:
        collection = get_profile_collection()
        profile_data["created_at"] = datetime.utcnow()
        profile_data["updated_at"] = datetime.utcnow()
        result = await collection.insert_one(profile_data)
        return str(result.inserted_id)


class CourseService:
    @staticmethod
    async def get_all_courses(student_id: str, semester: Optional[int] = None) -> List[Dict]:
        collection = get_courses_collection()
        query = {"is_active": True}
        if semester:
            query["semester"] = semester
        courses = []
        async for course in collection.find(query):
            course["_id"] = str(course["_id"])
            courses.append(course)
        return courses

    @staticmethod
    async def get_course(course_id: str) -> Optional[Dict]:
        collection = get_courses_collection()
        course = await collection.find_one({"course_id": course_id})
        if course:
            course["_id"] = str(course["_id"])
        return course

    @staticmethod
    async def get_enrolled_courses(student_id: str) -> List[Dict]:
        enrollments = get_enrollments_collection()
        courses = []
        async for enrollment in enrollments.find({"student_id": student_id, "status": "active"}):
            enrollment["_id"] = str(enrollment["_id"])
            courses.append(enrollment)
        return courses


class AttendanceService:
    @staticmethod
    async def get_attendance(student_id: str, course_id: Optional[str] = None, 
                            start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict]:
        collection = get_attendance_collection()
        query: Dict[str, Any] = {"student_id": student_id}
        if course_id:
            query["course_id"] = course_id
        if start_date and end_date:
            query["date"] = {"$gte": start_date, "$lte": end_date}
        elif start_date:
            query["date"] = {"$gte": start_date}
        elif end_date:
            query["date"] = {"$lte": end_date}
        
        attendance_records = []
        async for record in collection.find(query).sort("date", -1):
            record["_id"] = str(record["_id"])
            attendance_records.append(record)
        return attendance_records

    @staticmethod
    async def get_attendance_summary(student_id: str, course_id: Optional[str] = None) -> Dict:
        collection = get_attendance_collection()
        query: Dict[str, Any] = {"student_id": student_id}
        if course_id:
            query["course_id"] = course_id
        
        total = 0
        present = 0
        absent = 0
        late = 0
        excused = 0
        
        async for record in collection.find(query):
            total += 1
            status = record.get("status", "").lower()
            if status == "present":
                present += 1
            elif status == "absent":
                absent += 1
            elif status == "late":
                late += 1
            elif status == "excused":
                excused += 1
        
        percentage = (present / total * 100) if total > 0 else 0
        
        return {
            "total_classes": total,
            "present": present,
            "absent": absent,
            "late": late,
            "excused": excused,
            "percentage": round(percentage, 2)
        }


class ExamService:
    @staticmethod
    async def get_all_exams(student_id: str, status: Optional[str] = None) -> List[Dict]:
        collection = get_exams_collection()
        query: Dict[str, Any] = {}
        if status:
            query["status"] = status
        else:
            query["status"] = {"$in": ["scheduled", "postponed"]}
        
        exams = []
        async for exam in collection.find(query).sort("date", 1):
            exam["_id"] = str(exam["_id"])
            exams.append(exam)
        return exams

    @staticmethod
    async def get_exam(exam_id: str) -> Optional[Dict]:
        collection = get_exams_collection()
        exam = await collection.find_one({"exam_id": exam_id})
        if exam:
            exam["_id"] = str(exam["_id"])
        return exam

    @staticmethod
    async def get_upcoming_exams(student_id: str, limit: int = 5) -> List[Dict]:
        collection = get_exams_collection()
        today = datetime.now().strftime("%Y-%m-%d")
        exams = []
        async for exam in collection.find({
            "status": "scheduled",
            "date": {"$gte": today}
        }).sort("date", 1).limit(limit):
            exam["_id"] = str(exam["_id"])
            exams.append(exam)
        return exams

    @staticmethod
    async def register_for_exam(student_id: str, exam_id: str) -> bool:
        collection = get_enrollments_collection()
        existing = await collection.find_one({
            "student_id": student_id,
            "exam_id": exam_id
        })
        if existing:
            return False
        
        await collection.insert_one({
            "student_id": student_id,
            "exam_id": exam_id,
            "registered_at": datetime.utcnow().isoformat(),
            "status": "registered"
        })
        return True


class ResultService:
    @staticmethod
    async def get_results(student_id: str, course_id: Optional[str] = None) -> List[Dict]:
        collection = get_results_collection()
        query: Dict[str, Any] = {"student_id": student_id}
        if course_id:
            query["course_id"] = course_id
        
        results = []
        async for result in collection.find(query).sort("published_at", -1):
            result["_id"] = str(result["_id"])
            results.append(result)
        return results

    @staticmethod
    async def get_result(result_id: str) -> Optional[Dict]:
        collection = get_results_collection()
        result = await collection.find_one({"result_id": result_id})
        if result:
            result["_id"] = str(result["_id"])
        return result

    @staticmethod
    async def calculate_cgpa(student_id: str) -> Optional[float]:
        collection = get_results_collection()
        results = await collection.find({"student_id": student_id, "is_final": True}).to_list(length=None)
        
        if not results:
            return None
        
        total_points = 0.0
        total_credits = 0
        
        grade_points = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, 
                       "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0}
        
        enrollments = get_enrollments_collection()
        async for enrollment in enrollments.find({"student_id": student_id}):
            credits = enrollment.get("credits", 3)
            grade = None
            for result in results:
                if result.get("course_id") == enrollment.get("course_id"):
                    grade = result.get("grade")
                    break
            
            if grade and grade in grade_points:
                total_points += grade_points[grade] * credits
                total_credits += credits
        
        if total_credits == 0:
            return None
        
        return round(total_points / total_credits, 2)


class FeeService:
    @staticmethod
    async def get_fee_records(student_id: str, status: Optional[str] = None) -> List[Dict]:
        collection = get_fees_collection()
        query: Dict[str, Any] = {"student_id": student_id}
        if status:
            query["status"] = status
        
        fees = []
        async for fee in collection.find(query).sort("due_date", 1):
            fee["_id"] = str(fee["_id"])
            fees.append(fee)
        return fees

    @staticmethod
    async def get_fee_summary(student_id: str) -> Dict:
        collection = get_fees_collection()
        total_fees = 0.0
        total_paid = 0.0
        total_pending = 0.0
        overdue_amount = 0.0
        today = datetime.now().strftime("%Y-%m-%d")
        
        async for fee in collection.find({"student_id": student_id}):
            amount = fee.get("amount", 0)
            paid = fee.get("paid_amount", 0)
            status = fee.get("status", "")
            
            total_fees += amount
            total_paid += paid
            
            if status in ["pending", "partial", "overdue"]:
                total_pending += (amount - paid)
            
            if status == "overdue" or (status == "pending" and fee.get("due_date", "") < today):
                overdue_amount += (amount - paid)
        
        return {
            "total_fees": total_fees,
            "total_paid": total_paid,
            "total_pending": total_pending,
            "overdue_amount": overdue_amount
        }

    @staticmethod
    async def make_payment(fee_id: str, amount: float, payment_method: str) -> bool:
        collection = get_fees_collection()
        fee = await collection.find_one({"fee_id": fee_id})
        if not fee:
            return False
        
        new_paid_amount = fee.get("paid_amount", 0) + amount
        new_status = "paid" if new_paid_amount >= fee.get("amount", 0) else "partial"
        
        result = await collection.update_one(
            {"fee_id": fee_id},
            {"$set": {
                "paid_amount": new_paid_amount,
                "status": new_status,
                "paid_date": datetime.utcnow().isoformat(),
                "payment_method": payment_method,
                "transaction_id": f"TXN_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                "updated_at": datetime.utcnow()
            }}
        )
        return result.modified_count > 0


class NotificationService:
    @staticmethod
    async def get_notifications(student_id: str, unread_only: bool = False, 
                               limit: int = 50) -> List[Dict]:
        collection = get_notifications_collection()
        query: Dict[str, Any] = {
            "$or": [
                {"student_id": student_id},
                {"student_id": None}
            ]
        }
        if unread_only:
            query["is_read"] = False
        
        notifications = []
        async for notification in collection.find(query).sort("sent_at", -1).limit(limit):
            notification["_id"] = str(notification["_id"])
            notifications.append(notification)
        return notifications

    @staticmethod
    async def mark_as_read(notification_id: str) -> bool:
        collection = get_notifications_collection()
        result = await collection.update_one(
            {"notification_id": notification_id},
            {"$set": {"is_read": True, "read_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def mark_all_as_read(student_id: str) -> int:
        collection = get_notifications_collection()
        result = await collection.update_many(
            {"student_id": student_id, "is_read": False},
            {"$set": {"is_read": True, "read_at": datetime.utcnow()}}
        )
        return result.modified_count

    @staticmethod
    async def get_unread_count(student_id: str) -> int:
        collection = get_notifications_collection()
        count = await collection.count_documents({
            "student_id": student_id,
            "is_read": False
        })
        return count


class SettingsService:
    @staticmethod
    async def get_settings(student_id: str) -> Optional[Dict]:
        collection = get_settings_collection()
        settings = await collection.find_one({"student_id": student_id})
        if settings:
            settings["_id"] = str(settings["_id"])
        return settings

    @staticmethod
    async def update_settings(student_id: str, update_data: Dict) -> bool:
        collection = get_settings_collection()
        update_data["updated_at"] = datetime.utcnow()
        
        existing = await collection.find_one({"student_id": student_id})
        if existing:
            result = await collection.update_one(
                {"student_id": student_id},
                {"$set": update_data}
            )
            return result.modified_count > 0
        else:
            update_data["student_id"] = student_id
            await collection.insert_one(update_data)
            return True

    @staticmethod
    async def create_default_settings(student_id: str) -> str:
        collection = get_settings_collection()
        settings = {
            "student_id": student_id,
            "email_notifications": True,
            "sms_notifications": True,
            "push_notifications": True,
            "attendance_alerts": True,
            "fee_reminders": True,
            "exam_reminders": True,
            "result_notifications": True,
            "language": "en",
            "timezone": "UTC",
            "theme": "light",
            "updated_at": datetime.utcnow()
        }
        result = await collection.insert_one(settings)
        return str(result.inserted_id)


class DashboardService:
    @staticmethod
    async def get_dashboard_data(student_id: str) -> Dict:
        profile = await ProfileService.get_profile(student_id)
        
        if not profile:
            return {
                "student_name": "Unknown",
                "student_id": student_id,
                "department": "N/A",
                "semester": 0,
                "current_cgpa": None,
                "attendance_percentage": 0.0,
                "total_notifications": 0,
                "unread_notifications": 0,
                "upcoming_exams": 0,
                "pending_fees": 0.0,
                "enrolled_courses": 0,
                "completed_courses": 0
            }
        
        enrolled_courses = await CourseService.get_enrolled_courses(student_id)
        attendance_summary = await AttendanceService.get_attendance_summary(student_id)
        upcoming_exams = await ExamService.get_upcoming_exams(student_id, limit=10)
        fee_summary = await FeeService.get_fee_summary(student_id)
        total_notifications = await NotificationService.get_notifications(student_id, limit=1000)
        unread_notifications = await NotificationService.get_unread_count(student_id)
        current_cgpa = await ResultService.calculate_cgpa(student_id)
        
        completed_courses = len([e for e in enrolled_courses if e.get("grade")])
        
        return {
            "student_name": f"{profile.get('first_name', '')} {profile.get('last_name', '')}",
            "student_id": student_id,
            "department": profile.get("department", "N/A"),
            "semester": profile.get("semester", 1),
            "current_cgpa": current_cgpa,
            "attendance_percentage": attendance_summary.get("percentage", 0.0),
            "total_notifications": len(total_notifications),
            "unread_notifications": unread_notifications,
            "upcoming_exams": len(upcoming_exams),
            "pending_fees": fee_summary.get("total_pending", 0.0),
            "enrolled_courses": len(enrolled_courses),
            "completed_courses": completed_courses
        }
