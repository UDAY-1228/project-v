"""
Sports Officer - API Routes
==========================
FastAPI router for all Sports Officer endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService, SportsEventService, TeamService,
    PlayerRecordService, ReportService, SportsSettingsService,
)

router = APIRouter(prefix="/sports-officer", tags=["Sports Officer"])


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


@router.post("/sports-events", response_model=APIResponse)
async def create_sports_event(data: SportsEventCreate):
    try:
        event_id = await SportsEventService.create_event(data.model_dump())
        return APIResponse(success=True, data={"id": event_id}, message="Sports event created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sports-events", response_model=APIResponse)
async def get_sports_events(status: Optional[str] = None, sport_type: Optional[str] = None):
    try:
        events = await SportsEventService.get_all_events(status, sport_type)
        return APIResponse(success=True, data=events, count=len(events))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sports-events/{event_id}", response_model=APIResponse)
async def get_sports_event(event_id: str):
    try:
        event = await SportsEventService.get_event(event_id)
        if not event:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/sports-events/{event_id}", response_model=APIResponse)
async def update_sports_event(event_id: str, data: SportsEventCreate):
    try:
        updated = await SportsEventService.update_event(event_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sports-events/{event_id}", response_model=APIResponse)
async def delete_sports_event(event_id: str):
    try:
        deleted = await SportsEventService.delete_event(event_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/teams", response_model=APIResponse)
async def create_team(data: TeamCreate):
    try:
        team_id = await TeamService.create_team(data.model_dump())
        return APIResponse(success=True, data={"id": team_id}, message="Team created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/teams", response_model=APIResponse)
async def get_teams(sport_type: Optional[str] = None):
    try:
        teams = await TeamService.get_all_teams(sport_type)
        return APIResponse(success=True, data=teams, count=len(teams))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/teams/{team_id}", response_model=APIResponse)
async def get_team(team_id: str):
    try:
        team = await TeamService.get_team(team_id)
        if not team:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=team)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/teams/{team_id}", response_model=APIResponse)
async def update_team(team_id: str, data: TeamCreate):
    try:
        updated = await TeamService.update_team(team_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/teams/{team_id}", response_model=APIResponse)
async def delete_team(team_id: str):
    try:
        deleted = await TeamService.delete_team(team_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/player-records", response_model=APIResponse)
async def create_player_record(data: PlayerRecordCreate):
    try:
        player_id = await PlayerRecordService.create_player(data.model_dump())
        return APIResponse(success=True, data={"id": player_id}, message="Player record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/player-records", response_model=APIResponse)
async def get_player_records(team_id: Optional[str] = None, sport_type: Optional[str] = None):
    try:
        players = await PlayerRecordService.get_all_players(team_id, sport_type)
        return APIResponse(success=True, data=players, count=len(players))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/player-records/{player_id}", response_model=APIResponse)
async def get_player_record(player_id: str):
    try:
        player = await PlayerRecordService.get_player(player_id)
        if not player:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/player-records/{player_id}", response_model=APIResponse)
async def update_player_record(player_id: str, data: PlayerRecordCreate):
    try:
        updated = await PlayerRecordService.update_player(player_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/player-records/{player_id}", response_model=APIResponse)
async def delete_player_record(player_id: str):
    try:
        deleted = await PlayerRecordService.delete_player(player_id)
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
async def get_settings():
    try:
        settings = await SportsSettingsService.get_settings()
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SportsSettingsCreate):
    try:
        settings_id = await SportsSettingsService.upsert_settings(data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout", response_model=APIResponse)
async def logout():
    try:
        return APIResponse(success=True, message="Logged out successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
