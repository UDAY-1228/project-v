"""
Pydantic Models / Schemas for EIMS
All MongoDB document schemas with full validation
"""
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field, EmailStr, validator
from bson import ObjectId


# ─── Enums ────────────────────────────────────────────────────────────────────

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    INSTITUTION_ADMIN = "institution_admin"
    FACULTY = "faculty"
    ED_OFFICIAL = "ed_official"
    STUDENT = "student"
    PARENT = "parent"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    EXCUSED = "excused"


class FeeStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    WAIVED = "waived"
    PARTIAL = "partial"


class ExamType(str, Enum):
    UNIT_TEST = "unit_test"
    MID_TERM = "mid_term"
    FINAL = "final"
    PRACTICE = "practice"


class AssignmentStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    SUBMITTED = "submitted"
    GRADED = "graded"


class NotificationType(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ALERT = "alert"
    REMINDER = "reminder"


# ─── Address ─────────────────────────────────────────────────────────────────

class Address(BaseModel):
    street: str
    city: str = "Hyderabad"
    state: str = "Telangana"
    pincode: str
    country: str = "India"


# ─── Institution ──────────────────────────────────────────────────────────────

class InstitutionCreate(BaseModel):
    name: str
    code: str  # unique short code e.g. "DPS-HYD"
    type: str  # school, college, university
    address: Address
    phone: str
    email: EmailStr
    website: Optional[str] = None
    logo_url: Optional[str] = None
    affiliation_board: Optional[str] = None  # CBSE, ICSE, SSC, etc.
    academic_year: str = "2024-25"
    languages: List[str] = ["en", "te"]
    total_capacity: int = 1000
    is_active: bool = True


class Institution(InstitutionCreate):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ─── User / Profile ───────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    role: UserRole
    institution_id: Optional[str] = None
    gender: Gender = Gender.MALE
    date_of_birth: Optional[str] = None
    address: Optional[Address] = None
    language_preference: str = "en"
    profile_photo: Optional[str] = None


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[Address] = None
    profile_photo: Optional[str] = None
    language_preference: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    full_name: str
    email: str
    phone: str
    role: UserRole
    institution_id: Optional[str] = None
    gender: Gender
    profile_photo: Optional[str] = None
    is_active: bool
    created_at: datetime
    virtual_id: Optional[str] = None
    qr_code_url: Optional[str] = None
    face_enrolled: bool = False


# ─── Auth ─────────────────────────────────────────────────────────────────────

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    institution_code: Optional[str] = None


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    role: UserRole
    user: UserResponse


class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ─── Student ──────────────────────────────────────────────────────────────────

class StudentProfile(BaseModel):
    user_id: str
    institution_id: str
    roll_number: str
    class_name: str
    section: str
    admission_number: str
    parents: List[str] = []  # parent user_ids
    academic_year: str
    subjects: List[str] = []
    bus_route: Optional[str] = None
    hostel: bool = False
    scholarship: bool = False


# ─── Attendance ───────────────────────────────────────────────────────────────

class AttendanceLog(BaseModel):
    student_id: str
    institution_id: str
    class_name: str
    section: str
    date: str  # YYYY-MM-DD
    subject: Optional[str] = None
    status: AttendanceStatus
    method: str = "manual"  # manual, face_ai, qr, kiosk
    marked_by: str  # teacher/faculty user_id
    ai_confidence: Optional[float] = None
    override_reason: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AttendanceSummary(BaseModel):
    student_id: str
    total_days: int
    present_days: int
    absent_days: int
    late_days: int
    percentage: float
    at_risk: bool = False


# ─── Timetable ────────────────────────────────────────────────────────────────

class TimetableSlot(BaseModel):
    day: str  # Monday-Saturday
    period: int
    start_time: str  # "09:00"
    end_time: str   # "09:45"
    subject: str
    faculty_id: str
    room: str
    class_name: str
    section: str


class Timetable(BaseModel):
    institution_id: str
    class_name: str
    section: str
    academic_year: str
    term: str
    slots: List[TimetableSlot]
    generated_by_ai: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ─── Fees ─────────────────────────────────────────────────────────────────────

class FeeItem(BaseModel):
    description: str
    amount: float
    due_date: str  # YYYY-MM-DD


class FeeInvoice(BaseModel):
    student_id: str
    institution_id: str
    invoice_number: str
    academic_year: str
    term: str
    items: List[FeeItem]
    total_amount: float
    paid_amount: float = 0.0
    status: FeeStatus = FeeStatus.PENDING
    payment_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    waiver_reason: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FeePlan(BaseModel):
    institution_id: str
    name: str
    class_names: List[str]
    items: List[FeeItem]
    total_amount: float
    installments: int = 1
    late_fee: float = 0.0


# ─── LMS / Courses ────────────────────────────────────────────────────────────

class CourseContent(BaseModel):
    title: str
    content_type: str  # video, pdf, quiz, link
    url: str
    duration_minutes: Optional[int] = None
    order: int


class Course(BaseModel):
    institution_id: str
    title: str
    subject: str
    class_name: str
    faculty_id: str
    description: str
    thumbnail_url: Optional[str] = None
    contents: List[CourseContent] = []
    published: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Assignment(BaseModel):
    institution_id: str
    title: str
    description: str
    subject: str
    class_name: str
    section: str
    faculty_id: str
    due_date: str
    max_marks: float
    allow_late: bool = False
    attachments: List[str] = []
    status: AssignmentStatus = AssignmentStatus.DRAFT
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Submission(BaseModel):
    assignment_id: str
    student_id: str
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
    files: List[str] = []
    text_response: Optional[str] = None
    marks_obtained: Optional[float] = None
    feedback: Optional[str] = None
    graded_by: Optional[str] = None
    ai_checked: bool = False


# ─── Exams ────────────────────────────────────────────────────────────────────

class ExamQuestion(BaseModel):
    question: str
    options: Optional[List[str]] = None  # MCQ
    correct_answer: Optional[str] = None
    marks: float
    type: str  # mcq, short, long


class Exam(BaseModel):
    institution_id: str
    title: str
    subject: str
    class_name: str
    section: str
    exam_type: ExamType
    date: str
    start_time: str
    end_time: str
    total_marks: float
    pass_marks: float
    questions: List[ExamQuestion] = []
    created_by: str
    is_online: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExamResult(BaseModel):
    exam_id: str
    student_id: str
    marks_obtained: float
    grade: str
    rank: Optional[int] = None
    remarks: Optional[str] = None
    subject_scores: Dict[str, float] = {}
    published: bool = False
    published_at: Optional[datetime] = None


# ─── Communication ────────────────────────────────────────────────────────────

class Message(BaseModel):
    sender_id: str
    receiver_id: Optional[str] = None  # None = broadcast
    room_id: Optional[str] = None  # Group chat
    content: str
    attachments: List[str] = []
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False


class Notice(BaseModel):
    institution_id: str
    title: str
    content: str
    author_id: str
    target_roles: List[UserRole] = []
    target_classes: List[str] = []
    priority: str = "normal"  # low, normal, high, urgent
    attachments: List[str] = []
    published_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None


class PTMSlot(BaseModel):
    institution_id: str
    faculty_id: str
    date: str
    start_time: str
    end_time: str
    slot_duration: int = 15  # minutes
    available_slots: int = 0
    booked_slots: List[Dict[str, Any]] = []


# ─── Virtual ID ───────────────────────────────────────────────────────────────

class VirtualID(BaseModel):
    user_id: str
    institution_id: str
    virtual_id_number: str  # e.g. "EIMS-DPS-2024-001"
    qr_code_url: str
    qr_code_data: str
    face_encoding_hash: Optional[str] = None
    face_enrolled: bool = False
    face_enrollment_date: Optional[datetime] = None
    is_active: bool = True
    issued_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None


class FaceEnrollRequest(BaseModel):
    user_id: str
    consent: bool = True  # GDPR/biometric consent


# ─── Notifications ────────────────────────────────────────────────────────────

class Notification(BaseModel):
    user_id: str
    title: str
    message: str
    type: NotificationType = NotificationType.INFO
    action_url: Optional[str] = None
    read: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ─── Analytics ────────────────────────────────────────────────────────────────

class AtRiskAlert(BaseModel):
    student_id: str
    institution_id: str
    risk_score: float  # 0.0 - 1.0
    risk_factors: List[str]
    recommended_actions: List[str]
    generated_at: datetime = Field(default_factory=datetime.utcnow)


# ─── Audit Log ────────────────────────────────────────────────────────────────

class AuditLog(BaseModel):
    user_id: str
    institution_id: Optional[str] = None
    action: str
    resource: str
    resource_id: Optional[str] = None
    details: Dict[str, Any] = {}
    ip_address: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
