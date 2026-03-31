"""
Disciplinary Committee - API Routes
====================================
FastAPI router for all Disciplinary Committee endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    ComplaintService,
    CaseRecordService,
    ActionService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/disciplinary-committee", tags=["Disciplinary Committee"])


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


@router.post("/complaints", response_model=APIResponse)
async def create_complaint(data: ComplaintCreate):
    try:
        complaint_id = await ComplaintService.create_complaint(data.model_dump())
        return APIResponse(success=True, data={"id": complaint_id}, message="Complaint registered")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complaints", response_model=APIResponse)
async def get_complaints(status: Optional[str] = None, priority: Optional[str] = None):
    try:
        complaints = await ComplaintService.get_all_complaints(status, priority)
        return APIResponse(success=True, data=complaints, count=len(complaints))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complaints/{complaint_id}", response_model=APIResponse)
async def get_complaint(complaint_id: str):
    try:
        complaint = await ComplaintService.get_complaint(complaint_id)
        if not complaint:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=complaint)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/complaints/{complaint_id}", response_model=APIResponse)
async def update_complaint(complaint_id: str, data: ComplaintCreate):
    try:
        updated = await ComplaintService.update_complaint(complaint_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/complaints/{complaint_id}/assign", response_model=APIResponse)
async def assign_complaint(complaint_id: str, assigned_to: str):
    try:
        assigned = await ComplaintService.assign_complaint(complaint_id, assigned_to)
        return APIResponse(success=assigned, message="Assigned" if assigned else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/complaints/{complaint_id}", response_model=APIResponse)
async def delete_complaint(complaint_id: str):
    try:
        deleted = await ComplaintService.delete_complaint(complaint_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/case-records", response_model=APIResponse)
async def create_case_record(data: CaseRecordCreate):
    try:
        case_id = await CaseRecordService.create_case_record(data.model_dump())
        return APIResponse(success=True, data={"id": case_id}, message="Case record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/case-records", response_model=APIResponse)
async def get_case_records(status: Optional[str] = None):
    try:
        records = await CaseRecordService.get_all_case_records(status)
        return APIResponse(success=True, data=records, count=len(records))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/case-records/{case_id}", response_model=APIResponse)
async def get_case_record(case_id: str):
    try:
        record = await CaseRecordService.get_case_record(case_id)
        if not record:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/case-records/complaint/{complaint_id}", response_model=APIResponse)
async def get_case_by_complaint(complaint_id: str):
    try:
        record = await CaseRecordService.get_case_by_complaint(complaint_id)
        if not record:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/case-records/{case_id}", response_model=APIResponse)
async def update_case_record(case_id: str, data: CaseRecordCreate):
    try:
        updated = await CaseRecordService.update_case_record(case_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/case-records/{case_id}", response_model=APIResponse)
async def delete_case_record(case_id: str):
    try:
        deleted = await CaseRecordService.delete_case_record(case_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/actions", response_model=APIResponse)
async def create_action(data: ActionCreate):
    try:
        action_id = await ActionService.create_action(data.model_dump())
        return APIResponse(success=True, data={"id": action_id}, message="Action recorded")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/actions", response_model=APIResponse)
async def get_actions(case_id: Optional[str] = None, status: Optional[str] = None):
    try:
        actions = await ActionService.get_all_actions(case_id, status)
        return APIResponse(success=True, data=actions, count=len(actions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/actions/{action_id}", response_model=APIResponse)
async def get_action(action_id: str):
    try:
        action = await ActionService.get_action(action_id)
        if not action:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=action)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/actions/{action_id}", response_model=APIResponse)
async def update_action(action_id: str, data: ActionCreate):
    try:
        updated = await ActionService.update_action(action_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/actions/{action_id}", response_model=APIResponse)
async def delete_action(action_id: str):
    try:
        deleted = await ActionService.delete_action(action_id)
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


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await ReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings():
    try:
        settings = await SettingsService.get_settings()
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SettingsCreate):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout", response_model=APIResponse)
async def logout():
    return APIResponse(success=True, message="Logged out successfully")


@router.get("/health", response_model=APIResponse)
async def health_check():
    return APIResponse(success=True, data={"status": "healthy"}, message="Service running")
