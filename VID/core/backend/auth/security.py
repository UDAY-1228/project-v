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

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        institution_id: str = payload.get("institution_id")
        if username is None:
            raise credentials_exception
        return TokenData(username=username, role=role, institution_id=institution_id)
    except JWTError:
        raise credentials_exception

def get_current_token():
    return "token"

def check_role(allowed_roles: List[str]):
    async def role_checker(current_user: TokenData = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted"
            )
        return current_user
    return role_checker
