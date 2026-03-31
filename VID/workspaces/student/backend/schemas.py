"""
Student Workspace - Schemas
===========================
Request/Response schemas for API validation.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class ProfileUpdateRequest(BaseModel):
    phone: Optional[str] = None
    address: Optional[str] = None
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    emergency_contact: Optional[str] = None


class ProfileResponse(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    department: str
    batch: str
    section: Optional[str] = None
    semester: int
    enrollment_date: str
    profile_image: Optional[str] = None
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    emergency_contact: Optional[str] = None
    blood_group: Optional[str] = None
    is_active: bool = True


class CourseResponse(BaseModel):
    course_id: str
    course_code: str
    course_name: str
    credits: int
    department: str
    semester: int
    instructor_name: str
    instructor_email: Optional[str] = None
    description: Optional[str] = None
    schedule: Optional[str] = None
    room: Optional[str] = None


class AttendanceRecordResponse(BaseModel):
    attendance_id: str
    course_id: str
    course_code: str
    date: str
    status: str
    remarks: Optional[str] = None


class AttendanceSummary(BaseModel):
    total_classes: int
    present: int
    absent: int
    late: int
    excused: int
    percentage: float


class ExamResponse(BaseModel):
    exam_id: str
    exam_name: str
    course_id: str
    course_code: str
    course_name: str
    exam_type: str
    date: str
    start_time: str
    end_time: str
    duration_minutes: int
    venue: str
    total_marks: float
    status: str
    instructions: Optional[str] = None


class ResultResponse(BaseModel):
    result_id: str
    course_id: str
    course_code: str
    course_name: str
    exam_id: Optional[str] = None
    exam_name: Optional[str] = None
    marks_obtained: float
    total_marks: float
    percentage: float
    grade: str
    remarks: Optional[str] = None
    published_at: str
    is_final: bool


class FeeRecordResponse(BaseModel):
    fee_id: str
    fee_type: str
    amount: float
    paid_amount: float
    due_date: str
    paid_date: Optional[str] = None
    status: str
    academic_year: str
    semester: int
    description: Optional[str] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None


class FeeSummary(BaseModel):
    total_fees: float
    total_paid: float
    total_pending: float
    overdue_amount: float


class NotificationResponse(BaseModel):
    notification_id: str
    title: str
    message: str
    type: str
    is_read: bool
    priority: str
    related_id: Optional[str] = None
    related_type: Optional[str] = None
    sent_at: datetime
    read_at: Optional[datetime] = None


class DashboardResponse(BaseModel):
    student_name: str
    student_id: str
    department: str
    semester: int
    current_cgpa: Optional[float] = None
    attendance_percentage: float
    total_notifications: int
    unread_notifications: int
    upcoming_exams: int
    pending_fees: float
    enrolled_courses: int
    completed_courses: int


class SettingsUpdateRequest(BaseModel):
    email_notifications: Optional[bool] = None
    sms_notifications: Optional[bool] = None
    push_notifications: Optional[bool] = None
    attendance_alerts: Optional[bool] = None
    fee_reminders: Optional[bool] = None
    exam_reminders: Optional[bool] = None
    result_notifications: Optional[bool] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    theme: Optional[str] = None


class SettingsResponse(BaseModel):
    student_id: str
    email_notifications: bool
    sms_notifications: bool
    push_notifications: bool
    attendance_alerts: bool
    fee_reminders: bool
    exam_reminders: bool
    result_notifications: bool
    language: str
    timezone: str
    theme: str


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    error: Optional[str] = None
