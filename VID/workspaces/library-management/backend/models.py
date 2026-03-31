"""
Library Management - Pydantic Models
=====================================
Data models for all Library Management pages:
Dashboard, Book Catalog, Issue Return, Member Records, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    available = "available"
    issued = "issued"
    reserved = "reserved"
    returned = "returned"
    expired = "expired"
    pending = "pending"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_catalog_books: int = 0
    total_issues: int = 0
    active_members: int = 0
    reserved_books: int = 0
    overdue_returns: int = 0
    monthly_issues: int = 0


class BookCatalogBase(BaseModel):
    title: str
    author: str
    isbn: str
    publisher: Optional[str] = None
    edition: Optional[str] = None
    category: str
    sub_category: Optional[str] = None
    language: str = "English"
    pages: int = 0
    price: float = 0.0
    rack_location: Optional[str] = None
    summary: Optional[str] = None
    status: StatusEnum = StatusEnum.available


class BookCatalogCreate(BookCatalogBase):
    pass


class BookCatalog(BookCatalogBase):
    id: str
    accession_number: Optional[str] = None
    copies_total: int = 1
    copies_available: int = 1
    times_issued: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class IssueReturnBase(BaseModel):
    book_id: str
    member_id: str
    member_name: str
    book_title: str
    issue_date: datetime
    due_date: datetime
    return_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.issued
    remarks: Optional[str] = None


class IssueReturnCreate(IssueReturnBase):
    pass


class IssueReturn(IssueReturnBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MemberRecordBase(BaseModel):
    member_name: str
    email: str
    phone: str
    member_type: str
    department: Optional[str] = None
    enrollment_number: Optional[str] = None
    address: Optional[str] = None
    membership_start: datetime
    membership_expiry: datetime
    max_books_allowed: int = 3
    status: StatusEnum = StatusEnum.active


class MemberRecordCreate(MemberRecordBase):
    pass


class MemberRecord(MemberRecordBase):
    id: str
    member_id: str
    books_issued: int = 0
    fines_pending: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
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


class SettingsBase(BaseModel):
    library_name: str
    address: Optional[str] = None
    max_books_per_member: int = 3
    loan_period_days: int = 14
    grace_period_days: int = 2
    fine_per_day: float = 5.0
    renewal_limit: int = 2
    notification_preferences: Dict[str, bool] = {"email": True, "sms": False}


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
