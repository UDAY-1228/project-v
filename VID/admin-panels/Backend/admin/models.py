from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    password_hash: str
    role: str # student, faculty, admin, etc.
    is_active: bool = True
    workspaces: List[str] = [] # List of workspace IDs
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Workspace(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    description: Optional[str] = None
    permissions: List[str] = [] # list of permission scopes

class Notice(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    content: str
    audience: List[str] = ["all"] # all, student, faculty
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None

class AdminDashboardStats(BaseModel):
    institution_overview: dict
    trending_analytics: List[dict]
    user_activity_summary: dict
    workspace_activity_summary: dict
    recent_operations: List[dict]
