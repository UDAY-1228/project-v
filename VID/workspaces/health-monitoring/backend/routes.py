"""
Health Monitoring - API Routes
==============================
FastAPI router for all Health Monitoring endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    HealthRecordService,
    MedicalReportService,
    AlertService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/health-monitoring", tags=["Health Monitoring"])


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


@router.post("/health-records", response_model=APIResponse)
async def create_health_record(data: HealthRecordCreate):
    try:
        record_id = await HealthRecordService.create_record(data.model_dump())
        return APIResponse(success=True, data={"id": record_id}, message="Health record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health-records", response_model=APIResponse)
async def get_health_records(student_id: Optional[str] = None):
    try:
        records = await HealthRecordService.get_all_records(student_id)
        return APIResponse(success=True, data=records, count=len(records))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health-records/{record_id}", response_model=APIResponse)
async def get_health_record(record_id: str):
    try:
        record = await HealthRecordService.get_record(record_id)
        if not record:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/health-records/{record_id}", response_model=APIResponse)
async def update_health_record(record_id: str, data: HealthRecordCreate):
    try:
        updated = await HealthRecordService.update_record(record_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/health-records/{record_id}", response_model=APIResponse)
async def delete_health_record(record_id: str):
    try:
        deleted = await HealthRecordService.delete_record(record_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/medical-reports", response_model=APIResponse)
async def create_medical_report(data: MedicalReportCreate):
    try:
        report_id = await MedicalReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Medical report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/medical-reports", response_model=APIResponse)
async def get_medical_reports(student_id: Optional[str] = None, report_type: Optional[str] = None):
    try:
        reports = await MedicalReportService.get_all_reports(student_id, report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/medical-reports/{report_id}", response_model=APIResponse)
async def get_medical_report(report_id: str):
    try:
        report = await MedicalReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/medical-reports/{report_id}", response_model=APIResponse)
async def update_medical_report(report_id: str, data: MedicalReportCreate):
    try:
        updated = await MedicalReportService.update_report(report_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/medical-reports/{report_id}", response_model=APIResponse)
async def delete_medical_report(report_id: str):
    try:
        deleted = await MedicalReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/alerts", response_model=APIResponse)
async def create_alert(data: AlertCreate):
    try:
        alert_id = await AlertService.create_alert(data.model_dump())
        return APIResponse(success=True, data={"id": alert_id}, message="Alert created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alerts", response_model=APIResponse)
async def get_alerts(severity: Optional[str] = None, status: Optional[str] = None):
    try:
        alerts = await AlertService.get_all_alerts(severity, status)
        return APIResponse(success=True, data=alerts, count=len(alerts))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alerts/{alert_id}", response_model=APIResponse)
async def get_alert(alert_id: str):
    try:
        alert = await AlertService.get_alert(alert_id)
        if not alert:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=alert)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/alerts/{alert_id}", response_model=APIResponse)
async def update_alert(alert_id: str, data: AlertCreate):
    try:
        updated = await AlertService.update_alert(alert_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/alerts/{alert_id}/resolve", response_model=APIResponse)
async def resolve_alert(alert_id: str, resolved_by: str):
    try:
        resolved = await AlertService.resolve_alert(alert_id, resolved_by)
        return APIResponse(success=resolved, message="Alert resolved" if resolved else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/alerts/{alert_id}", response_model=APIResponse)
async def delete_alert(alert_id: str):
    try:
        deleted = await AlertService.delete_alert(alert_id)
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
async def get_settings(institution_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: HealthSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
