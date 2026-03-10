from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

# 1. Institution Tenant Model
class Institution(BaseModel):
    name: str
    code: str
    license_type: str  # trial, standard, premium
    address: dict
    created_at: datetime = Field(default_factory=datetime.utcnow)

# 2. User & Student Identity
class User(BaseModel):
    username: str
    email: str
    role: str  # S/P, T, H, A, D
    inst_id: str
    is_active: bool = True

class StudentProfile(BaseModel):
    user_id: str
    roll_no: str
    grade: str
    section: str
    virtual_id_url: str
    face_encoding: List[float] = []  # Used for AI Attendance

# 3. Attendance Logs
class AttendanceLog(BaseModel):
    student_id: str
    date: datetime
    status: str  # Present, Absent, Late
    method: str  # manual, face_ai, biometric
    institution_id: str

# 4. Payments
class FeePayment(BaseModel):
    student_id: str
    amount: float
    status: str  # Pending, Completed, Failed
    gateway_txn_id: str
    payment_method: str  # UPI, Card, Netbanking
    timestamp: datetime = Field(default_factory=datetime.utcnow)
