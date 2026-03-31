"""
Student Workspace - Routes
==========================
API route definitions for Student workspace.
"""

from fastapi import APIRouter, Depends, Query, Header
from typing import Optional
from .controllers import (
    ProfileController, CourseController, AttendanceController,
    ExamController, ResultController, FeeController,
    NotificationController, SettingsController, DashboardController
)
from .schemas import (
    ProfileUpdateRequest, DashboardResponse, CourseResponse,
    AttendanceRecordResponse, AttendanceSummary, ExamResponse,
    ResultResponse, FeeRecordResponse, FeeSummary, NotificationResponse,
    SettingsUpdateRequest, SettingsResponse, ApiResponse
)

router = APIRouter(prefix="/api/student", tags=["Student"])


def get_current_student_id(x_student_id: str = Header(...)) -> str:
    return x_student_id


@router.get("/dashboard")
async def get_dashboard(student_id: str = Depends(get_current_student_id)):
    return await DashboardController.get_dashboard(student_id)


@router.get("/profile")
async def get_profile(student_id: str = Depends(get_current_student_id)):
    return await ProfileController.get_profile(student_id)


@router.put("/profile")
async def update_profile(
    data: ProfileUpdateRequest,
    student_id: str = Depends(get_current_student_id)
):
    return await ProfileController.update_profile(student_id, data)


@router.get("/courses")
async def get_courses(
    student_id: str = Depends(get_current_student_id),
    semester: Optional[int] = None
):
    return await CourseController.get_all_courses(student_id, semester)


@router.get("/courses/enrolled")
async def get_enrolled_courses(student_id: str = Depends(get_current_student_id)):
    return await CourseController.get_enrolled_courses(student_id)


@router.get("/courses/{course_id}")
async def get_course(course_id: str):
    return await CourseController.get_course(course_id)


@router.get("/attendance")
async def get_attendance(
    student_id: str = Depends(get_current_student_id),
    course_id: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    return await AttendanceController.get_attendance(
        student_id, course_id, start_date, end_date
    )


@router.get("/attendance/summary")
async def get_attendance_summary(
    student_id: str = Depends(get_current_student_id),
    course_id: Optional[str] = None
):
    return await AttendanceController.get_attendance_summary(student_id, course_id)


@router.get("/exams")
async def get_exams(
    student_id: str = Depends(get_current_student_id),
    status: Optional[str] = None
):
    return await ExamController.get_all_exams(student_id, status)


@router.get("/exams/upcoming")
async def get_upcoming_exams(
    student_id: str = Depends(get_current_student_id),
    limit: int = Query(default=5, ge=1, le=20)
):
    return await ExamController.get_upcoming_exams(student_id, limit)


@router.get("/exams/{exam_id}")
async def get_exam(exam_id: str):
    return await ExamController.get_exam(exam_id)


@router.post("/exams/{exam_id}/register")
async def register_for_exam(
    exam_id: str,
    student_id: str = Depends(get_current_student_id)
):
    return await ExamController.register_for_exam(student_id, exam_id)


@router.get("/results")
async def get_results(
    student_id: str = Depends(get_current_student_id),
    course_id: Optional[str] = None
):
    return await ResultController.get_results(student_id, course_id)


@router.get("/results/cgpa")
async def get_cgpa(student_id: str = Depends(get_current_student_id)):
    return await ResultController.get_cgpa(student_id)


@router.get("/results/{result_id}")
async def get_result(result_id: str):
    return await ResultController.get_result(result_id)


@router.get("/fees")
async def get_fees(
    student_id: str = Depends(get_current_student_id),
    status: Optional[str] = None
):
    return await FeeController.get_fee_records(student_id, status)


@router.get("/fees/summary")
async def get_fee_summary(student_id: str = Depends(get_current_student_id)):
    return await FeeController.get_fee_summary(student_id)


@router.post("/fees/{fee_id}/pay")
async def make_payment(
    fee_id: str,
    amount: float = Query(gt=0),
    payment_method: str = Query(min_length=1),
    student_id: str = Depends(get_current_student_id)
):
    return await FeeController.make_payment(fee_id, amount, payment_method)


@router.get("/notifications")
async def get_notifications(
    student_id: str = Depends(get_current_student_id),
    unread_only: bool = False,
    limit: int = Query(default=50, ge=1, le=100)
):
    return await NotificationController.get_notifications(
        student_id, unread_only, limit
    )


@router.get("/notifications/unread-count")
async def get_unread_count(student_id: str = Depends(get_current_student_id)):
    return await NotificationController.get_unread_count(student_id)


@router.put("/notifications/{notification_id}/read")
async def mark_notification_as_read(notification_id: str):
    return await NotificationController.mark_as_read(notification_id)


@router.put("/notifications/read-all")
async def mark_all_notifications_as_read(
    student_id: str = Depends(get_current_student_id)
):
    return await NotificationController.mark_all_as_read(student_id)


@router.get("/settings")
async def get_settings(student_id: str = Depends(get_current_student_id)):
    return await SettingsController.get_settings(student_id)


@router.put("/settings")
async def update_settings(
    data: SettingsUpdateRequest,
    student_id: str = Depends(get_current_student_id)
):
    return await SettingsController.update_settings(student_id, data)
