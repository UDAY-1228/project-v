from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Student"])

@router.get('/attendance')
async def get_attendance(current_user: TokenData = Depends(get_current_user)):
    return await get_data('attendance', current_user.institution_id)

@router.get('/chatbot')
async def get_chatbot(current_user: TokenData = Depends(get_current_user)):
    return await get_data('chatbot', current_user.institution_id)

@router.get('/teacher-communications')
async def get_teacher_communications(current_user: TokenData = Depends(get_current_user)):
    return await get_data('teacher_communications', current_user.institution_id)

@router.get('/fees')
async def get_fees(current_user: TokenData = Depends(get_current_user)):
    return await get_data('fees', current_user.institution_id)

@router.get('/examinations')
async def get_examinations(current_user: TokenData = Depends(get_current_user)):
    return await get_data('examinations', current_user.institution_id)

@router.get('/co-curricular-activities')
async def get_co_curricular_activities(current_user: TokenData = Depends(get_current_user)):
    return await get_data('co_curricular_activities', current_user.institution_id)

@router.get('/learning-management')
async def get_learning_management(current_user: TokenData = Depends(get_current_user)):
    return await get_data('learning_management', current_user.institution_id)

@router.get('/course-tracking')
async def get_course_tracking(current_user: TokenData = Depends(get_current_user)):
    return await get_data('course_tracking', current_user.institution_id)

@router.get('/profile')
async def get_profile(current_user: TokenData = Depends(get_current_user)):
    return await get_data('profile', current_user.institution_id)

@router.get('/payment-history')
async def get_payment_history(current_user: TokenData = Depends(get_current_user)):
    return await get_data('payment_history', current_user.institution_id)

