"""
Timetable - FastAPI Routes
=========================
API endpoints for the Timetable workspace.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from . import models
from . import services

router = APIRouter(prefix="/api/timetable", tags=["Timetable"])


@router.get("/dashboard", response_model=models.DashboardStats)
async def get_dashboard():
    """Get dashboard statistics."""
    return await services.DashboardService.get_stats()


@router.get("/dashboard/stats", response_model=models.DashboardStats)
async def get_dashboard_stats():
    """Get dashboard statistics (alias)."""
    return await services.DashboardService.get_stats()


@router.post("/schedules", response_model=models.Schedule)
async def create_schedule(schedule: models.ScheduleCreate):
    """Create a new schedule."""
    return await services.ScheduleService.create(schedule.model_dump())


@router.get("/schedules", response_model=List[models.Schedule])
async def get_all_schedules():
    """Get all schedules."""
    return await services.ScheduleService.get_all()


@router.get("/schedules/{schedule_id}", response_model=models.Schedule)
async def get_schedule(schedule_id: str):
    """Get schedule by ID."""
    schedule = await services.ScheduleService.get_by_id(schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


@router.put("/schedules/{schedule_id}", response_model=models.Schedule)
async def update_schedule(schedule_id: str, schedule: models.ScheduleUpdate):
    """Update a schedule."""
    updated = await services.ScheduleService.update(schedule_id, schedule.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated


@router.delete("/schedules/{schedule_id}")
async def delete_schedule(schedule_id: str):
    """Delete a schedule."""
    deleted = await services.ScheduleService.delete(schedule_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"message": "Schedule deleted successfully"}


@router.post("/class-allocations", response_model=models.ClassAllocation)
async def create_class_allocation(allocation: models.ClassAllocationCreate):
    """Create a new class allocation."""
    return await services.ClassAllocationService.create(allocation.model_dump())


@router.get("/class-allocations", response_model=List[models.ClassAllocation])
async def get_all_class_allocations():
    """Get all class allocations."""
    return await services.ClassAllocationService.get_all()


@router.get("/class-allocations/{allocation_id}", response_model=models.ClassAllocation)
async def get_class_allocation(allocation_id: str):
    """Get class allocation by ID."""
    allocation = await services.ClassAllocationService.get_by_id(allocation_id)
    if not allocation:
        raise HTTPException(status_code=404, detail="Class allocation not found")
    return allocation


@router.get("/class-allocations/class/{class_id}", response_model=models.ClassAllocation)
async def get_class_allocation_by_class(class_id: str):
    """Get class allocation by class ID."""
    allocation = await services.ClassAllocationService.get_by_class(class_id)
    if not allocation:
        raise HTTPException(status_code=404, detail="Class allocation not found")
    return allocation


@router.put("/class-allocations/{allocation_id}", response_model=models.ClassAllocation)
async def update_class_allocation(allocation_id: str, allocation: models.ClassAllocationUpdate):
    """Update a class allocation."""
    updated = await services.ClassAllocationService.update(allocation_id, allocation.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Class allocation not found")
    return updated


@router.delete("/class-allocations/{allocation_id}")
async def delete_class_allocation(allocation_id: str):
    """Delete a class allocation."""
    deleted = await services.ClassAllocationService.delete(allocation_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Class allocation not found")
    return {"message": "Class allocation deleted successfully"}


@router.post("/room-allocations", response_model=models.RoomAllocation)
async def create_room_allocation(allocation: models.RoomAllocationCreate):
    """Create a new room allocation."""
    return await services.RoomAllocationService.create(allocation.model_dump())


@router.get("/room-allocations", response_model=List[models.RoomAllocation])
async def get_all_room_allocations():
    """Get all room allocations."""
    return await services.RoomAllocationService.get_all()


@router.get("/room-allocations/{room_id}", response_model=models.RoomAllocation)
async def get_room_allocation(room_id: str):
    """Get room allocation by ID."""
    allocation = await services.RoomAllocationService.get_by_id(room_id)
    if not allocation:
        raise HTTPException(status_code=404, detail="Room allocation not found")
    return allocation


@router.put("/room-allocations/{room_id}", response_model=models.RoomAllocation)
async def update_room_allocation(room_id: str, allocation: models.RoomAllocationUpdate):
    """Update a room allocation."""
    updated = await services.RoomAllocationService.update(room_id, allocation.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Room allocation not found")
    return updated


@router.delete("/room-allocations/{room_id}")
async def delete_room_allocation(room_id: str):
    """Delete a room allocation."""
    deleted = await services.RoomAllocationService.delete(room_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Room allocation not found")
    return {"message": "Room allocation deleted successfully"}


@router.post("/reports", response_model=models.Report)
async def create_report(report: models.ReportCreate):
    """Create a new report."""
    return await services.ReportService.create(report.model_dump())


@router.get("/reports", response_model=List[models.Report])
async def get_all_reports():
    """Get all reports."""
    return await services.ReportService.get_all()


@router.get("/reports/type/{report_type}", response_model=List[models.Report])
async def get_reports_by_type(report_type: str):
    """Get reports by type."""
    return await services.ReportService.get_by_type(report_type)


@router.get("/settings")
async def get_settings():
    """Get settings."""
    settings = await services.SettingsService.get()
    if not settings:
        return {"academic_year": "2025-2026", "semester": "Semester 1", "week_start_day": "Monday"}
    return settings


@router.put("/settings")
async def update_settings(settings: dict):
    """Update settings."""
    return await services.SettingsService.update(settings)


@router.post("/logout")
async def logout():
    """Logout endpoint."""
    return {"message": "Logged out successfully"}
