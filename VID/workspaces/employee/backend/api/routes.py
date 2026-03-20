from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Employee"])

@router.get('/home')
async def get_home(current_user: TokenData = Depends(get_current_user)):
    return await get_data('home', current_user.institution_id)

@router.get('/leaves')
async def get_leaves(current_user: TokenData = Depends(get_current_user)):
    return await get_data('leaves', current_user.institution_id)

@router.get('/attendance')
async def get_attendance(current_user: TokenData = Depends(get_current_user)):
    return await get_data('attendance', current_user.institution_id)

@router.get('/salary')
async def get_salary(current_user: TokenData = Depends(get_current_user)):
    return await get_data('salary', current_user.institution_id)

@router.get('/expenses')
async def get_expenses(current_user: TokenData = Depends(get_current_user)):
    return await get_data('expenses', current_user.institution_id)

@router.get('/shift-requests')
async def get_shift_requests(current_user: TokenData = Depends(get_current_user)):
    return await get_data('shift_requests', current_user.institution_id)

@router.get('/compensatory-leave')
async def get_compensatory_leave(current_user: TokenData = Depends(get_current_user)):
    return await get_data('compensatory_leave', current_user.institution_id)

