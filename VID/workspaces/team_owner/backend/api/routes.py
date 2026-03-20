from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Team Owner"])

@router.get('/institutions')
async def get_institutions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('institutions', current_user.institution_id)

@router.get('/organization-settings')
async def get_organization_settings(current_user: TokenData = Depends(get_current_user)):
    return await get_data('organization_settings', current_user.institution_id)

@router.get('/user-management')
async def get_user_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('user_management', current_user.institution_id)

@router.get('/apps')
async def get_apps(current_user: TokenData = Depends(get_current_user)):
    return await get_data('apps', current_user.institution_id)

@router.get('/data-management')
async def get_data_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('data_management', current_user.institution_id)

