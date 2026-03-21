from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Sports Officer"])

@router.get('/sports-events')
async def get_sports_events(current_user: TokenData = Depends(get_current_user)):
    return await get_data('sports_events', current_user.institution_id)

@router.get('/team-management')
async def get_team_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('team_management', current_user.institution_id)

@router.get('/player-registrations')
async def get_player_registrations(current_user: TokenData = Depends(get_current_user)):
    return await get_data('player_registrations', current_user.institution_id)

@router.get('/practice-schedules')
async def get_practice_schedules(current_user: TokenData = Depends(get_current_user)):
    return await get_data('practice_schedules', current_user.institution_id)

@router.get('/tournament-management')
async def get_tournament_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('tournament_management', current_user.institution_id)

@router.get('/performance-tracking')
async def get_performance_tracking(current_user: TokenData = Depends(get_current_user)):
    return await get_data('performance_tracking', current_user.institution_id)

@router.get('/reports')
async def get_reports(current_user: TokenData = Depends(get_current_user)):
    return await get_data('reports', current_user.institution_id)

@router.get('/activities-list')
async def get_activities_list(current_user: TokenData = Depends(get_current_user)):
    return await get_data('activities_list', current_user.institution_id)

@router.get('/event-calendar')
async def get_event_calendar(current_user: TokenData = Depends(get_current_user)):
    return await get_data('event_calendar', current_user.institution_id)

@router.get('/student-participation')
async def get_student_participation(current_user: TokenData = Depends(get_current_user)):
    return await get_data('student_participation', current_user.institution_id)

@router.get('/achievements')
async def get_achievements(current_user: TokenData = Depends(get_current_user)):
    return await get_data('achievements', current_user.institution_id)

@router.get('/certificates')
async def get_certificates(current_user: TokenData = Depends(get_current_user)):
    return await get_data('certificates', current_user.institution_id)

@router.get('/clubs-management')
async def get_clubs_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('clubs_management', current_user.institution_id)

@router.get('/announcements')
async def get_announcements(current_user: TokenData = Depends(get_current_user)):
    return await get_data('announcements', current_user.institution_id)

