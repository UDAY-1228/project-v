"""
Course Coordinator - Pydantic Models
===================================
Data models for all Course Coordinator pages:
Dashboard, Course Planning, Subjects, Faculty Allocation, Reports, Settings
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
    scheduled = "scheduled"


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
    total_courses: int = 0
    total_subjects: int = 0
    total_faculty: int = 0
    active_plans: int = 0
    pending_allocations: int = 0
    upcoming_sessions: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Course Planning

class CoursePlanBase(BaseModel):
    plan_name: str
    academic_year: str
    semester: str
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    start_date: datetime
    end_date: datetime
    objectives: Optional[List[str]] = []
    topics: Optional[List[str]] = []
    expected_outcomes: Optional[List[str]] = []
    resources_required: Optional[List[str]] = []
    status: StatusEnum = StatusEnum.draft


class CoursePlanCreate(CoursePlanBase):
    pass


class CoursePlan(CoursePlanBase):
    id: str
    progress_percentage: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SessionBase(BaseModel):
    session_name: str
    plan_id: str
    faculty_id: Optional[str] = None
    faculty_name: Optional[str] = None
    subject_id: Optional[str] = None
    subject_name: Optional[str] = None
    date: datetime
    start_time: str
    end_time: str
    room: Optional[str] = None
    batch: Optional[str] = None
    session_type: str = "lecture"
    status: StatusEnum = StatusEnum.scheduled


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: str
    attendance_count: int = 0
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Subjects

class SubjectBase(BaseModel):
    subject_name: str
    subject_code: str
    course_id: Optional[str] = None
    course_name: Optional[str] = None
    semester: Optional[str] = None
    credits: int = 3
    subject_type: str = "theory"
    description: Optional[str] = None
    prerequisites: Optional[List[str]] = []
    syllabus: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: str
    enrolled_students: int = 0
    assigned_faculty: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Faculty Allocation

class FacultyBase(BaseModel):
    faculty_id: str
    faculty_name: str
    department: str
    email: str
    phone: Optional[str] = None
    specialization: Optional[str] = None
    max_hours_per_week: int = 20
    current_hours: int = 0
    qualifications: Optional[List[str]] = []
    experience_years: Optional[int] = None
    status: StatusEnum = StatusEnum.active


class FacultyCreate(FacultyBase):
    pass


class Faculty(FacultyBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AllocationBase(BaseModel):
    faculty_id: str
    faculty_name: Optional[str] = None
    subject_id: str
    subject_name: Optional[str] = None
    course_id: Optional[str] = None
    course_name: Optional[str] = None
    semester: Optional[str] = None
    batch: Optional[str] = None
    hours_per_week: int = 3
    academic_year: str
    semester_type: str = "odd"
    status: StatusEnum = StatusEnum.active


class AllocationCreate(AllocationBase):
    pass


class Allocation(AllocationBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Reports

class CoordinatorReportBase(BaseModel):
    report_name: str
    report_type: str = "summary"
    academic_year: str
    department_id: Optional[str] = None
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    total_courses: int = 0
    total_subjects: int = 0
    total_faculty: int = 0
    total_sessions: int = 0
    status: StatusEnum = StatusEnum.pending


class CoordinatorReportCreate(CoordinatorReportBase):
    pass


class CoordinatorReport(CoordinatorReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Settings

class CoordinatorSettingsBase(BaseModel):
    institution_name: str = "VID Institute"
    default_session_duration: int = 60
    max_faculty_hours: int = 20
    min_prerequisite_hours: int = 2
    allow_overload: bool = False
    auto_allocation: bool = False
    notification_enabled: bool = True
    reminder_days: List[int] = [1, 3, 7]


class CoordinatorSettingsCreate(CoordinatorSettingsBase):
    pass


class CoordinatorSettings(CoordinatorSettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
