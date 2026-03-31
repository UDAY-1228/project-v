"""
Research Development - API Routes
==================================
FastAPI router for all Research Development endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    ResearchProjectService,
    PublicationService,
    GrantService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/research-development", tags=["Research Development"])


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


@router.post("/research-projects", response_model=APIResponse)
async def create_research_project(data: ResearchProjectCreate):
    try:
        project_id = await ResearchProjectService.create_project(data.model_dump())
        return APIResponse(success=True, data={"id": project_id}, message="Research project created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/research-projects", response_model=APIResponse)
async def get_research_projects(status: Optional[str] = None, department: Optional[str] = None):
    try:
        projects = await ResearchProjectService.get_all_projects(status, department)
        return APIResponse(success=True, data=projects, count=len(projects))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/research-projects/{project_id}", response_model=APIResponse)
async def get_research_project(project_id: str):
    try:
        project = await ResearchProjectService.get_project(project_id)
        if not project:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/research-projects/{project_id}", response_model=APIResponse)
async def update_research_project(project_id: str, data: ResearchProjectCreate):
    try:
        updated = await ResearchProjectService.update_project(project_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/research-projects/{project_id}", response_model=APIResponse)
async def delete_research_project(project_id: str):
    try:
        deleted = await ResearchProjectService.delete_project(project_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/publications", response_model=APIResponse)
async def create_publication(data: PublicationCreate):
    try:
        pub_id = await PublicationService.create_publication(data.model_dump())
        return APIResponse(success=True, data={"id": pub_id}, message="Publication created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/publications", response_model=APIResponse)
async def get_publications(pub_type: Optional[str] = None, department: Optional[str] = None):
    try:
        publications = await PublicationService.get_all_publications(pub_type, department)
        return APIResponse(success=True, data=publications, count=len(publications))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/publications/{publication_id}", response_model=APIResponse)
async def get_publication(publication_id: str):
    try:
        publication = await PublicationService.get_publication(publication_id)
        if not publication:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=publication)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/publications/{publication_id}", response_model=APIResponse)
async def update_publication(publication_id: str, data: PublicationCreate):
    try:
        updated = await PublicationService.update_publication(publication_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/publications/{publication_id}", response_model=APIResponse)
async def delete_publication(publication_id: str):
    try:
        deleted = await PublicationService.delete_publication(publication_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/grants", response_model=APIResponse)
async def create_grant(data: GrantCreate):
    try:
        grant_id = await GrantService.create_grant(data.model_dump())
        return APIResponse(success=True, data={"id": grant_id}, message="Grant created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/grants", response_model=APIResponse)
async def get_grants(status: Optional[str] = None, agency: Optional[str] = None):
    try:
        grants = await GrantService.get_all_grants(status, agency)
        return APIResponse(success=True, data=grants, count=len(grants))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/grants/{grant_id}", response_model=APIResponse)
async def get_grant(grant_id: str):
    try:
        grant = await GrantService.get_grant(grant_id)
        if not grant:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=grant)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/grants/{grant_id}", response_model=APIResponse)
async def update_grant(grant_id: str, data: GrantCreate):
    try:
        updated = await GrantService.update_grant(grant_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/grants/{grant_id}", response_model=APIResponse)
async def delete_grant(grant_id: str):
    try:
        deleted = await GrantService.delete_grant(grant_id)
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
