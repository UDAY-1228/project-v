"""
Placement Cell - API Routes
===========================
FastAPI router for all Placement Cell endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    CompanyService,
    JobDriveService,
    ApplicationService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/placement-cell", tags=["Placement Cell"])


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


@router.post("/companies", response_model=APIResponse)
async def create_company(data: CompanyCreate):
    try:
        company_id = await CompanyService.create_company(data.model_dump())
        return APIResponse(success=True, data={"id": company_id}, message="Company created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/companies", response_model=APIResponse)
async def get_companies(industry: Optional[str] = None, status: Optional[str] = None):
    try:
        companies = await CompanyService.get_all_companies(industry, status)
        return APIResponse(success=True, data=companies, count=len(companies))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/companies/{company_id}", response_model=APIResponse)
async def get_company(company_id: str):
    try:
        company = await CompanyService.get_company(company_id)
        if not company:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/companies/{company_id}", response_model=APIResponse)
async def update_company(company_id: str, data: CompanyCreate):
    try:
        updated = await CompanyService.update_company(company_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/companies/{company_id}", response_model=APIResponse)
async def delete_company(company_id: str):
    try:
        deleted = await CompanyService.delete_company(company_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/job-drives", response_model=APIResponse)
async def create_job_drive(data: JobDriveCreate):
    try:
        drive_id = await JobDriveService.create_job_drive(data.model_dump())
        return APIResponse(success=True, data={"id": drive_id}, message="Job drive created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/job-drives", response_model=APIResponse)
async def get_job_drives(
    status: Optional[str] = None,
    company_id: Optional[str] = None,
    limit: int = Query(100, ge=1, le=500)
):
    try:
        drives = await JobDriveService.get_all_job_drives(status, company_id, limit)
        return APIResponse(success=True, data=drives, count=len(drives))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/job-drives/{drive_id}", response_model=APIResponse)
async def get_job_drive(drive_id: str):
    try:
        drive = await JobDriveService.get_job_drive(drive_id)
        if not drive:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=drive)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/job-drives/{drive_id}", response_model=APIResponse)
async def update_job_drive(drive_id: str, data: JobDriveCreate):
    try:
        updated = await JobDriveService.update_job_drive(drive_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/job-drives/{drive_id}", response_model=APIResponse)
async def delete_job_drive(drive_id: str):
    try:
        deleted = await JobDriveService.delete_job_drive(drive_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/applications", response_model=APIResponse)
async def create_application(data: ApplicationCreate):
    try:
        app_id = await ApplicationService.create_application(data.model_dump())
        return APIResponse(success=True, data={"id": app_id}, message="Application submitted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/applications", response_model=APIResponse)
async def get_applications(
    student_id: Optional[str] = None,
    drive_id: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = Query(200, ge=1, le=500)
):
    try:
        applications = await ApplicationService.get_all_applications(student_id, drive_id, status, limit)
        return APIResponse(success=True, data=applications, count=len(applications))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/applications/{application_id}", response_model=APIResponse)
async def get_application(application_id: str):
    try:
        application = await ApplicationService.get_application(application_id)
        if not application:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=application)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/applications/{application_id}", response_model=APIResponse)
async def update_application(application_id: str, data: ApplicationUpdate):
    try:
        updated = await ApplicationService.update_application(application_id, data.model_dump(exclude_none=True))
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/applications/{application_id}", response_model=APIResponse)
async def delete_application(application_id: str):
    try:
        deleted = await ApplicationService.delete_application(application_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/applications/bulk-update", response_model=APIResponse)
async def bulk_update_applications(application_ids: List[str], status: str):
    try:
        count = await ApplicationService.bulk_update_status(application_ids, status)
        return APIResponse(success=True, data={"count": count}, message=f"Updated {count} applications")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: PlacementReportCreate):
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None, academic_year: Optional[str] = None):
    try:
        reports = await ReportService.get_all_reports(report_type, academic_year)
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
async def update_settings(data: PlacementSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
