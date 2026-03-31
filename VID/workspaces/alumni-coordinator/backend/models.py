"""
Alumni Coordinator - Pydantic Models
====================================
Data models for all Alumni Coordinator pages:
Dashboard, Alumni Records, Events, Communication, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    draft = "draft"
    archived = "archived"
    pending = "pending"
    completed = "completed"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class PaginationParams(BaseModel):
    page: int = 1
    limit: int = 20
    sort_by: str = "created_at"
    sort_order: str = "desc"


class DashboardStats(BaseModel):
    total_alumni: int = 0
    total_events: int = 0
    upcoming_events: int = 0
    total_communications: int = 0
    active_reports: int = 0
    recent_activities: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AlumniRecordBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    graduation_year: int
    degree: str
    department: str
    current_company: Optional[str] = None
    current_position: Optional[str] = None
    current_location: Optional[str] = None
    linkedin_url: Optional[str] = None
    employment_status: str = "employed"
    industry: Optional[str] = None
    achievements: List[str] = []
    notes: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class AlumniRecordCreate(AlumniRecordBase):
    pass


class AlumniRecord(AlumniRecordBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EventBase(BaseModel):
    event_name: str
    event_type: str
    description: Optional[str] = None
    date: datetime
    end_date: Optional[datetime] = None
    venue: Optional[str] = None
    virtual_link: Optional[str] = None
    max_attendees: Optional[int] = None
    registration_required: bool = True
    target_audience: List[str] = ["alumni"]
    organized_by: Optional[str] = None
    speakers: List[Dict[str, str]] = []
    attachments: List[str] = []
    status: StatusEnum = StatusEnum.draft


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: str
    registered_count: int = 0
    attended_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EventRegistration(BaseModel):
    event_id: str
    attendee_id: str
    attendee_name: Optional[str] = None
    attendee_email: Optional[str] = None
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    attendance_status: str = "pending"
    feedback: Optional[str] = None
    rating: Optional[int] = None


class CommunicationBase(BaseModel):
    title: str
    message: str
    communication_type: str = "email"
    recipient_type: str = "all"
    recipient_ids: List[str] = []
    scheduled_at: Optional[datetime] = None
    sent_at: Optional[datetime] = None
    status: StatusEnum = StatusEnum.draft
    template_id: Optional[str] = None
    attachments: List[str] = []


class CommunicationCreate(CommunicationBase):
    pass


class Communication(CommunicationBase):
    id: str
    sent_count: int = 0
    opened_count: int = 0
    clicked_count: int = 0
    failed_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    filters: Optional[Dict[str, Any]] = {}
    generated_by: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SettingsBase(BaseModel):
    institute_name: Optional[str] = None
    coordinator_name: Optional[str] = None
    coordinator_email: Optional[str] = None
    coordinator_phone: Optional[str] = None
    communication_preferences: Dict[str, bool] = {
        "email": True,
        "sms": False,
        "push": True,
    }
    event_reminder_days: int = 7
    alumni_verification_required: bool = True
    data_retention_years: int = 10


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
