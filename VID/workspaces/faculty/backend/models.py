"""
Faculty - Pydantic Models
==========================
Data models for all Faculty workspace pages:
Dashboard, Classes, Attendance, Assignments, Exams, Reports, Profile, Settings
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
    marked = "marked"
    unpublished = "unpublished"


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


class AttendanceStatusEnum(str, Enum):
    present = "present"
    absent = "absent"
    late = "late"
    excused = "excused"


class GradeEnum(str, Enum):
    O = "O"
    A_plus = "A+"
    A = "A"
    B_plus = "B+"
    B = "B"
    C = "C"
    P = "P"
    F = "F"
    absent = "ABS"


class ExamTypeEnum(str, Enum):
    quiz = "quiz"
    class_test = "class_test"
    mid_semester = "mid_semester"
    end_semester = "end_semester"
    practical = "practical"
    assignment = "assignment"
    project = "project"


class DashboardStats(BaseModel):
    total_classes: int = 0
    total_students: int = 0
    total_assignments: int = 0
    pending_assignments: int = 0
    upcoming_exams: int = 0
    average_attendance: float = 0.0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class FacultyProfileBase(BaseModel):
    faculty_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    department: str
    designation: str
    qualification: Optional[str] = None
    specialization: Optional[str] = None
    experience_years: int = 0
    date_of_joining: Optional[datetime] = None
    office_location: Optional[str] = None
    office_hours: Optional[str] = None
    bio: Optional[str] = None
    profile_image_url: Optional[str] = None


class FacultyProfileCreate(FacultyProfileBase):
    pass


class FacultyProfile(FacultyProfileBase):
    id: Optional[str] = None
    total_classes: int = 0
    total_students: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ClassBase(BaseModel):
    class_name: str
    subject_id: str
    subject_name: str
    course_id: str
    course_name: str
    semester_id: str
    semester_name: str
    department_id: str
    department_name: str
    section: str = "A"
    academic_year: str
    room: Optional[str] = None
    building: Optional[str] = None
    total_students: int = 0
    schedule_day: str
    start_time: str
    end_time: str
    status: StatusEnum = StatusEnum.active


class ClassCreate(ClassBase):
    pass


class Class(ClassBase):
    id: str
    faculty_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentBase(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    roll_number: str
    course_id: str
    semester: str
    section: str = "A"


class Student(StudentBase):
    id: str
    attendance_percentage: float = 0.0
    total_classes_attended: int = 0
    total_classes: int = 0


class AttendanceRecord(BaseModel):
    student_id: str
    student_name: str
    roll_number: str
    class_id: str
    date: datetime
    status: AttendanceStatusEnum
    remarks: Optional[str] = None


class AttendanceMark(BaseModel):
    student_id: str
    status: AttendanceStatusEnum
    remarks: Optional[str] = None


class AttendanceCreate(BaseModel):
    class_id: str
    date: datetime
    records: List[AttendanceMark]


class AttendanceSummary(BaseModel):
    student_id: str
    student_name: str
    roll_number: str
    total_classes: int
    classes_attended: int
    classes_absent: int
    percentage: float
    status: str


class AttendanceReport(BaseModel):
    class_id: str
    subject_name: str
    date_range_start: datetime
    date_range_end: datetime
    total_sessions: int
    average_attendance: float
    student_summaries: List[AttendanceSummary]


class AssignmentBase(BaseModel):
    title: str
    description: Optional[str] = None
    class_id: str
    subject_id: str
    subject_name: str
    total_marks: float = 100
    passing_marks: float = 40
    due_date: datetime
    instructions: Optional[str] = None
    attachments: List[str] = []
    allow_late_submission: bool = False
    late_penalty_percentage: float = 10.0
    status: StatusEnum = StatusEnum.draft


class AssignmentCreate(AssignmentBase):
    pass


class Assignment(AssignmentBase):
    id: str
    faculty_id: str
    posted_date: datetime = Field(default_factory=datetime.utcnow)
    total_submissions: int = 0
    evaluated_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AssignmentSubmission(BaseModel):
    assignment_id: str
    student_id: str
    student_name: str
    submission_date: datetime
    marks_obtained: Optional[float] = None
    grade: Optional[GradeEnum] = None
    feedback: Optional[str] = None
    is_late: bool = False
    file_url: Optional[str] = None
    status: str = "submitted"


class ExamBase(BaseModel):
    exam_name: str
    exam_type: ExamTypeEnum
    class_id: str
    subject_id: str
    subject_name: str
    course_id: str
    semester_id: str
    total_marks: float = 100
    passing_marks: float = 40
    exam_date: datetime
    duration_minutes: int = 60
    start_time: str
    end_time: str
    venue: Optional[str] = None
    instructions: Optional[str] = None
    status: StatusEnum = StatusEnum.draft


class ExamCreate(ExamBase):
    pass


class Exam(ExamBase):
    id: str
    faculty_id: str
    total_students: int = 0
    evaluated_count: int = 0
    average_score: float = 0.0
    highest_score: float = 0.0
    lowest_score: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ExamResult(BaseModel):
    exam_id: str
    student_id: str
    student_name: str
    roll_number: str
    marks_obtained: float
    max_marks: float
    percentage: float
    grade: Optional[GradeEnum] = None
    remarks: Optional[str] = None
    is_absent: bool = False
    evaluated_at: Optional[datetime] = None


class ExamResultCreate(BaseModel):
    student_id: str
    marks_obtained: float
    remarks: Optional[str] = None
    is_absent: bool = False


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    department_id: Optional[str] = None
    course_id: Optional[str] = None
    semester_id: Optional[str] = None
    academic_year: Optional[str] = None
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


class FacultySettingsBase(BaseModel):
    notification_email: bool = True
    notification_sms: bool = False
    notification_push: bool = True
    default_lecture_duration: int = 60
    default_attendance_threshold: float = 75.0
    auto_close_assignment_days: int = 7
    auto_publish_results: bool = False
    require_student_verification: bool = True
    theme_preference: str = "dark"
    language_preference: str = "en"


class FacultySettingsCreate(FacultySettingsBase):
    pass


class FacultySettings(FacultySettingsBase):
    id: str
    faculty_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
