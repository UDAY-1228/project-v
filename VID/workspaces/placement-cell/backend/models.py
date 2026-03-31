"""
Placement Cell - Pydantic Models
================================
Data models for all Placement Cell pages:
Dashboard, Companies, Job Drives, Student Applications, Reports, Settings
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
    shortlisted = "shortlisted"
    selected = "selected"
    rejected = "rejected"
    cancelled = "cancelled"


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


# Dashboard

class DashboardStats(BaseModel):
    total_companies: int = 0
    active_drives: int = 0
    total_applications: int = 0
    placed_students: int = 0
    pending_applications: int = 0
    upcoming_drives: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Companies

class CompanyBase(BaseModel):
    company_name: str
    company_code: Optional[str] = None
    industry: str
    website: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = "India"
    pincode: Optional[str] = None
    hr_name: Optional[str] = None
    hr_email: Optional[str] = None
    hr_phone: Optional[str] = None
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: str
    total_drives: int = 0
    total_hires: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Job Drives

class JobDriveBase(BaseModel):
    drive_name: str
    company_id: str
    company_name: Optional[str] = None
    drive_date: datetime
    application_deadline: datetime
    location: str
    mode: str = "offline"
    eligibility_criteria: Optional[str] = None
    minimum_cgpa: Optional[float] = None
    maximum_gaps: Optional[int] = None
    eligible_courses: List[str] = []
    required_skills: List[str] = []
    job_title: str
    job_description: Optional[str] = None
    job_type: str = "full_time"
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    salary_currency: str = "INR"
    bond_years: Optional[int] = None
    total_vacancies: int = 0
    status: StatusEnum = StatusEnum.pending


class JobDriveCreate(JobDriveBase):
    pass


class JobDrive(JobDriveBase):
    id: str
    applications_count: int = 0
    shortlisted_count: int = 0
    selected_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Student Applications

class ApplicationBase(BaseModel):
    student_id: str
    student_name: str
    drive_id: str
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    applied_date: datetime = Field(default_factory=datetime.utcnow)
    resume_url: Optional[str] = None
    status: StatusEnum = StatusEnum.pending
    round: int = 1
    round_name: Optional[str] = None
    remarks: Optional[str] = None
    final_status: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class Application(ApplicationBase):
    id: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ApplicationUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    round: Optional[int] = None
    round_name: Optional[str] = None
    remarks: Optional[str] = None
    final_status: Optional[str] = None


# Reports

class PlacementReportBase(BaseModel):
    report_name: str
    report_type: str = "summary"
    academic_year: str
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    total_students: int = 0
    placed_students: int = 0
    placement_percentage: float = 0.0
    average_salary: float = 0.0
    highest_salary: float = 0.0
    status: StatusEnum = StatusEnum.pending


class PlacementReportCreate(PlacementReportBase):
    pass


class PlacementReport(PlacementReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Settings

class PlacementSettingsBase(BaseModel):
    institution_name: str = "VID Institute"
    tpo_email: str
    tpo_phone: str
    allow_student_registration: bool = True
    auto_reminder_days: List[int] = [7, 3, 1]
    require_approval: bool = True
    max_applications_per_student: int = 10
    placement_season: str = "2025-2026"


class PlacementSettingsCreate(PlacementSettingsBase):
    pass


class PlacementSettings(PlacementSettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
