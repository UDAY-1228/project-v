"""
AI-Yantra - Pydantic Models
=============================
Data models for all AI-Yantra pages:
Dashboard, AI Tools, Automation Panel, Model Control, Analytics, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    running = "running"
    stopped = "stopped"
    pending = "pending"
    completed = "completed"
    failed = "failed"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class AIToolBase(BaseModel):
    name: str
    description: str
    tool_type: str
    category: str
    config: Dict[str, Any] = {}
    status: StatusEnum = StatusEnum.inactive


class AIToolCreate(AIToolBase):
    pass


class AITool(AIToolBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AutomationBase(BaseModel):
    name: str
    description: str
    trigger_type: str
    conditions: List[Dict[str, Any]] = []
    actions: List[Dict[str, Any]] = []
    is_active: bool = True
    schedule: Optional[str] = None


class AutomationCreate(AutomationBase):
    pass


class Automation(AutomationBase):
    id: str
    last_run: Optional[datetime] = None
    run_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ModelBase(BaseModel):
    name: str
    model_type: str
    version: str
    framework: str
    status: StatusEnum = StatusEnum.stopped
    config: Dict[str, Any] = {}
    metadata: Dict[str, Any] = {}


class ModelCreate(ModelBase):
    pass


class Model(ModelBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    name: str
    report_type: str
    date_from: datetime
    date_to: datetime
    filters: Dict[str, Any] = {}
    generated_by: Optional[str] = None


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DashboardStats(BaseModel):
    total_models: int = 0
    active_models: int = 0
    total_automations: int = 0
    active_automations: int = 0
    api_calls_today: int = 0
    success_rate: float = 0.0


class AnalyticsData(BaseModel):
    metric_name: str
    value: float
    unit: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = {}


class SettingsBase(BaseModel):
    ai_provider: str = "openai"
    api_key_env: str = "OPENAI_API_KEY"
    max_tokens: int = 2048
    temperature: float = 0.7
    default_model: str = "gpt-4"
    rate_limit: int = 100
    enable_caching: bool = True
    cache_ttl: int = 3600


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
