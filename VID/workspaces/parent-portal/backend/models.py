"""
Parent Portal - Pydantic Models
===============================
Data models for all Parent Portal pages:
Dashboard, Student Progress, Attendance, Fee Status, Notifications, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    paid = "paid"
    unpaid = "unpaid"
    partial = "partial"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_students: int = 0
    average_attendance: float = 0.0
    pending_fees: float = 0.0
    upcoming_events: int = 0
    unread_notifications: int = 0
    recent_activities: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    student_name: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class StudentProgressBase(BaseModel):
    student_id: str
    student_name: str
    course: str
    semester: str
    subjects: List[Dict[str, Any]] = []
    assignments: List[Dict[str, Any]] = []
    exams: List[Dict[str, Any]] = []
    overall_percentage: float = 0.0
    grade: Optional[str] = None
    rank: Optional[int] = None
    attendance_percentage: float = 0.0
    remarks: Optional[str] = None


class StudentProgressCreate(StudentProgressBase):
    pass


class StudentProgress(StudentProgressBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AttendanceBase(BaseModel):
    student_id: str
    student_name: str
    date: datetime
    status: str = "present"
    reason: Optional[str] = None
    marked_by: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass


class Attendance(AttendanceBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AttendanceSummary(BaseModel):
    student_id: str
    student_name: str
    total_days: int = 0
    present_days: int = 0
    absent_days: int = 0
    leave_days: int = 0
    attendance_percentage: float = 0.0
    monthly_breakdown: List[Dict[str, Any]] = []


class FeeStatusBase(BaseModel):
    student_id: str
    student_name: str
    fee_type: str
    total_amount: float
    paid_amount: float = 0.0
    pending_amount: float = 0.0
    due_date: Optional[datetime] = None
    paid_date: Optional[datetime] = None
    payment_mode: Optional[str] = None
    transaction_id: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class FeeStatusCreate(FeeStatusBase):
    pass


class FeeStatus(FeeStatusBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class FeePayment(BaseModel):
    fee_id: str
    amount: float
    payment_mode: str
    transaction_id: Optional[str] = None
    payment_date: datetime = Field(default_factory=datetime.utcnow)
    remarks: Optional[str] = None


class NotificationBase(BaseModel):
    title: str
    message: str
    notification_type: str = "general"
    priority: str = "normal"
    recipient_ids: List[str] = []
    related_student_id: Optional[str] = None
    is_read: bool = False
    expires_at: Optional[datetime] = None


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SettingsBase(BaseModel):
    parent_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": True,
        "push": True,
    }
    language: str = "en"
    timezone: str = "UTC"


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    parent_id: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)
