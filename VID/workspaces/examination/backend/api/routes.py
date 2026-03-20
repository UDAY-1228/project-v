from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Examination"])

@router.get('/results')
async def get_results(current_user: TokenData = Depends(get_current_user)):
    return await get_data('results', current_user.institution_id)

@router.get('/previous-exams')
async def get_previous_exams(current_user: TokenData = Depends(get_current_user)):
    return await get_data('previous_exams', current_user.institution_id)

@router.get('/tests')
async def get_tests(current_user: TokenData = Depends(get_current_user)):
    return await get_data('tests', current_user.institution_id)

@router.get('/previous-year-papers')
async def get_previous_year_papers(current_user: TokenData = Depends(get_current_user)):
    return await get_data('previous_year_papers', current_user.institution_id)

@router.get('/averages')
async def get_averages(current_user: TokenData = Depends(get_current_user)):
    return await get_data('averages', current_user.institution_id)

@router.get('/class-toppers')
async def get_class_toppers(current_user: TokenData = Depends(get_current_user)):
    return await get_data('class_toppers', current_user.institution_id)

@router.get('/reports')
async def get_reports(current_user: TokenData = Depends(get_current_user)):
    return await get_data('reports', current_user.institution_id)

