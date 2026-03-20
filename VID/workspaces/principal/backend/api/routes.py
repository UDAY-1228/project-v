from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from core.backend.auth.security import get_current_user, check_role, TokenData
from ..services.logic import get_items, create_item, get_item_by_id

router = APIRouter()

@router.get("/")
async def list_items(current_user: TokenData = Depends(get_current_user)):
    return await get_items(current_user.institution_id)

@router.post("/")
async def create_new_item(item_data: dict, current_user: TokenData = Depends(get_current_user)):
    return await create_item(item_data, current_user.institution_id)

@router.get("/{item_id}")
async def read_item_details(item_id: str, current_user: TokenData = Depends(get_current_user)):
    return await get_item_by_id(item_id, current_user.institution_id)
