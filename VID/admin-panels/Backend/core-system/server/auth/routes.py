from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .services import unified_login
from typing import Optional

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str
    institution_id: Optional[str] = None # Optional for Super Admin

@router.post("/login")
async def login(data: LoginRequest):
    result = await unified_login(data.username, data.password, data.institution_id)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
