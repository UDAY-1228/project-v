"""
Principal Dashboard - API Routes
==================================
FastAPI router for all Principal Dashboard endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    InstitutionOverviewService,
    StaffStatsService,
    StudentStatsService,
    ReportService,
    PolicyService,
    SettingsService,
)

router = APIRouter(prefix="/principal-dashboard", tags=["Principal Dashboard"])


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


@router.post("/institution-overview", response_model=APIResponse)
async def create_institution_overview(data: InstitutionOverviewCreate):
    try:
        overview_id = await InstitutionOverviewService.create_overview(data.model_dump())
        return APIResponse(success=True, data={"id": overview_id}, message="Institution overview created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/institution-overview", response_model=APIResponse)
async def get_institution_overviews():
    try:
        overviews = await InstitutionOverviewService.get_all_overviews()
        return APIResponse(success=True, data=overviews, count=len(overviews))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/institution-overview/{overview_id}", response_model=APIResponse)
async def get_institution_overview(overview_id: str):
    try:
        overview = await InstitutionOverviewService.get_overview(overview_id)
        if not overview:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=overview)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/institution-overview/{overview_id}", response_model=APIResponse)
async def update_institution_overview(overview_id: str, data: InstitutionOverviewCreate):
    try:
        updated = await InstitutionOverviewService.update_overview(overview_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/staff-stats", response_model=APIResponse)
async def create_staff_stats(data: StaffStatsCreate):
    try:
        stats_id = await StaffStatsService.create_stats(data.model_dump())
        return APIResponse(success=True, data={"id": stats_id}, message="Staff stats created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/staff-stats", response_model=APIResponse)
async def get_staff_stats(department_id: Optional[str] = None):
    try:
        if department_id:
            stats = await StaffStatsService.get_stats_by_department(department_id)
        else:
            stats = await StaffStatsService.get_all_stats()
        return APIResponse(success=True, data=stats, count=len(stats))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/staff-stats/{stats_id}", response_model=APIResponse)
async def update_staff_stats(stats_id: str, data: StaffStatsCreate):
    try:
        updated = await StaffStatsService.update_stats(stats_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/staff-stats/{stats_id}", response_model=APIResponse)
async def delete_staff_stats(stats_id: str):
    try:
        deleted = await StaffStatsService.delete_stats(stats_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/student-stats", response_model=APIResponse)
async def create_student_stats(data: StudentStatsCreate):
    try:
        stats_id = await StudentStatsService.create_stats(data.model_dump())
        return APIResponse(success=True, data={"id": stats_id}, message="Student stats created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/student-stats", response_model=APIResponse)
async def get_student_stats(course_id: Optional[str] = None):
    try:
        if course_id:
            stats = await StudentStatsService.get_stats_by_course(course_id)
        else:
            stats = await StudentStatsService.get_all_stats()
        return APIResponse(success=True, data=stats, count=len(stats))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/student-stats/{stats_id}", response_model=APIResponse)
async def update_student_stats(stats_id: str, data: StudentStatsCreate):
    try:
        updated = await StudentStatsService.update_stats(stats_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/student-stats/{stats_id}", response_model=APIResponse)
async def delete_student_stats(stats_id: str):
    try:
        deleted = await StudentStatsService.delete_stats(stats_id)
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


@router.post("/policies", response_model=APIResponse)
async def create_policy(data: PolicyCreate):
    try:
        policy_id = await PolicyService.create_policy(data.model_dump())
        return APIResponse(success=True, data={"id": policy_id}, message="Policy created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/policies", response_model=APIResponse)
async def get_policies(policy_type: Optional[str] = None):
    try:
        policies = await PolicyService.get_all_policies(policy_type)
        return APIResponse(success=True, data=policies, count=len(policies))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/policies/{policy_id}", response_model=APIResponse)
async def get_policy(policy_id: str):
    try:
        policy = await PolicyService.get_policy(policy_id)
        if not policy:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=policy)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/policies/{policy_id}", response_model=APIResponse)
async def update_policy(policy_id: str, data: PolicyCreate):
    try:
        updated = await PolicyService.update_policy(policy_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/policies/{policy_id}", response_model=APIResponse)
async def delete_policy(policy_id: str):
    try:
        deleted = await PolicyService.delete_policy(policy_id)
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


@router.post("/logout", response_model=APIResponse)
async def logout():
    return APIResponse(success=True, message="Logged out successfully")


@router.get("/health", response_model=APIResponse)
async def health_check():
    return APIResponse(success=True, data={"status": "healthy"}, message="Service running")
