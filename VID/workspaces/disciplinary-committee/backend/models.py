"""
Disciplinary Committee - Pydantic Models
==========================================
Data models for Disciplinary Committee: Dashboard, Complaints, Case Records,
Actions, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    pending = "pending"
    investigating = "investigating"
    resolved = "resolved"
    dismissed = "dismissed"
    escalated = "escalated"
    active = "active"
    inactive = "inactive"


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_complaints: int = 0
    pending_complaints: int = 0
    resolved_cases: int = 0
    active_cases: int = 0
    escalated_cases: int = 0
    avg_resolution_days: float = 0.0


class ComplaintBase(BaseModel):
    complaint_title: str
    complaint_type: str
    description: str
    reporter_id: str
    reporter_name: str
    reporter_type: str
    accused_id: Optional[str] = None
    accused_name: Optional[str] = None
    department_id: Optional[str] = None
    incident_date: Optional[datetime] = None
    incident_location: Optional[str] = None
    witnesses: List[str] = []
    evidence: List[str] = []
    priority: PriorityEnum = PriorityEnum.medium
    status: StatusEnum = StatusEnum.pending


class ComplaintCreate(ComplaintBase):
    pass


class Complaint(ComplaintBase):
    id: str
    assigned_to: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    resolved_at: Optional[datetime] = None


class CaseRecordBase(BaseModel):
    case_id: str
    complaint_id: str
    case_title: str
    case_type: str
    assigned_committee_members: List[str] = []
    investigation_start_date: Optional[datetime] = None
    evidence_collected: List[str] = []
    witness_statements: List[Dict[str, str]] = []
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    status: StatusEnum = StatusEnum.investigating


class CaseRecordCreate(CaseRecordBase):
    pass


class CaseRecord(CaseRecordBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ActionBase(BaseModel):
    case_id: str
    action_type: str
    description: str
    action_taken_by: str
    action_taken_by_name: str
    target_id: str
    target_name: str
    severity: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.active


class ActionCreate(ActionBase):
    pass


class Action(ActionBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    case_id: Optional[str] = None
    department_id: Optional[str] = None
    period_start: Optional[datetime] = None
    period_end: Optional[datetime] = None
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    status: StatusEnum = StatusEnum.pending


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SettingsBase(BaseModel):
    committee_name: str
    chair_name: str
    notification_enabled: bool = True
    auto_escalation_days: int = 30
    require_approval_for_actions: bool = True
    retention_period_years: int = 7


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
