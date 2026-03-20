from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Common"])

@router.get('/home')
async def get_home(current_user: TokenData = Depends(get_current_user)):
    return await get_data('home', current_user.institution_id)

@router.get('/student-central')
async def get_student_central(current_user: TokenData = Depends(get_current_user)):
    return await get_data('student_central', current_user.institution_id)

@router.get('/my-requests')
async def get_my_requests(current_user: TokenData = Depends(get_current_user)):
    return await get_data('my_requests', current_user.institution_id)

@router.get('/payments')
async def get_payments(current_user: TokenData = Depends(get_current_user)):
    return await get_data('payments', current_user.institution_id)

@router.get('/examination')
async def get_examination(current_user: TokenData = Depends(get_current_user)):
    return await get_data('examination', current_user.institution_id)

@router.get('/hrms')
async def get_hrms(current_user: TokenData = Depends(get_current_user)):
    return await get_data('hrms', current_user.institution_id)

@router.get('/configuration')
async def get_configuration(current_user: TokenData = Depends(get_current_user)):
    return await get_data('configuration', current_user.institution_id)

@router.get('/user-management-system')
async def get_user_management_system(current_user: TokenData = Depends(get_current_user)):
    return await get_data('user_management_system', current_user.institution_id)

