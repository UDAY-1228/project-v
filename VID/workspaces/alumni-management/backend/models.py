"""
Alumni Management - Pydantic Models
==================================
Data models for all Alumni Management pages:
Dashboard, Alumni Database, Donations, Events, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    draft = "draft"
    pending = "pending"
    completed = "completed"
    verified = "verified"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_alumni: int = 0
    verified_alumni: int = 0
    total_donations: float = 0.0
    pending_donations: int = 0
    total_events: int = 0
    active_reports: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AlumniDatabaseBase(BaseModel):
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
    is_verified: bool = False
    employment_status: str = "employed"
    industry: Optional[str] = None
    achievements: List[str] = []
    notes: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class AlumniDatabaseCreate(AlumniDatabaseBase):
    pass


class AlumniDatabase(AlumniDatabaseBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DonationBase(BaseModel):
    donor_id: str
    donor_name: str
    donor_email: str
    donation_type: str = "general"
    amount: float
    currency: str = "USD"
    payment_method: str
    transaction_id: Optional[str] = None
    donation_date: datetime
    is_anonymous: bool = False
    message: Optional[str] = None
    status: StatusEnum = StatusEnum.pending
    allocated_to: Optional[str] = None


class DonationCreate(DonationBase):
    pass


class Donation(DonationBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DonationCampaign(BaseModel):
    campaign_name: str
    description: Optional[str] = None
    target_amount: float
    raised_amount: float = 0.0
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)


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
    status: StatusEnum = StatusEnum.draft


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: str
    registered_count: int = 0
    attended_count: int = 0
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
    organization_name: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    address: Optional[str] = None
    tax_id: Optional[str] = None
    receipt_template: Optional[str] = None
    thank_you_message: Optional[str] = None


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)
