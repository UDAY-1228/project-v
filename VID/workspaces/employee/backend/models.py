"""
Employee - Pydantic Models
==========================
Data models for all Employee pages: Dashboard, Attendance, Tasks,
Leave Requests, Profile, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_tasks: int = 0
    completed_tasks: int = 0
    pending_leaves: int = 0
    attendance_rate: float = 0.0
    upcoming_events: int = 0
    total_hours_worked: float = 0.0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AttendanceBase(BaseModel):
    employee_id: str
    date: datetime
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    status: str = "present"
    hours_worked: float = 0.0
    notes: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass


class Attendance(AttendanceBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TaskBase(BaseModel):
    task_title: str
    task_description: Optional[str] = None
    assigned_to: str
    assigned_by: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: str = "medium"
    status: str = "pending"
    category: Optional[str] = None
    tags: List[str] = []


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TaskUpdate(BaseModel):
    status: Optional[str] = None
    progress: Optional[int] = None
    notes: Optional[str] = None


class LeaveRequestBase(BaseModel):
    employee_id: str
    leave_type: str
    start_date: datetime
    end_date: datetime
    reason: Optional[str] = None
    status: str = "pending"
    is_half_day: bool = False


class LeaveRequestCreate(LeaveRequestBase):
    pass


class LeaveRequest(LeaveRequestBase):
    id: str
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class LeaveBalance(BaseModel):
    employee_id: str
    casual_leave: int = 12
    sick_leave: int = 10
    earned_leave: int = 15
    unpaid_leave: int = 0


class ProfileBase(BaseModel):
    employee_id: str
    full_name: str
    email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    date_of_joining: Optional[datetime] = None
    profile_picture: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EmployeeSettingsBase(BaseModel):
    notification_email: bool = True
    notification_sms: bool = False
    notification_push: bool = True
    theme: str = "dark"
    language: str = "en"
    timezone: str = "UTC"


class EmployeeSettingsCreate(EmployeeSettingsBase):
    pass


class EmployeeSettings(EmployeeSettingsBase):
    id: str
    employee_id: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
