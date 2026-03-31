"""
Hostel Admin - Pydantic Models
===============================
Data models for Hostel Admin workspace:
Dashboard, Rooms, Students, Fee Records, Complaints, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    occupied = "occupied"
    vacant = "vacant"
    maintenance = "maintenance"
    pending = "pending"
    resolved = "resolved"
    paid = "paid"
    unpaid = "unpaid"
    partially_paid = "partially_paid"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_rooms: int = 0
    occupied_rooms: int = 0
    vacant_rooms: int = 0
    total_students: int = 0
    pending_complaints: int = 0
    pending_fees: int = 0
    occupancy_rate: float = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class RoomBase(BaseModel):
    room_number: str
    block_name: str
    floor: int
    room_type: str = Field(default="shared", example="shared")
    capacity: int = 4
    current_occupancy: int = 0
    rent_per_student: float = 0
    amenities: List[str] = []
    status: StatusEnum = StatusEnum.vacant


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentBase(BaseModel):
    student_id: str
    student_name: str
    email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    course: Optional[str] = None
    year: int = 1
    room_id: Optional[str] = None
    bed_number: Optional[int] = None
    admission_date: Optional[datetime] = None
    guardian_name: Optional[str] = None
    guardian_phone: Optional[str] = None
    address: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class FeeRecordBase(BaseModel):
    student_id: str
    student_name: str
    fee_type: str = Field(default="hostel", example="hostel")
    amount: float
    paid_amount: float = 0
    due_date: datetime
    paid_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    academic_year: str
    semester: str
    status: StatusEnum = StatusEnum.pending
    remarks: Optional[str] = None


class FeeRecordCreate(FeeRecordBase):
    pass


class FeeRecord(FeeRecordBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ComplaintBase(BaseModel):
    student_id: str
    student_name: str
    room_id: Optional[str] = None
    complaint_type: str = Field(default="maintenance", example="maintenance")
    title: str
    description: str
    priority: str = "normal"
    assigned_to: Optional[str] = None
    status: StatusEnum = StatusEnum.pending
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None


class ComplaintCreate(ComplaintBase):
    pass


class Complaint(ComplaintBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class HostelReportBase(BaseModel):
    report_name: str
    report_type: str = Field(default="summary", example="summary")
    start_date: datetime
    end_date: datetime
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    block_name: Optional[str] = None
    academic_year: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class HostelReportCreate(HostelReportBase):
    pass


class HostelReport(HostelReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class HostelSettingsBase(BaseModel):
    institution_id: Optional[str] = None
    hostel_name: str = "Main Hostel"
    warden_name: Optional[str] = None
    warden_phone: Optional[str] = None
    warden_email: Optional[str] = None
    mess_timing_breakfast: str = "7:00-9:00"
    mess_timing_lunch: str = "12:00-2:00"
    mess_timing_dinner: str = "7:00-9:00"
    curfew_time: str = "21:00"
    visitors_allowed: bool = True
    visitor_timings: str = "10:00-18:00"
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": False,
        "push": True
    }


class HostelSettingsCreate(HostelSettingsBase):
    pass


class HostelSettings(HostelSettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
