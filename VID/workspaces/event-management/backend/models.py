"""
Event Management - Pydantic Models
===================================
Data models for all Event Management pages: Dashboard, Events,
Registrations, Scheduling, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    completed = "completed"
    cancelled = "cancelled"
    draft = "draft"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_events: int = 0
    upcoming_events: int = 0
    total_registrations: int = 0
    completed_events: int = 0
    total_revenue: float = 0.0
    average_attendance: float = 0.0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class EventBase(BaseModel):
    event_name: str
    event_type: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    venue: Optional[str] = None
    max_capacity: int = 100
    registration_fee: float = 0.0
    registration_deadline: Optional[datetime] = None
    organizer_name: Optional[str] = None
    organizer_contact: Optional[str] = None
    status: str = "draft"
    is_public: bool = True
    tags: List[str] = []


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: str
    created_by: Optional[str] = None
    registered_count: int = 0
    attended_count: int = 0
    revenue: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class RegistrationBase(BaseModel):
    event_id: str
    participant_name: str
    participant_email: str
    participant_phone: Optional[str] = None
    ticket_type: str = "general"
    payment_status: str = "pending"
    payment_amount: float = 0.0
    payment_method: Optional[str] = None
    attended: bool = False


class RegistrationCreate(RegistrationBase):
    pass


class Registration(RegistrationBase):
    id: str
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    checked_in_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ScheduleSlot(BaseModel):
    slot_name: str
    start_time: datetime
    end_time: datetime
    speaker_name: Optional[str] = None
    speaker_topic: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class ScheduleBase(BaseModel):
    event_id: str
    schedule_date: datetime
    slots: List[ScheduleSlot] = []
    venue: Optional[str] = None


class ScheduleCreate(ScheduleBase):
    pass


class Schedule(ScheduleBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    event_id: Optional[str] = None
    generated_by: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    filters: Optional[Dict[str, Any]] = {}
    status: str = "pending"


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class EventSettingsBase(BaseModel):
    default_registration_fee: float = 0.0
    max_capacity_default: int = 100
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": False,
        "push": True
    }
    reminder_days_before: int = 3
    allow_cancellations: bool = True
    refund_policy_days: int = 7


class EventSettingsCreate(EventSettingsBase):
    pass


class EventSettings(EventSettingsBase):
    id: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
