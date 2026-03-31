"""
Employee - API Routes
====================
FastAPI router for all Employee endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService, AttendanceService, TaskService,
    LeaveRequestService, ProfileService, SettingsService,
)

router = APIRouter(prefix="/employee", tags=["Employee"])


@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats():
    try:
        stats = await DashboardService.get_stats()
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(limit: int = Query(10, ge=1, le=50)):
    try:
        activities = await DashboardService.get_recent_activity(limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/attendance/check-in", response_model=APIResponse)
async def check_in(employee_id: str):
    try:
        record_id = await AttendanceService.check_in(employee_id)
        return APIResponse(success=True, data={"id": record_id}, message="Checked in successfully")
    except ValueError as e:
        return APIResponse(success=False, error=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/attendance/check-out", response_model=APIResponse)
async def check_out(employee_id: str):
    try:
        success = await AttendanceService.check_out(employee_id)
        return APIResponse(success=success, message="Checked out" if success else "No check-in found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance/records", response_model=APIResponse)
async def get_attendance_records(employee_id: str, month: Optional[int] = None):
    try:
        records = await AttendanceService.get_attendance_records(employee_id, month)
        return APIResponse(success=True, data=records, count=len(records))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tasks", response_model=APIResponse)
async def create_task(data: TaskCreate):
    try:
        task_id = await TaskService.create_task(data.model_dump())
        return APIResponse(success=True, data={"id": task_id}, message="Task created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tasks", response_model=APIResponse)
async def get_tasks(employee_id: Optional[str] = None):
    try:
        tasks = await TaskService.get_all_tasks(employee_id)
        return APIResponse(success=True, data=tasks, count=len(tasks))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tasks/{task_id}", response_model=APIResponse)
async def get_task(task_id: str):
    try:
        task = await TaskService.get_task(task_id)
        if not task:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/tasks/{task_id}", response_model=APIResponse)
async def update_task(task_id: str, data: TaskUpdate):
    try:
        updated = await TaskService.update_task(task_id, data.model_dump(exclude_none=True))
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/tasks/{task_id}", response_model=APIResponse)
async def delete_task(task_id: str):
    try:
        deleted = await TaskService.delete_task(task_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/leave-requests", response_model=APIResponse)
async def create_leave_request(data: LeaveRequestCreate):
    try:
        request_id = await LeaveRequestService.create_leave_request(data.model_dump())
        return APIResponse(success=True, data={"id": request_id}, message="Leave request created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/leave-requests", response_model=APIResponse)
async def get_leave_requests(employee_id: Optional[str] = None):
    try:
        requests = await LeaveRequestService.get_all_leave_requests(employee_id)
        return APIResponse(success=True, data=requests, count=len(requests))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/leave-requests/{request_id}", response_model=APIResponse)
async def get_leave_request(request_id: str):
    try:
        request = await LeaveRequestService.get_leave_request(request_id)
        if not request:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/leave-balance/{employee_id}", response_model=APIResponse)
async def get_leave_balance(employee_id: str):
    try:
        balance = await LeaveRequestService.get_leave_balance(employee_id)
        return APIResponse(success=True, data=balance)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/profile/{employee_id}", response_model=APIResponse)
async def get_profile(employee_id: str):
    try:
        profile = await ProfileService.get_profile(employee_id)
        if not profile:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile", response_model=APIResponse)
async def create_profile(data: ProfileCreate):
    try:
        profile_id = await ProfileService.create_profile(data.model_dump())
        return APIResponse(success=True, data={"id": profile_id}, message="Profile created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/profile/{employee_id}", response_model=APIResponse)
async def update_profile(employee_id: str, data: ProfileCreate):
    try:
        updated = await ProfileService.update_profile(employee_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings/{employee_id}", response_model=APIResponse)
async def get_settings(employee_id: str):
    try:
        settings = await SettingsService.get_settings(employee_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings/{employee_id}", response_model=APIResponse)
async def update_settings(employee_id: str, data: EmployeeSettingsCreate):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), employee_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout", response_model=APIResponse)
async def logout():
    try:
        return APIResponse(success=True, message="Logged out successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
