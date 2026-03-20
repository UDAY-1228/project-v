from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from core.backend.auth.security import get_current_user, check_role, TokenData
from ..services.logic import get_transport_data, create_transport_item

router = APIRouter()

@router.get("/buses")
async def list_buses(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("buses", current_user.institution_id if current_user.institution_id else "default")

@router.get("/routes")
async def list_routes(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("routes", current_user.institution_id if current_user.institution_id else "default")

@router.get("/boarding-points")
async def list_boarding_points(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("boarding_points", current_user.institution_id if current_user.institution_id else "default")

@router.get("/registrations")
async def list_registrations(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("registrations", current_user.institution_id if current_user.institution_id else "default")

@router.get("/assignments")
async def list_assignments(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("assignments", current_user.institution_id if current_user.institution_id else "default")

@router.get("/notice-board")
async def list_notices(current_user: TokenData = Depends(get_current_user)):
    return await get_transport_data("notice_board", current_user.institution_id if current_user.institution_id else "default")

@router.get("/analytics")
async def get_analytics(current_user: TokenData = Depends(get_current_user)):
    data = await get_transport_data("analytics", current_user.institution_id if current_user.institution_id else "default")
    return data[0] if isinstance(data, list) and data else data

@router.get("/configurations")
async def get_config(current_user: TokenData = Depends(get_current_user)):
    data = await get_transport_data("configurations", current_user.institution_id if current_user.institution_id else "default")
    return data[0] if isinstance(data, list) and data else data
