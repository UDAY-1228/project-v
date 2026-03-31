"""
Research Development - Pydantic Models
=======================================
Data models for Research Development: Dashboard, Research Projects,
Publications, Grants, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    completed = "completed"
    draft = "draft"
    approved = "approved"
    rejected = "rejected"
    in_progress = "in_progress"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_projects: int = 0
    active_projects: int = 0
    completed_projects: int = 0
    total_publications: int = 0
    total_grants: int = 0
    total_funding_received: float = 0.0


class ResearchProjectBase(BaseModel):
    project_title: str
    project_code: str
    project_type: str
    principal_investigator: str
    pi_department: str
    co_investigators: List[str] = []
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    duration_months: int = 0
    funding_agency: Optional[str] = None
    grant_id: Optional[str] = None
    total_budget: float = 0.0
    abstract: Optional[str] = None
    objectives: List[str] = []
    methodology: Optional[str] = None
    status: StatusEnum = StatusEnum.draft


class ResearchProjectCreate(ResearchProjectBase):
    pass


class ResearchProject(ResearchProjectBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class PublicationBase(BaseModel):
    publication_title: str
    authors: List[str]
    corresponding_author: str
    department: str
    journal_name: str
    journal_issn: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    publication_date: Optional[datetime] = None
    doi: Optional[str] = None
    publication_type: str
    indexing: List[str] = []
    impact_factor: Optional[float] = None
    citations_count: int = 0
    project_id: Optional[str] = None
    status: StatusEnum = StatusEnum.draft


class PublicationCreate(PublicationBase):
    pass


class Publication(PublicationBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class GrantBase(BaseModel):
    grant_title: str
    grant_type: str
    funding_agency: str
    agency_type: str
    principal_investigator: str
    pi_department: str
    co_investigators: List[str] = []
    application_date: Optional[datetime] = None
    grant_amount: float = 0.0
    currency: str = "INR"
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.pending
    deliverables: List[str] = []
    description: Optional[str] = None


class GrantCreate(GrantBase):
    pass


class Grant(GrantBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    project_id: Optional[str] = None
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
    research_policy_enabled: bool = True
    publication_threshold_per_year: int = 2
    minimum_impact_factor: float = 0.0
    plagiarism_check_required: bool = True
    review_committee_required: bool = True
    ethics_approval_required: bool = True


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
