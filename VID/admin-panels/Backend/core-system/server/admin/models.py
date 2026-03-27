from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    full_name: str
    email: str
    role: str # Principal, Faculty, Coordinator, Student, Officer, Staff
    assigned_workspaces: List[str] = []

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    institution_id: str
    created_at: datetime

class LoginSchema(BaseModel):
    username: str
    password: str
    institution_id: str
