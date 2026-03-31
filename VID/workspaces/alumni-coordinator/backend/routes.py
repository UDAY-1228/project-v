"""
Alumni Coordinator - API Routes
================================
FastAPI router for all Alumni Coordinator endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    AlumniRecordsService,
    EventsService,
    CommunicationService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/alumni-coordinator", tags=["Alumni Coordinator"])


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


@router.post("/alumni", response_model=APIResponse)
async def create_alumni(data: AlumniRecordCreate):
    try:
        alumni_id = await AlumniRecordsService.create_alumni(data.model_dump())
        return APIResponse(success=True, data={"id": alumni_id}, message="Alumni record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni", response_model=APIResponse)
async def get_alumni(department: Optional[str] = None, graduation_year: Optional[int] = None):
    try:
        alumni = await AlumniRecordsService.get_all_alumni(department, graduation_year)
        return APIResponse(success=True, data=alumni, count=len(alumni))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni/search", response_model=APIResponse)
async def search_alumni(query: str = Query(..., min_length=1)):
    try:
        results = await AlumniRecordsService.search_alumni(query)
        return APIResponse(success=True, data=results, count=len(results))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni/{alumni_id}", response_model=APIResponse)
async def get_alumni_record(alumni_id: str):
    try:
        alumni = await AlumniRecordsService.get_alumni(alumni_id)
        if not alumni:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=alumni)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/alumni/{alumni_id}", response_model=APIResponse)
async def update_alumni(alumni_id: str, data: AlumniRecordCreate):
    try:
        updated = await AlumniRecordsService.update_alumni(alumni_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/alumni/{alumni_id}", response_model=APIResponse)
async def delete_alumni(alumni_id: str):
    try:
        deleted = await AlumniRecordsService.delete_alumni(alumni_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/events", response_model=APIResponse)
async def create_event(data: EventCreate):
    try:
        event_id = await EventsService.create_event(data.model_dump())
        return APIResponse(success=True, data={"id": event_id}, message="Event created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events", response_model=APIResponse)
async def get_events(status: Optional[str] = None):
    try:
        events = await EventsService.get_all_events(status)
        return APIResponse(success=True, data=events, count=len(events))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events/{event_id}", response_model=APIResponse)
async def get_event(event_id: str):
    try:
        event = await EventsService.get_event(event_id)
        if not event:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/events/{event_id}", response_model=APIResponse)
async def update_event(event_id: str, data: EventCreate):
    try:
        updated = await EventsService.update_event(event_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/events/{event_id}", response_model=APIResponse)
async def delete_event(event_id: str):
    try:
        deleted = await EventsService.delete_event(event_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/events/{event_id}/register", response_model=APIResponse)
async def register_attendee(event_id: str, data: EventRegistration):
    try:
        reg_id = await EventsService.register_attendee(event_id, data.model_dump())
        return APIResponse(success=True, data={"id": reg_id}, message="Registration successful")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events/{event_id}/registrations", response_model=APIResponse)
async def get_event_registrations(event_id: str):
    try:
        registrations = await EventsService.get_registrations(event_id)
        return APIResponse(success=True, data=registrations, count=len(registrations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/communications", response_model=APIResponse)
async def create_communication(data: CommunicationCreate):
    try:
        comm_id = await CommunicationService.create_communication(data.model_dump())
        return APIResponse(success=True, data={"id": comm_id}, message="Communication created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/communications", response_model=APIResponse)
async def get_communications(status: Optional[str] = None):
    try:
        comms = await CommunicationService.get_all_communications(status)
        return APIResponse(success=True, data=comms, count=len(comms))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/communications/{comm_id}", response_model=APIResponse)
async def get_communication(comm_id: str):
    try:
        comm = await CommunicationService.get_communication(comm_id)
        if not comm:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=comm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/communications/{comm_id}", response_model=APIResponse)
async def update_communication(comm_id: str, data: CommunicationCreate):
    try:
        updated = await CommunicationService.update_communication(comm_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/communications/{comm_id}", response_model=APIResponse)
async def delete_communication(comm_id: str):
    try:
        deleted = await CommunicationService.delete_communication(comm_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/communications/{comm_id}/send", response_model=APIResponse)
async def send_communication(comm_id: str):
    try:
        sent = await CommunicationService.send_communication(comm_id)
        return APIResponse(success=sent, message="Sent" if sent else "Failed")
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


@router.get("/settings", response_model=APIResponse)
async def get_settings(institution_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
