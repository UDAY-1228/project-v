"""
Library Admin - Pydantic Models
================================
Data models for all Library Admin pages:
Dashboard, Book Control, Issue Return, Fine Control, Reports, Settings
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
    lost = "lost"
    reserved = "reserved"
    pending = "pending"
    paid = "paid"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_books: int = 0
    issued_books: int = 0
    available_books: int = 0
    total_members: int = 0
    overdue_books: int = 0
    total_fines_collected: float = 0.0


class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    publisher: Optional[str] = None
    category: str
    rack_number: Optional[str] = None
    total_copies: int = 1
    available_copies: int = 1
    price: float = 0.0
    status: StatusEnum = StatusEnum.available


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: str
    accession_number: Optional[str] = None
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
    fine_amount: float = 0.0


class IssueReturnCreate(IssueReturnBase):
    pass


class IssueReturn(IssueReturnBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class FineControlBase(BaseModel):
    member_id: str
    member_name: str
    book_id: str
    book_title: str
    fine_type: str
    amount: float
    days_overdue: int = 0
    status: StatusEnum = StatusEnum.pending
    remarks: Optional[str] = None


class FineControlCreate(FineControlBase):
    pass


class FineControl(FineControlBase):
    id: str
    issued_date: datetime = Field(default_factory=datetime.utcnow)
    paid_date: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


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
    max_books_per_member: int = 3
    loan_period_days: int = 14
    fine_per_day: float = 5.0
    max_fine_limit: float = 500.0
    renewal_allowed: bool = True
    notification_preferences: Dict[str, bool] = {"email": True, "sms": False}


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
