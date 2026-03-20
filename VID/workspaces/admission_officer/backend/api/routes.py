from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Admission Officer"])

@router.get('/prospects')
async def get_prospects(current_user: TokenData = Depends(get_current_user)):
    return await get_data('prospects', current_user.institution_id)

@router.get('/applications')
async def get_applications(current_user: TokenData = Depends(get_current_user)):
    return await get_data('applications', current_user.institution_id)

@router.get('/admissions')
async def get_admissions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('admissions', current_user.institution_id)

@router.get('/configuration')
async def get_configuration(current_user: TokenData = Depends(get_current_user)):
    return await get_data('configuration', current_user.institution_id)

