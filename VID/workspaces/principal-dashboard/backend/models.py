"""
Principal Dashboard - Pydantic Models
======================================
Data models for Principal Dashboard: Dashboard, Institution Overview,
Staff Stats, Student Stats, Reports, Policies, Settings
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
    draft = "draft"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_students: int = 0
    total_staff: int = 0
    total_departments: int = 0
    total_courses: int = 0
    avg_attendance: float = 0.0
    pending_approvals: int = 0


class InstitutionOverviewBase(BaseModel):
    institution_name: str
    established_year: int
    accreditation_status: str
    total_campuses: int = 1
    total_buildings: int = 1
    total_labs: int = 0
    total_libraries: int = 1
    total_hostels: int = 0


class InstitutionOverviewCreate(InstitutionOverviewBase):
    pass


class InstitutionOverview(InstitutionOverviewBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StaffStatsBase(BaseModel):
    department_id: str
    department_name: str
    total_teaching_staff: int = 0
    total_non_teaching_staff: int = 0
    phd_holders: int = 0
    avg_experience_years: float = 0.0
    faculty_student_ratio: float = 0.0


class StaffStatsCreate(StaffStatsBase):
    pass


class StaffStats(StaffStatsBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentStatsBase(BaseModel):
    course_id: str
    course_name: str
    total_enrolled: int = 0
    total_passed: int = 0
    total_failed: int = 0
    avg_gpa: float = 0.0
    placement_percentage: float = 0.0


class StudentStatsCreate(StudentStatsBase):
    pass


class StudentStats(StudentStatsBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    status: StatusEnum = StatusEnum.pending


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class PolicyBase(BaseModel):
    policy_name: str
    policy_type: str
    description: str
    applicable_to: List[str] = ["all"]
    department_id: Optional[str] = None
    effective_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.active


class PolicyCreate(PolicyBase):
    pass


class Policy(PolicyBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SettingsBase(BaseModel):
    academic_year: str
    semester_system: str = "semester"
    grading_system: str = "cgpa"
    max_students_per_class: int = 60
    attendance_threshold: float = 75.0
    pass_percentage: float = 40.0


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    institution_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
