from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Hostel Admin"])

@router.get('/hostels')
async def get_hostels(current_user: TokenData = Depends(get_current_user)):
    return await get_data('hostels', current_user.institution_id)

@router.get('/attendance')
async def get_attendance(current_user: TokenData = Depends(get_current_user)):
    return await get_data('attendance', current_user.institution_id)

@router.get('/gate-pass')
async def get_gate_pass(current_user: TokenData = Depends(get_current_user)):
    return await get_data('gate_pass', current_user.institution_id)

@router.get('/requests')
async def get_requests(current_user: TokenData = Depends(get_current_user)):
    return await get_data('requests', current_user.institution_id)

@router.get('/reports')
async def get_reports(current_user: TokenData = Depends(get_current_user)):
    return await get_data('reports', current_user.institution_id)

@router.get('/configuration')
async def get_configuration(current_user: TokenData = Depends(get_current_user)):
    return await get_data('configuration', current_user.institution_id)

