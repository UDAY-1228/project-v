"""
HRMS - Controllers
===================
Request handlers for the HRMS workspace.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from datetime import date, datetime

from .models import (
    EmployeeCreate, EmployeeUpdate, Employee,
    AttendanceCreate, AttendanceUpdate, AttendanceRecord,
    LeaveRequestCreate, LeaveRequestUpdate, LeaveRequest,
    PayrollCreate, PayrollUpdate, PayrollRecord,
    PositionCreate, PositionUpdate, Position,
    JobApplicationCreate, JobApplicationUpdate, JobApplication,
    DashboardStats, ReportFilters, SystemSettings
)
from . import services

router = APIRouter(prefix="/api/hrms", tags=["HRMS"])


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "hrms"}


@router.get("/dashboard/stats", response_model=DashboardStats)
async def get_dashboard_stats():
    total_employees = await services.EmployeeService.count_employees()
    active_employees = await services.EmployeeService.count_employees(status="active")
    present_today = await services.AttendanceService.get_present_today()
    on_leave = await services.LeaveService.get_on_leave_count()
    pending_payroll = await services.PayrollService.get_pending_payroll_count()
    open_positions = await services.RecruitmentService.get_open_positions_count()
    new_applications = await services.ApplicationService.get_new_applications_count()
    
    thirty_days_ago = date.today().replace(day=max(1, date.today().day - 30))
    recent_hires = await services.EmployeeService.count_employees_joined_after(thirty_days_ago)
    
    return DashboardStats(
        total_employees=total_employees,
        active_employees=active_employees,
        present_today=present_today,
        on_leave=on_leave,
        pending_payroll=pending_payroll,
        open_positions=open_positions,
        new_applications=new_applications,
        recent_hires=recent_hires
    )


@router.post("/employees", response_model=dict)
async def create_employee(employee: EmployeeCreate):
    employee_dict = employee.model_dump()
    result = await services.EmployeeService.create_employee(employee_dict)
    return result


@router.get("/employees", response_model=List[dict])
async def get_all_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    department: Optional[str] = None,
    status: Optional[str] = None
):
    return await services.EmployeeService.get_all_employees(skip, limit, department, status)


@router.get("/employees/{employee_id}", response_model=dict)
async def get_employee(employee_id: str):
    employee = await services.EmployeeService.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/employees/{employee_id}", response_model=dict)
async def update_employee(employee_id: str, employee: EmployeeUpdate):
    update_data = {k: v for k, v in employee.model_dump().items() if v is not None}
    result = await services.EmployeeService.update_employee(employee_id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result


@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: str):
    success = await services.EmployeeService.delete_employee(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@router.post("/attendance", response_model=dict)
async def create_attendance(attendance: AttendanceCreate):
    attendance_dict = attendance.model_dump()
    if isinstance(attendance_dict.get("date"), date):
        attendance_dict["date"] = attendance_dict["date"].isoformat()
    return await services.AttendanceService.create_attendance(attendance_dict)


@router.get("/attendance", response_model=List[dict])
async def get_attendance_records(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    employee_id: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    return await services.AttendanceService.get_attendance_records(skip, limit, employee_id, start_date, end_date)


@router.get("/attendance/{id}", response_model=dict)
async def get_attendance(id: str):
    attendance = await services.AttendanceService.get_attendance_by_id(id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance


@router.put("/attendance/{id}", response_model=dict)
async def update_attendance(id: str, attendance: AttendanceUpdate):
    update_data = {k: v for k, v in attendance.model_dump().items() if v is not None}
    result = await services.AttendanceService.update_attendance(id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return result


@router.delete("/attendance/{id}")
async def delete_attendance(id: str):
    success = await services.AttendanceService.delete_attendance(id)
    if not success:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return {"message": "Attendance record deleted successfully"}


@router.post("/leaves", response_model=dict)
async def create_leave_request(leave: LeaveRequestCreate):
    leave_dict = leave.model_dump()
    leave_dict["status"] = "pending"
    leave_dict["start_date"] = leave_dict["start_date"].isoformat()
    leave_dict["end_date"] = leave_dict["end_date"].isoformat()
    return await services.LeaveService.create_leave_request(leave_dict)


@router.get("/leaves", response_model=List[dict])
async def get_leave_requests(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    employee_id: Optional[str] = None,
    status: Optional[str] = None
):
    return await services.LeaveService.get_leave_requests(skip, limit, employee_id, status)


@router.get("/leaves/{id}", response_model=dict)
async def get_leave_request(id: str):
    leave = await services.LeaveService.get_leave_request(id)
    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return leave


@router.put("/leaves/{id}", response_model=dict)
async def update_leave_request(id: str, leave: LeaveRequestUpdate):
    update_data = leave.model_dump()
    result = await services.LeaveService.update_leave_request(id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return result


@router.delete("/leaves/{id}")
async def delete_leave_request(id: str):
    success = await services.LeaveService.delete_leave_request(id)
    if not success:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return {"message": "Leave request deleted successfully"}


@router.post("/payroll", response_model=dict)
async def create_payroll(payroll: PayrollCreate):
    payroll_dict = payroll.model_dump()
    return await services.PayrollService.create_payroll(payroll_dict)


@router.get("/payroll", response_model=List[dict])
async def get_payroll_records(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    employee_id: Optional[str] = None,
    month: Optional[int] = None,
    year: Optional[int] = None
):
    return await services.PayrollService.get_payroll_records(skip, limit, employee_id, month, year)


@router.get("/payroll/{id}", response_model=dict)
async def get_payroll(id: str):
    payroll = await services.PayrollService.get_payroll(id)
    if not payroll:
        raise HTTPException(status_code=404, detail="Payroll record not found")
    return payroll


@router.put("/payroll/{id}", response_model=dict)
async def update_payroll(id: str, payroll: PayrollUpdate):
    update_data = {k: v for k, v in payroll.model_dump().items() if v is not None}
    result = await services.PayrollService.update_payroll(id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Payroll record not found")
    return result


@router.delete("/payroll/{id}")
async def delete_payroll(id: str):
    success = await services.PayrollService.delete_payroll(id)
    if not success:
        raise HTTPException(status_code=404, detail="Payroll record not found")
    return {"message": "Payroll record deleted successfully"}


@router.post("/recruitment/positions", response_model=dict)
async def create_position(position: PositionCreate):
    position_dict = position.model_dump()
    return await services.RecruitmentService.create_position(position_dict)


@router.get("/recruitment/positions", response_model=List[dict])
async def get_positions(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    department: Optional[str] = None,
    status: Optional[str] = None
):
    return await services.RecruitmentService.get_positions(skip, limit, department, status)


@router.get("/recruitment/positions/{id}", response_model=dict)
async def get_position(id: str):
    position = await services.RecruitmentService.get_position(id)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return position


@router.put("/recruitment/positions/{id}", response_model=dict)
async def update_position(id: str, position: PositionUpdate):
    update_data = {k: v for k, v in position.model_dump().items() if v is not None}
    result = await services.RecruitmentService.update_position(id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Position not found")
    return result


@router.delete("/recruitment/positions/{id}")
async def delete_position(id: str):
    success = await services.RecruitmentService.delete_position(id)
    if not success:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"message": "Position deleted successfully"}


@router.post("/recruitment/applications", response_model=dict)
async def create_application(application: JobApplicationCreate):
    application_dict = application.model_dump()
    return await services.ApplicationService.create_application(application_dict)


@router.get("/recruitment/applications", response_model=List[dict])
async def get_applications(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    position_id: Optional[str] = None,
    status: Optional[str] = None
):
    return await services.ApplicationService.get_applications(skip, limit, position_id, status)


@router.get("/recruitment/applications/{id}", response_model=dict)
async def get_application(id: str):
    application = await services.ApplicationService.get_application(id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@router.put("/recruitment/applications/{id}", response_model=dict)
async def update_application(id: str, application: JobApplicationUpdate):
    update_data = {k: v for k, v in application.model_dump().items() if v is not None}
    result = await services.ApplicationService.update_application(id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Application not found")
    return result


@router.delete("/recruitment/applications/{id}")
async def delete_application(id: str):
    success = await services.ApplicationService.delete_application(id)
    if not success:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"message": "Application deleted successfully"}


@router.get("/reports/employees")
async def get_employee_report(
    department: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    return await services.ReportsService.get_employee_report(department, start_date, end_date)


@router.get("/reports/attendance")
async def get_attendance_report(
    start_date: date,
    end_date: date,
    department: Optional[str] = None
):
    return await services.ReportsService.get_attendance_report(start_date, end_date, department)


@router.get("/settings", response_model=dict)
async def get_settings():
    return await services.SettingsService.get_settings()


@router.put("/settings", response_model=dict)
async def update_settings(settings: SystemSettings):
    settings_dict = settings.model_dump()
    return await services.SettingsService.update_settings(settings_dict)
