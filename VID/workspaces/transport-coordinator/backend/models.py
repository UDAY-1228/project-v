"""
Transport Coordinator - Pydantic Models
========================================
Data models for Transport Coordinator workspace:
Dashboard, Vehicles, Routes, Student Transport, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    maintenance = "maintenance"
    retired = "retired"
    pending = "pending"
    completed = "completed"
    on_route = "on_route"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_vehicles: int = 0
    active_vehicles: int = 0
    total_routes: int = 0
    total_students_transported: int = 0
    pending_maintenance: int = 0
    active_trips: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class VehicleBase(BaseModel):
    vehicle_number: str
    vehicle_type: str = Field(default="bus", example="bus")
    capacity: int = 40
    driver_name: Optional[str] = None
    driver_phone: Optional[str] = None
    conductor_name: Optional[str] = None
    conductor_phone: Optional[str] = None
    fuel_type: str = "diesel"
    status: StatusEnum = StatusEnum.active
    insurance_expiry: Optional[datetime] = None
    pollution_cert_expiry: Optional[datetime] = None
    fitness_cert_expiry: Optional[datetime] = None


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: str
    last_service_date: Optional[datetime] = None
    next_service_due: Optional[datetime] = None
    total_km_traveled: float = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class RouteBase(BaseModel):
    route_name: str
    route_code: str
    start_point: str
    end_point: str
    distance_km: float = 0
    estimated_duration_minutes: int = 0
    stops: List[Dict[str, Any]] = []
    vehicle_id: Optional[str] = None
    driver_id: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class RouteCreate(RouteBase):
    pass


class Route(RouteBase):
    id: str
    total_students_assigned: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentTransportBase(BaseModel):
    student_id: str
    student_name: str
    route_id: str
    pickup_point: str
    drop_point: str
    pickup_time: Optional[str] = None
    drop_time: Optional[str] = None
    is_active: bool = True
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class StudentTransportCreate(StudentTransportBase):
    pass


class StudentTransport(StudentTransportBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TripLogBase(BaseModel):
    vehicle_id: str
    route_id: str
    driver_id: str
    trip_date: datetime
    start_time: datetime
    end_time: Optional[datetime] = None
    start_km: float = 0
    end_km: float = 0
    students_onboard: int = 0
    trip_type: str = "pickup"
    status: StatusEnum = StatusEnum.pending


class TripLogCreate(TripLogBase):
    pass


class TripLog(TripLogBase):
    id: str
    distance_covered: float = 0
    fuel_consumed: float = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TransportReportBase(BaseModel):
    report_name: str
    report_type: str = Field(default="summary", example="summary")
    start_date: datetime
    end_date: datetime
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    vehicle_id: Optional[str] = None
    route_id: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class TransportReportCreate(TransportReportBase):
    pass


class TransportReport(TransportReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TransportSettingsBase(BaseModel):
    institution_id: Optional[str] = None
    max_students_per_vehicle: int = 40
    allow_overnight_parking: bool = False
    require_driver_break: bool = True
    break_duration_minutes: int = 30
    maintenance_alert_days: int = 7
    insurance_alert_days: int = 30
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": True,
        "push": True
    }


class TransportSettingsCreate(TransportSettingsBase):
    pass


class TransportSettings(TransportSettingsBase):
    id: str
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
