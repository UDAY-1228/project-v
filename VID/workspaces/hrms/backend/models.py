"""
HRMS - Models
=============
Pydantic models for the HRMS workspace.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class EmploymentStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ON_LEAVE = "on_leave"
    TERMINATED = "terminated"


class EmploymentType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERN = "intern"


class LeaveType(str, Enum):
    SICK = "sick"
    CASUAL = "casual"
    ANNUAL = "annual"
    MATERNITY = "maternity"
    PATERNITY = "paternity"
    UNPAID = "unpaid"


class LeaveStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    HALF_DAY = "half_day"


class RecruitmentStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    ON_HOLD = "on_hold"


class ApplicationStatus(str, Enum):
    NEW = "new"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFERED = "offered"
    HIRED = "hired"
    REJECTED = "rejected"


class EmployeeBase(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: Optional[date] = None
    gender: Optional[Gender] = None
    address: Optional[str] = None
    department: str
    designation: str
    employment_type: EmploymentType = EmploymentType.FULL_TIME
    joining_date: date
    salary: Optional[float] = None
    status: EmploymentStatus = EmploymentStatus.ACTIVE


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[Gender] = None
    address: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    employment_type: Optional[EmploymentType] = None
    salary: Optional[float] = None
    status: Optional[EmploymentStatus] = None


class Employee(EmployeeBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    class Config:
        populate_by_name = True


class AttendanceRecord(BaseModel):
    employee_id: str
    date: date
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    status: AttendanceStatus
    overtime_hours: float = 0
    notes: Optional[str] = None


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    status: AttendanceStatus
    overtime_hours: float = 0
    notes: Optional[str] = None


class AttendanceUpdate(BaseModel):
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    status: Optional[AttendanceStatus] = None
    overtime_hours: Optional[float] = None
    notes: Optional[str] = None


class LeaveRequest(BaseModel):
    employee_id: str
    leave_type: LeaveType
    start_date: date
    end_date: date
    reason: str
    status: LeaveStatus = LeaveStatus.PENDING
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    notes: Optional[str] = None


class LeaveRequestCreate(BaseModel):
    employee_id: str
    leave_type: LeaveType
    start_date: date
    end_date: date
    reason: str


class LeaveRequestUpdate(BaseModel):
    status: LeaveStatus
    approved_by: Optional[str] = None
    notes: Optional[str] = None


class PayrollRecord(BaseModel):
    employee_id: str
    month: int
    year: int
    basic_salary: float
    allowances: float = 0
    deductions: float = 0
    overtime_pay: float = 0
    bonuses: float = 0
    tax: float = 0
    net_salary: float
    payment_date: Optional[datetime] = None
    status: str = "pending"


class PayrollCreate(BaseModel):
    employee_id: str
    month: int
    year: int
    basic_salary: float
    allowances: float = 0
    deductions: float = 0
    overtime_pay: float = 0
    bonuses: float = 0
    tax: float = 0


class PayrollUpdate(BaseModel):
    allowances: Optional[float] = None
    deductions: Optional[float] = None
    overtime_pay: Optional[float] = None
    bonuses: Optional[float] = None
    tax: Optional[float] = None
    status: Optional[str] = None


class Position(BaseModel):
    title: str
    department: str
    description: str
    requirements: List[str] = []
    salary_range_min: Optional[float] = None
    salary_range_max: Optional[float] = None
    status: RecruitmentStatus = RecruitmentStatus.OPEN
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PositionCreate(BaseModel):
    title: str
    department: str
    description: str
    requirements: List[str] = []
    salary_range_min: Optional[float] = None
    salary_range_max: Optional[float] = None


class PositionUpdate(BaseModel):
    title: Optional[str] = None
    department: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[List[str]] = None
    salary_range_min: Optional[float] = None
    salary_range_max: Optional[float] = None
    status: Optional[RecruitmentStatus] = None


class JobApplication(BaseModel):
    position_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    resume_url: Optional[str] = None
    cover_letter: Optional[str] = None
    status: ApplicationStatus = ApplicationStatus.NEW
    interview_date: Optional[datetime] = None
    interview_notes: Optional[str] = None
    applied_at: datetime = Field(default_factory=datetime.utcnow)


class JobApplicationCreate(BaseModel):
    position_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    resume_url: Optional[str] = None
    cover_letter: Optional[str] = None


class JobApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus] = None
    interview_date: Optional[datetime] = None
    interview_notes: Optional[str] = None


class DashboardStats(BaseModel):
    total_employees: int
    active_employees: int
    present_today: int
    on_leave: int
    pending_payroll: int
    open_positions: int
    new_applications: int
    recent_hires: int


class ReportFilters(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    department: Optional[str] = None
    report_type: str


class SystemSettings(BaseModel):
    company_name: str = "Organization"
    working_hours_start: str = "09:00"
    working_hours_end: str = "17:00"
    late_threshold_minutes: int = 15
    overtime_rate: float = 1.5
    casual_leave_limit: int = 12
    sick_leave_limit: int = 10
    annual_leave_limit: int = 20
