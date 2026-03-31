"""
Student Workspace - Models
==========================
Pydantic models for Student workspace data validation and serialization.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    EXCUSED = "excused"


class ExamStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    POSTPONED = "postponed"


class FeeStatus(str, Enum):
    PAID = "paid"
    PENDING = "pending"
    OVERDUE = "overdue"
    PARTIAL = "partial"


class NotificationType(str, Enum):
    GENERAL = "general"
    ACADEMIC = "academic"
    FEE = "fee"
    EVENT = "event"
    ATTENDANCE = "attendance"
    EXAM = "exam"
    RESULT = "result"


class StudentProfile(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[Gender] = None
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
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Course(BaseModel):
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
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Enrollment(BaseModel):
    enrollment_id: str
    student_id: str
    course_id: str
    course_code: str
    course_name: str
    enrollment_date: str
    status: str = "active"
    grade: Optional[str] = None
    marks: Optional[float] = None
    attendance_percentage: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Attendance(BaseModel):
    attendance_id: str
    student_id: str
    course_id: str
    course_code: str
    date: str
    status: AttendanceStatus
    remarks: Optional[str] = None
    marked_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Exam(BaseModel):
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
    status: ExamStatus = ExamStatus.SCHEDULED
    instructions: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ExamRegistration(BaseModel):
    registration_id: str
    student_id: str
    exam_id: str
    registered_at: str
    status: str = "registered"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Result(BaseModel):
    result_id: str
    student_id: str
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
    is_final: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class FeeRecord(BaseModel):
    fee_id: str
    student_id: str
    fee_type: str
    amount: float
    paid_amount: float = 0.0
    due_date: str
    paid_date: Optional[str] = None
    status: FeeStatus = FeeStatus.PENDING
    academic_year: str
    semester: int
    description: Optional[str] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    remarks: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Notification(BaseModel):
    notification_id: str
    student_id: Optional[str] = None
    title: str
    message: str
    type: NotificationType
    is_read: bool = False
    priority: str = "normal"
    related_id: Optional[str] = None
    related_type: Optional[str] = None
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    read_at: Optional[datetime] = None


class StudentSettings(BaseModel):
    student_id: str
    email_notifications: bool = True
    sms_notifications: bool = True
    push_notifications: bool = True
    attendance_alerts: bool = True
    fee_reminders: bool = True
    exam_reminders: bool = True
    result_notifications: bool = True
    language: str = "en"
    timezone: str = "UTC"
    theme: str = "light"
    updated_at: datetime = Field(default_factory=datetime.utcnow)
