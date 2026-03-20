from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Course Coordinator"])

@router.get('/all-courses')
async def get_all_courses(current_user: TokenData = Depends(get_current_user)):
    return await get_data('all_courses', current_user.institution_id)

