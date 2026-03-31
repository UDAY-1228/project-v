"""
Examination - Pydantic Models
=============================
Pydantic models for the Examination workspace.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ExamBase(BaseModel):
    name: str
    subject: str
    class_level: str
    duration_minutes: int
    total_marks: int
    passing_marks: int


class ExamCreate(ExamBase):
    pass


class ExamUpdate(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None
    class_level: Optional[str] = None
    duration_minutes: Optional[int] = None
    total_marks: Optional[int] = None
    passing_marks: Optional[int] = None
    is_active: Optional[bool] = None


class Exam(ExamBase):
    id: str = Field(alias="_id")
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class ExamScheduleBase(BaseModel):
    exam_id: str
    date: datetime
    start_time: str
    end_time: str
    venue: str
    invigilator: Optional[str] = None


class ExamScheduleCreate(ExamScheduleBase):
    pass


class ExamScheduleUpdate(BaseModel):
    date: Optional[datetime] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    venue: Optional[str] = None
    invigilator: Optional[str] = None


class ExamSchedule(ExamScheduleBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class HallTicketBase(BaseModel):
    student_id: str
    exam_schedule_id: str
    seat_number: str


class HallTicketCreate(HallTicketBase):
    pass


class HallTicketUpdate(BaseModel):
    seat_number: Optional[str] = None
    status: Optional[str] = None


class HallTicket(HallTicketBase):
    id: str = Field(alias="_id")
    status: str = "issued"
    issued_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class ResultBase(BaseModel):
    student_id: str
    exam_id: str
    marks_obtained: float
    grade: str
    remarks: Optional[str] = None


class ResultCreate(ResultBase):
    pass


class ResultUpdate(BaseModel):
    marks_obtained: Optional[float] = None
    grade: Optional[str] = None
    remarks: Optional[str] = None


class Result(ResultBase):
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
    total_exams: int
    upcoming_schedules: int
    hall_tickets_issued: int
    results_declared: int


class SettingsUpdate(BaseModel):
    exam_name: Optional[str] = None
    passing_percentage: Optional[float] = None
    notification_enabled: Optional[bool] = None
