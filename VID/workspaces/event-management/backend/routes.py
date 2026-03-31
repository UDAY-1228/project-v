"""
Event Management - API Routes
=============================
FastAPI router for all Event Management endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService, EventService, RegistrationService,
    ScheduleService, ReportService, EventSettingsService,
)

router = APIRouter(prefix="/event-management", tags=["Event Management"])


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


@router.post("/events", response_model=APIResponse)
async def create_event(data: EventCreate):
    try:
        event_id = await EventService.create_event(data.model_dump())
        return APIResponse(success=True, data={"id": event_id}, message="Event created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events", response_model=APIResponse)
async def get_events(status: Optional[str] = None, event_type: Optional[str] = None):
    try:
        events = await EventService.get_all_events(status, event_type)
        return APIResponse(success=True, data=events, count=len(events))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events/{event_id}", response_model=APIResponse)
async def get_event(event_id: str):
    try:
        event = await EventService.get_event(event_id)
        if not event:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/events/{event_id}", response_model=APIResponse)
async def update_event(event_id: str, data: EventCreate):
    try:
        updated = await EventService.update_event(event_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/events/{event_id}", response_model=APIResponse)
async def delete_event(event_id: str):
    try:
        deleted = await EventService.delete_event(event_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/events/{event_id}/publish", response_model=APIResponse)
async def publish_event(event_id: str):
    try:
        published = await EventService.publish_event(event_id)
        return APIResponse(success=published, message="Event published" if published else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/registrations", response_model=APIResponse)
async def create_registration(data: RegistrationCreate):
    try:
        registration_id = await RegistrationService.register_participant(data.model_dump())
        return APIResponse(success=True, data={"id": registration_id}, message="Registration successful")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/registrations", response_model=APIResponse)
async def get_registrations(event_id: Optional[str] = None):
    try:
        registrations = await RegistrationService.get_registrations(event_id)
        return APIResponse(success=True, data=registrations, count=len(registrations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/registrations/{registration_id}", response_model=APIResponse)
async def get_registration(registration_id: str):
    try:
        registration = await RegistrationService.get_registration(registration_id)
        if not registration:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=registration)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/registrations/{registration_id}/check-in", response_model=APIResponse)
async def check_in_participant(registration_id: str):
    try:
        checked = await RegistrationService.check_in_participant(registration_id)
        return APIResponse(success=checked, message="Participant checked in" if checked else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/registrations/{registration_id}", response_model=APIResponse)
async def delete_registration(registration_id: str):
    try:
        deleted = await RegistrationService.delete_registration(registration_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/schedules", response_model=APIResponse)
async def create_schedule(data: ScheduleCreate):
    try:
        schedule_id = await ScheduleService.create_schedule(data.model_dump())
        return APIResponse(success=True, data={"id": schedule_id}, message="Schedule created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/schedules/{event_id}", response_model=APIResponse)
async def get_schedules(event_id: str):
    try:
        schedules = await ScheduleService.get_schedules(event_id)
        return APIResponse(success=True, data=schedules, count=len(schedules))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/schedules/{schedule_id}", response_model=APIResponse)
async def update_schedule(schedule_id: str, data: ScheduleCreate):
    try:
        updated = await ScheduleService.update_schedule(schedule_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/schedules/{schedule_id}", response_model=APIResponse)
async def delete_schedule(schedule_id: str):
    try:
        deleted = await ScheduleService.delete_schedule(schedule_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: ReportCreate):
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None):
    try:
        reports = await ReportService.get_all_reports(report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    try:
        report = await ReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await ReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{event_id}/generate", response_model=APIResponse)
async def generate_event_report(event_id: str):
    try:
        report = await ReportService.generate_event_report(event_id)
        return APIResponse(success=True, data=report, message="Report generated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings():
    try:
        settings = await EventSettingsService.get_settings()
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: EventSettingsCreate):
    try:
        settings_id = await EventSettingsService.upsert_settings(data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout", response_model=APIResponse)
async def logout():
    try:
        return APIResponse(success=True, message="Logged out successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
