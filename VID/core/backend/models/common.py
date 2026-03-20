from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = "super-admin"
    INSTITUTION_ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    STAFF = "staff"
    ACADEMIC_COORDINATOR = "academic-coordinator"
    ADMISSION_OFFICER = "admission-officer"
    TEAM_OWNER = "team-owner"
    TRANSPORT_COORDINATOR = "transport-coordinator"
    EMPLOYEE = "employee"
    HOSTEL_ADMIN = "hostel-admin"
    FACULTY = "faculty"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    is_active: bool = True
    role: UserRole
    institution_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str = Field(alias="_id")
    hashed_password: str

class InstitutionBase(BaseModel):
    name: str
    address: str
    phone: str
    email: EmailStr
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Institution(InstitutionBase):
    id: str = Field(alias="_id")
    admin_user_id: str

class InstitutionCreate(InstitutionBase):
    pass
