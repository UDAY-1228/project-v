"""
Health Monitoring - Pydantic Models
====================================
Data models for Health Monitoring workspace:
Dashboard, Health Records, Medical Reports, Alerts, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    resolved = "resolved"
    critical = "critical"
    normal = "normal"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_patients: int = 0
    total_records: int = 0
    pending_alerts: int = 0
    critical_alerts: int = 0
    reports_generated: int = 0
    active_campaigns: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthRecordBase(BaseModel):
    student_id: str
    student_name: str
    date_of_birth: Optional[datetime] = None
    blood_group: Optional[str] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    allergies: List[str] = []
    chronic_conditions: List[str] = []
    medications: List[str] = []
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    notes: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class HealthRecordCreate(HealthRecordBase):
    pass


class HealthRecord(HealthRecordBase):
    id: str
    last_checkup: Optional[datetime] = None
    next_checkup_due: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MedicalReportBase(BaseModel):
    student_id: str
    student_name: str
    report_type: str = Field(default="checkup", example="checkup")
    examination_date: datetime
    doctor_name: Optional[str] = None
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None
    lab_results: Optional[Dict[str, Any]] = {}
    vitals: Optional[Dict[str, float]] = {}
    attachments: List[str] = []
    follow_up_required: bool = False
    follow_up_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.active


class MedicalReportCreate(MedicalReportBase):
    pass


class MedicalReport(MedicalReportBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AlertBase(BaseModel):
    student_id: Optional[str] = None
    student_name: Optional[str] = None
    alert_type: str = Field(default="health", example="health")
    severity: str = "normal"
    title: str
    description: str
    reported_by: Optional[str] = None
    status: StatusEnum = StatusEnum.pending
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None


class AlertCreate(AlertBase):
    pass


class Alert(AlertBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportBase(BaseModel):
    report_name: str
    report_type: str = Field(default="summary", example="summary")
    start_date: datetime
    end_date: datetime
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    data: Optional[Dict[str, Any]] = {}
    status: StatusEnum = StatusEnum.pending


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class HealthSettingsBase(BaseModel):
    institution_id: Optional[str] = None
    default_checkup_frequency_days: int = 90
    critical_bmi_threshold_min: float = 15.0
    critical_bmi_threshold_max: float = 35.0
    alert_notification_enabled: bool = True
    email_notifications: bool = True
    sms_notifications: bool = False
    push_notifications: bool = True
    auto_generate_reports: bool = False


class HealthSettingsCreate(HealthSettingsBase):
    pass


class HealthSettings(HealthSettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
