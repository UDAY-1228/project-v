"""
Team Owner - Pydantic Models
=============================
Pydantic models for the Team Owner workspace.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class WorkspaceBase(BaseModel):
    name: str
    description: Optional[str] = None
    workspace_type: str
    is_active: bool = True


class WorkspaceCreate(WorkspaceBase):
    pass


class WorkspaceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    workspace_type: Optional[str] = None
    is_active: Optional[bool] = None


class Workspace(WorkspaceBase):
    id: str = Field(alias="_id")
    owner_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class MemberBase(BaseModel):
    user_id: str
    workspace_id: str
    role: str
    status: str = "active"


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    role: Optional[str] = None
    status: Optional[str] = None


class Member(MemberBase):
    id: str = Field(alias="_id")
    joined_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class AccessControlBase(BaseModel):
    workspace_id: str
    user_id: str
    permissions: List[str]


class AccessControlCreate(AccessControlBase):
    pass


class AccessControlUpdate(BaseModel):
    permissions: Optional[List[str]] = None


class AccessControl(AccessControlBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class ReportBase(BaseModel):
    report_type: str
    title: str
    data: dict
    generated_by: str


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class DashboardStats(BaseModel):
    total_workspaces: int
    total_members: int
    total_access_controls: int
    active_workspaces: int
