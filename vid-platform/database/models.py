from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

# 1. Institution Tenant Model
class Institution(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    code: str
    license_type: str  # trial, standard, premium
    settings: dict = {
        "attendance_threshold": 75.0,
        "theme": "indigo",
        "branding_url": ""
    }
    created_at: datetime = Field(default_factory=datetime.utcnow)

# 2. Identity & Access (RBAC)
class Role(BaseModel):
    name: str  # SuperAdmin, Admin, Teacher, Student, Parent
    permissions: List[str]

class User(BaseModel):
    id: str = Field(..., alias="_id")
    username: str
    email: str
    role_id: str
    inst_id: str
    biometric_consent: bool = False
    is_active: bool = True

class StudentProfile(BaseModel):
    user_id: str
    parent_id: Optional[str]
    roll_no: str
    grade: str
    section: str
    virtual_id_qr: str
    face_encoding: List[float] = []  # For AI Attendance

# 3. Academic & Timetable
class TimetablePeriod(BaseModel):
    day: str
    start_time: str
    end_time: str
    subject: str
    teacher_id: str
    room: str

class Timetable(BaseModel):
    inst_id: str
    grade: str
    section: str
    periods: List[TimetablePeriod]
    version: int = 1

# 4. Attendance
class AttendanceLog(BaseModel):
    student_id: str
    inst_id: str
    date: datetime
    status: str  # Present, Absent, Late, Medical
    method: str  # face_ai, manual, kiosk
    flagged: bool = False  # For AI verification doubts

# 5. Learning Management (LMS)
class Course(BaseModel):
    id: str = Field(..., alias="_id")
    inst_id: str
    title: str
    description: str
    teacher_id: str
    syllabus: List[dict]

class Assignment(BaseModel):
    course_id: str
    title: str
    due_date: datetime
    max_marks: int
    ai_grading_enabled: bool = False

class Submission(BaseModel):
    assignment_id: str
    student_id: str
    file_url: str
    submitted_at: datetime
    marks: Optional[float]
    ai_feedback: Optional[str]

# 6. Finance & Fees
class FeePlan(BaseModel):
    inst_id: str
    name: str
    total_amount: float
    installments: int
    heads: List[dict]  # Tuition, Lab, etc.

class Invoice(BaseModel):
    student_id: str
    plan_id: str
    amount_due: float
    status: str  # Paid, Unpaid, Partial
    due_date: datetime

class Transaction(BaseModel):
    invoice_id: str
    amount: float
    method: str  # Razorpay, Cash, etc.
    status: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# 7. Exams & Results
class Exam(BaseModel):
    inst_id: str
    name: str
    start_date: datetime
    end_date: datetime

class MarksEntry(BaseModel):
    exam_id: str
    student_id: str
    subject: str
    marks_obtained: float
    verified_by_hod: bool = False

# 8. Communication & Support
class Notice(BaseModel):
    inst_id: str
    title: str
    content: str
    category: str  # General, Academic, Event
    target_roles: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SupportTicket(BaseModel):
    user_id: str
    subject: str
    description: str
    status: str  # Open, Closed, In-Progress
    priority: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

# 9. Feedback & Audit
class Feedback(BaseModel):
    inst_id: str
    user_id: Optional[str]  # None for anonymous
    content: str
    rating: int  # 1-5
    sentiment_score: Optional[float]

class ActivityLog(BaseModel):
    user_id: str
    action: str
    module: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    ip_address: Optional[str]
