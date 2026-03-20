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

