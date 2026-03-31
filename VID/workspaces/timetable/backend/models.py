"""
Timetable - Pydantic Models
============================
Pydantic models for the Timetable workspace.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ScheduleBase(BaseModel):
    name: str
    academic_year: str
    semester: str
    class_id: str


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(BaseModel):
    name: Optional[str] = None
    academic_year: Optional[str] = None
    semester: Optional[str] = None
    class_id: Optional[str] = None
    slots: Optional[List[dict]] = None


class Schedule(ScheduleBase):
    id: str = Field(alias="_id")
    slots: List[dict] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class ClassAllocationBase(BaseModel):
    class_id: str
    class_name: str
    department: str
    year: int
    section: Optional[str] = None


class ClassAllocationCreate(ClassAllocationBase):
    pass


class ClassAllocationUpdate(BaseModel):
    class_name: Optional[str] = None
    department: Optional[str] = None
    year: Optional[int] = None
    section: Optional[str] = None


class ClassAllocation(ClassAllocationBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class RoomAllocationBase(BaseModel):
    room_number: str
    building: str
    capacity: int
    room_type: str
    amenities: Optional[List[str]] = None


class RoomAllocationCreate(RoomAllocationBase):
    pass


class RoomAllocationUpdate(BaseModel):
    room_number: Optional[str] = None
    building: Optional[str] = None
    capacity: Optional[int] = None
    room_type: Optional[str] = None
    amenities: Optional[List[str]] = None


class RoomAllocation(RoomAllocationBase):
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


class TimeSlotBase(BaseModel):
    day: str
    start_time: str
    end_time: str
    subject: str
    faculty: str
    room_id: str
    class_id: str


class TimeSlotCreate(TimeSlotBase):
    pass


class TimeSlotUpdate(BaseModel):
    day: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    subject: Optional[str] = None
    faculty: Optional[str] = None
    room_id: Optional[str] = None
    class_id: Optional[str] = None


class DashboardStats(BaseModel):
    total_schedules: int
    total_classes: int
    total_rooms: int
    total_slots: int
