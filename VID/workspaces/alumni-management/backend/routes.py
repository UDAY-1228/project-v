"""
Alumni Management - API Routes
==============================
FastAPI router for all Alumni Management endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    AlumniDatabaseService,
    DonationsService,
    CampaignsService,
    EventsService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/alumni-management", tags=["Alumni Management"])


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
async def create_alumni(data: AlumniDatabaseCreate):
    try:
        alumni_id = await AlumniDatabaseService.create_alumni(data.model_dump())
        return APIResponse(success=True, data={"id": alumni_id}, message="Alumni record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni", response_model=APIResponse)
async def get_alumni(department: Optional[str] = None, graduation_year: Optional[int] = None):
    try:
        alumni = await AlumniDatabaseService.get_all_alumni(department, graduation_year)
        return APIResponse(success=True, data=alumni, count=len(alumni))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni/search", response_model=APIResponse)
async def search_alumni(query: str = Query(..., min_length=1)):
    try:
        results = await AlumniDatabaseService.search_alumni(query)
        return APIResponse(success=True, data=results, count=len(results))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alumni/{alumni_id}", response_model=APIResponse)
async def get_alumni_record(alumni_id: str):
    try:
        alumni = await AlumniDatabaseService.get_alumni(alumni_id)
        if not alumni:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=alumni)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/alumni/{alumni_id}", response_model=APIResponse)
async def update_alumni(alumni_id: str, data: AlumniDatabaseCreate):
    try:
        updated = await AlumniDatabaseService.update_alumni(alumni_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/alumni/{alumni_id}", response_model=APIResponse)
async def delete_alumni(alumni_id: str):
    try:
        deleted = await AlumniDatabaseService.delete_alumni(alumni_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/alumni/{alumni_id}/verify", response_model=APIResponse)
async def verify_alumni(alumni_id: str):
    try:
        verified = await AlumniDatabaseService.verify_alumni(alumni_id)
        return APIResponse(success=verified, message="Verified" if verified else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/donations", response_model=APIResponse)
async def create_donation(data: DonationCreate):
    try:
        donation_id = await DonationsService.create_donation(data.model_dump())
        return APIResponse(success=True, data={"id": donation_id}, message="Donation recorded")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/donations", response_model=APIResponse)
async def get_donations(status: Optional[str] = None):
    try:
        donations = await DonationsService.get_all_donations(status)
        return APIResponse(success=True, data=donations, count=len(donations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/donations/total", response_model=APIResponse)
async def get_total_donations():
    try:
        total = await DonationsService.get_total_donations()
        return APIResponse(success=True, data={"total": total})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/donations/{donation_id}", response_model=APIResponse)
async def get_donation(donation_id: str):
    try:
        donation = await DonationsService.get_donation(donation_id)
        if not donation:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=donation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/donations/donor/{donor_id}", response_model=APIResponse)
async def get_donations_by_donor(donor_id: str):
    try:
        donations = await DonationsService.get_donations_by_donor(donor_id)
        return APIResponse(success=True, data=donations, count=len(donations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/campaigns", response_model=APIResponse)
async def create_campaign(data: DonationCampaign):
    try:
        campaign_id = await CampaignsService.create_campaign(data.model_dump())
        return APIResponse(success=True, data={"id": campaign_id}, message="Campaign created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/campaigns", response_model=APIResponse)
async def get_campaigns(active_only: bool = False):
    try:
        campaigns = await CampaignsService.get_all_campaigns(active_only)
        return APIResponse(success=True, data=campaigns, count=len(campaigns))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/campaigns/{campaign_id}", response_model=APIResponse)
async def get_campaign(campaign_id: str):
    try:
        campaign = await CampaignsService.get_campaign(campaign_id)
        if not campaign:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=campaign)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/campaigns/{campaign_id}", response_model=APIResponse)
async def update_campaign(campaign_id: str, data: DonationCampaign):
    try:
        updated = await CampaignsService.update_campaign(campaign_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
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
