"""
Academic Coordinator - Pydantic Models
=======================================
Data models for all Academic Coordinator pages:
Dashboard, Academic Management, Courses, Subjects, Timetable,
Assessments, Reports, Notice Board, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


# ── Shared ──────────────────────────────────────────────────────────────────────

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


# ── Dashboard ───────────────────────────────────────────────────────────────────

class DashboardStats(BaseModel):
    total_courses: int = 0
    total_subjects: int = 0
    total_assessments: int = 0
    active_timetables: int = 0
    pending_reports: int = 0
    unread_notices: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# ── Academic Management ─────────────────────────────────────────────────────────

class AcademicYearBase(BaseModel):
    year_name: str = Field(..., example="2025-2026")
    start_date: datetime
    end_date: datetime
    status: StatusEnum = StatusEnum.active

class AcademicYearCreate(AcademicYearBase):
    pass

class AcademicYear(AcademicYearBase):
    id: str
    institution_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SemesterBase(BaseModel):
    semester_name: str = Field(..., example="Semester 1")
    academic_year_id: str
    start_date: datetime
    end_date: datetime
    status: StatusEnum = StatusEnum.active

class SemesterCreate(SemesterBase):
    pass

class Semester(SemesterBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DepartmentBase(BaseModel):
    department_name: str
    department_code: str
    hod_name: Optional[str] = None
    hod_email: Optional[str] = None
    status: StatusEnum = StatusEnum.active

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: str
    total_faculty: int = 0
    total_students: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ── Courses ─────────────────────────────────────────────────────────────────────

class CourseBase(BaseModel):
    course_name: str
    course_code: str
    department_id: str
    duration_years: int = 4
    total_credits: int = 0
    degree_type: str = Field(default="UG", example="UG")  # UG, PG, PhD
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.active

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: str
    total_students_enrolled: int = 0
    total_subjects: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ── Subjects ────────────────────────────────────────────────────────────────────

class SubjectBase(BaseModel):
    subject_name: str
    subject_code: str
    course_id: str
    semester_id: str
    credits: int = 3
    subject_type: str = Field(default="theory", example="theory")  # theory, lab, elective
    faculty_id: Optional[str] = None
    faculty_name: Optional[str] = None
    max_students: int = 60
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.active

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: str
    enrolled_students: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ── Timetable ───────────────────────────────────────────────────────────────────

class TimetableSlot(BaseModel):
    day: str  # Monday-Saturday
    start_time: str  # e.g., "09:00"
    end_time: str  # e.g., "10:00"
    subject_id: str
    subject_name: Optional[str] = None
    faculty_id: Optional[str] = None
    faculty_name: Optional[str] = None
    room: Optional[str] = None
    slot_type: str = "lecture"  # lecture, lab, tutorial


class TimetableBase(BaseModel):
    timetable_name: str
    course_id: str
    semester_id: str
    academic_year_id: str
    section: str = "A"
    slots: List[TimetableSlot] = []
    status: StatusEnum = StatusEnum.active

class TimetableCreate(TimetableBase):
    pass

class Timetable(TimetableBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ── Assessments ─────────────────────────────────────────────────────────────────

class AssessmentBase(BaseModel):
    assessment_name: str
    assessment_type: str = Field(default="internal", example="internal")  # internal, external, assignment, quiz
    subject_id: str
    subject_name: Optional[str] = None
    course_id: str
    semester_id: str
    total_marks: float = 100
    passing_marks: float = 40
    date: Optional[datetime] = None
    duration_minutes: int = 60
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.draft

class AssessmentCreate(AssessmentBase):
    pass

class Assessment(AssessmentBase):
    id: str
    total_students: int = 0
    submitted_count: int = 0
    average_score: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AssessmentResult(BaseModel):
    assessment_id: str
    student_id: str
    student_name: Optional[str] = None
    marks_obtained: float
    grade: Optional[str] = None
    remarks: Optional[str] = None
    submitted_at: datetime = Field(default_factory=datetime.utcnow)


# ── Reports ─────────────────────────────────────────────────────────────────────

class ReportBase(BaseModel):
    report_name: str
    report_type: str = Field(default="academic", example="academic")
    # academic, attendance, performance, course-wise, department-wise
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    semester_id: Optional[str] = None
    academic_year_id: Optional[str] = None
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


# ── Notice Board ────────────────────────────────────────────────────────────────

class NoticeBase(BaseModel):
    title: str
    content: str
    category: str = Field(default="general", example="general")
    # general, academic, exam, event, urgent
    priority: str = "normal"  # low, normal, high, urgent
    target_audience: List[str] = ["all"]  # all, students, faculty, department
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    attachments: List[str] = []
    posted_by: Optional[str] = None
    expiry_date: Optional[datetime] = None
    is_pinned: bool = False
    status: StatusEnum = StatusEnum.active

class NoticeCreate(NoticeBase):
    pass

class Notice(NoticeBase):
    id: str
    views_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ── Settings ────────────────────────────────────────────────────────────────────

class AcademicSettingsBase(BaseModel):
    grading_system: str = "absolute"  # absolute, relative, cgpa
    max_credits_per_semester: int = 30
    min_attendance_percentage: float = 75.0
    pass_percentage: float = 40.0
    allow_course_registration: bool = True
    result_publication_mode: str = "manual"  # manual, auto
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": False,
        "push": True,
    }
    academic_calendar_enabled: bool = True

class AcademicSettingsCreate(AcademicSettingsBase):
    pass

class AcademicSettings(AcademicSettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
