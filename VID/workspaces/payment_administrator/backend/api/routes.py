from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Payment Administrator"])

@router.get('/academic-fees')
async def get_academic_fees(current_user: TokenData = Depends(get_current_user)):
    return await get_data('academic_fees', current_user.institution_id)

@router.get('/student-permissions')
async def get_student_permissions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('student_permissions', current_user.institution_id)

@router.get('/exam-fee-restrictions')
async def get_exam_fee_restrictions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('exam_fee_restrictions', current_user.institution_id)

@router.get('/examination-fees')
async def get_examination_fees(current_user: TokenData = Depends(get_current_user)):
    return await get_data('examination_fees', current_user.institution_id)

@router.get('/open-payments')
async def get_open_payments(current_user: TokenData = Depends(get_current_user)):
    return await get_data('open_payments', current_user.institution_id)

@router.get('/configuration')
async def get_configuration(current_user: TokenData = Depends(get_current_user)):
    return await get_data('configuration', current_user.institution_id)

@router.get('/reports')
async def get_reports(current_user: TokenData = Depends(get_current_user)):
    return await get_data('reports', current_user.institution_id)

@router.get('/concessions')
async def get_concessions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('concessions', current_user.institution_id)

@router.get('/online-transactions')
async def get_online_transactions(current_user: TokenData = Depends(get_current_user)):
    return await get_data('online_transactions', current_user.institution_id)

@router.get('/challans')
async def get_challans(current_user: TokenData = Depends(get_current_user)):
    return await get_data('challans', current_user.institution_id)

@router.get('/statements')
async def get_statements(current_user: TokenData = Depends(get_current_user)):
    return await get_data('statements', current_user.institution_id)

@router.get('/scholarships')
async def get_scholarships(current_user: TokenData = Depends(get_current_user)):
    return await get_data('scholarships', current_user.institution_id)

@router.get('/credit-memos')
async def get_credit_memos(current_user: TokenData = Depends(get_current_user)):
    return await get_data('credit_memos', current_user.institution_id)

@router.get('/student-fee-card')
async def get_student_fee_card(current_user: TokenData = Depends(get_current_user)):
    return await get_data('student_fee_card', current_user.institution_id)

@router.get('/transaction-card')
async def get_transaction_card(current_user: TokenData = Depends(get_current_user)):
    return await get_data('transaction_card', current_user.institution_id)

