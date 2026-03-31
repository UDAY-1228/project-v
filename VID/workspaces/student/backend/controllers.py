"""
Student Workspace - Controllers
===============================
Request handlers for Student workspace API endpoints.
"""

from typing import Optional, List
from fastapi import HTTPException, Depends, Query
from .services import (
    ProfileService, CourseService, AttendanceService, ExamService,
    ResultService, FeeService, NotificationService, SettingsService, DashboardService
)
from .schemas import (
    ProfileUpdateRequest, DashboardResponse, CourseResponse,
    AttendanceRecordResponse, AttendanceSummary, ExamResponse,
    ResultResponse, FeeRecordResponse, FeeSummary, NotificationResponse,
    SettingsUpdateRequest, SettingsResponse, ApiResponse
)


class ProfileController:
    @staticmethod
    async def get_profile(student_id: str):
        profile = await ProfileService.get_profile(student_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile

    @staticmethod
    async def update_profile(student_id: str, data: ProfileUpdateRequest):
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No data provided for update")
        
        success = await ProfileService.update_profile(student_id, update_data)
        if not success:
            raise HTTPException(status_code=404, detail="Profile not found or not updated")
        return {"success": True, "message": "Profile updated successfully"}

    @staticmethod
    async def create_profile(profile_data: dict):
        student_id = profile_data.get("student_id")
        if not student_id:
            raise HTTPException(status_code=400, detail="student_id is required")
        
        existing = await ProfileService.get_profile(student_id)
        if existing:
            raise HTTPException(status_code=400, detail="Profile already exists")
        
        result_id = await ProfileService.create_profile(profile_data)
        return {"success": True, "message": "Profile created", "id": result_id}


class CourseController:
    @staticmethod
    async def get_all_courses(student_id: str, semester: Optional[int] = None):
        courses = await CourseService.get_all_courses(student_id, semester)
        return courses

    @staticmethod
    async def get_course(course_id: str):
        course = await CourseService.get_course(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course

    @staticmethod
    async def get_enrolled_courses(student_id: str):
        courses = await CourseService.get_enrolled_courses(student_id)
        return courses


class AttendanceController:
    @staticmethod
    async def get_attendance(
        student_id: str,
        course_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ):
        records = await AttendanceService.get_attendance(
            student_id, course_id, start_date, end_date
        )
        return records

    @staticmethod
    async def get_attendance_summary(student_id: str, course_id: Optional[str] = None):
        summary = await AttendanceService.get_attendance_summary(student_id, course_id)
        return summary


class ExamController:
    @staticmethod
    async def get_all_exams(student_id: str, status: Optional[str] = None):
        exams = await ExamService.get_all_exams(student_id, status)
        return exams

    @staticmethod
    async def get_exam(exam_id: str):
        exam = await ExamService.get_exam(exam_id)
        if not exam:
            raise HTTPException(status_code=404, detail="Exam not found")
        return exam

    @staticmethod
    async def get_upcoming_exams(student_id: str, limit: int = 5):
        exams = await ExamService.get_upcoming_exams(student_id, limit)
        return exams

    @staticmethod
    async def register_for_exam(student_id: str, exam_id: str):
        success = await ExamService.register_for_exam(student_id, exam_id)
        if not success:
            raise HTTPException(status_code=400, detail="Already registered or invalid exam")
        return {"success": True, "message": "Exam registration successful"}


class ResultController:
    @staticmethod
    async def get_results(student_id: str, course_id: Optional[str] = None):
        results = await ResultService.get_results(student_id, course_id)
        return results

    @staticmethod
    async def get_result(result_id: str):
        result = await ResultService.get_result(result_id)
        if not result:
            raise HTTPException(status_code=404, detail="Result not found")
        return result

    @staticmethod
    async def get_cgpa(student_id: str):
        cgpa = await ResultService.calculate_cgpa(student_id)
        return {"student_id": student_id, "cgpa": cgpa}


class FeeController:
    @staticmethod
    async def get_fee_records(student_id: str, status: Optional[str] = None):
        fees = await FeeService.get_fee_records(student_id, status)
        return fees

    @staticmethod
    async def get_fee_summary(student_id: str):
        summary = await FeeService.get_fee_summary(student_id)
        return summary

    @staticmethod
    async def make_payment(fee_id: str, amount: float, payment_method: str):
        success = await FeeService.make_payment(fee_id, amount, payment_method)
        if not success:
            raise HTTPException(status_code=400, detail="Payment failed")
        return {"success": True, "message": "Payment successful"}


class NotificationController:
    @staticmethod
    async def get_notifications(
        student_id: str,
        unread_only: bool = False,
        limit: int = 50
    ):
        notifications = await NotificationService.get_notifications(
            student_id, unread_only, limit
        )
        return notifications

    @staticmethod
    async def mark_as_read(notification_id: str):
        success = await NotificationService.mark_as_read(notification_id)
        if not success:
            raise HTTPException(status_code=404, detail="Notification not found")
        return {"success": True, "message": "Marked as read"}

    @staticmethod
    async def mark_all_as_read(student_id: str):
        count = await NotificationService.mark_all_as_read(student_id)
        return {"success": True, "message": f"Marked {count} notifications as read"}

    @staticmethod
    async def get_unread_count(student_id: str):
        count = await NotificationService.get_unread_count(student_id)
        return {"unread_count": count}


class SettingsController:
    @staticmethod
    async def get_settings(student_id: str):
        settings = await SettingsService.get_settings(student_id)
        if not settings:
            settings = await SettingsService.create_default_settings(student_id)
            settings = await SettingsService.get_settings(student_id)
        return settings

    @staticmethod
    async def update_settings(student_id: str, data: SettingsUpdateRequest):
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No settings to update")
        
        success = await SettingsService.update_settings(student_id, update_data)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to update settings")
        return {"success": True, "message": "Settings updated successfully"}


class DashboardController:
    @staticmethod
    async def get_dashboard(student_id: str):
        data = await DashboardService.get_dashboard_data(student_id)
        return data
