import os
from datetime import datetime, timedelta
from typing import Optional, List
from jose import JWTError, jwt
from passlib.context import CryptContext
from enum import Enum
from pydantic import BaseModel

class UserRole(str, Enum):
    SUPER_ADMIN = "super-admin"
    INSTITUTION_ADMIN = "admin"
    PRINCIPAL = "principal"
    VICE_PRINCIPAL = "vice-principal"
    FEES_COORDINATOR = "fees-coordinator"
    MANAGER = "manager"
    ACCOUNTS = "accounts"
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

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
    institution_id: Optional[str] = None

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-it-in-production")
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_token():
    return "token"

def get_current_user():
    return {"username": "current", "role": "admin"}
