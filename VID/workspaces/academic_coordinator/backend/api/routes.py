from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from core.backend.auth.security import get_current_user, TokenData, check_role
from ..services.logic import get_data, create_item

router = APIRouter(tags=["Academic Coordinator"])

@router.get("/activities")
async def get_activities(current_user: TokenData = Depends(get_current_user)):
    return await get_data("activities", current_user.institution_id)

@router.get("/courses")
async def get_courses(current_user: TokenData = Depends(get_current_user)):
    return await get_data("courses", current_user.institution_id)

@router.get("/assessments")
async def get_assessments(current_user: TokenData = Depends(get_current_user)):
    return await get_data("assessments", current_user.institution_id)

@router.get("/catalog")
async def get_catalog(current_user: TokenData = Depends(get_current_user)):
    return await get_data("master_catalog", current_user.institution_id)

@router.get("/config")
async def get_config(current_user: TokenData = Depends(get_current_user)):
    return await get_data("configs", current_user.institution_id)

@router.post("/activities")
async def create_activity(activity_data: Dict[str, Any], current_user: TokenData = Depends(get_current_user)):
    activity_data["institution_id"] = current_user.institution_id
    return {"id": await create_item("activities", activity_data)}
