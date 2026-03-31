"""
Admission Officer - Pydantic Models
=====================================
Data models for all Admission Officer pages:
Dashboard, Applications, Student Admissions, Document Verification,
Fee Details, Reports, Settings
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
    under_review = "under_review"
    completed = "completed"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_applications: int = 0
    pending_applications: int = 0
    approved_applications: int = 0
    rejected_applications: int = 0
    total_admissions: int = 0
    verified_documents: int = 0


class ApplicationBase(BaseModel):
    applicant_name: str
    email: str
    phone: str
    date_of_birth: datetime
    gender: str
    address: str
    course_applied: str
    academic_background: List[Dict[str, Any]] = []
    status: StatusEnum = StatusEnum.pending


class ApplicationCreate(ApplicationBase):
    pass


class Application(ApplicationBase):
    id: str
    application_number: Optional[str] = None
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentAdmissionBase(BaseModel):
    application_id: str
    student_name: str
    admission_number: str
    roll_number: Optional[str] = None
    course: str
    batch: str
    semester: int = 1
    status: StatusEnum = StatusEnum.active
    fees_paid: bool = False


class StudentAdmissionCreate(StudentAdmissionBase):
    pass


class StudentAdmission(StudentAdmissionBase):
    id: str
    admission_date: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DocumentVerificationBase(BaseModel):
    application_id: str
    student_name: str
    documents: List[Dict[str, str]] = []
    status: StatusEnum = StatusEnum.pending
    verified_by: Optional[str] = None
    remarks: Optional[str] = None


class DocumentVerificationCreate(DocumentVerificationBase):
    pass


class DocumentVerification(DocumentVerificationBase):
    id: str
    verified_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class FeeDetailsBase(BaseModel):
    student_id: str
    student_name: str
    course: str
    fee_type: str
    total_amount: float
    paid_amount: float = 0.0
    pending_amount: float
    payment_status: StatusEnum = StatusEnum.pending
    due_date: datetime
    payment_history: List[Dict[str, Any]] = []


class FeeDetailsCreate(FeeDetailsBase):
    pass


class FeeDetails(FeeDetailsBase):
    id: str
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
    admission_cycle: str
    application_fee: float
    acceptance_fee: float
    max_intake: int
    current_intake: int = 0
    notification_preferences: Dict[str, bool] = {"email": True, "sms": False}


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
