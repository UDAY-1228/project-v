from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Faculty"])

@router.get('/activities')
async def get_activities(current_user: TokenData = Depends(get_current_user)):
    return await get_data('activities', current_user.institution_id)

@router.get('/my-courses')
async def get_my_courses(current_user: TokenData = Depends(get_current_user)):
    return await get_data('my_courses', current_user.institution_id)

@router.get('/class-timetable')
async def get_class_timetable(current_user: TokenData = Depends(get_current_user)):
    return await get_data('class_timetable', current_user.institution_id)

@router.get('/my-mentees')
async def get_my_mentees(current_user: TokenData = Depends(get_current_user)):
    return await get_data('my_mentees', current_user.institution_id)

@router.get('/question-banks')
async def get_question_banks(current_user: TokenData = Depends(get_current_user)):
    return await get_data('question_banks', current_user.institution_id)

@router.get('/my-profile')
async def get_my_profile(current_user: TokenData = Depends(get_current_user)):
    return await get_data('my_profile', current_user.institution_id)

@router.get('/research-scholar')
async def get_research_scholar(current_user: TokenData = Depends(get_current_user)):
    return await get_data('research_scholar', current_user.institution_id)

@router.get('/lms')
async def get_lms(current_user: TokenData = Depends(get_current_user)):
    return await get_data('lms', current_user.institution_id)

