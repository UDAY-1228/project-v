from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import datetime
import uuid
from core.backend.database.json_storage import add_institution, add_user, get_institutions
from core.backend.auth.security import create_access_token, UserRole

router = APIRouter()

@router.post("/institutions")
async def create_new_institution(data: dict):
    # Validating uniqueness of code
    existing = get_institutions()
    if any(inst['code'] == data['code'] for inst in existing):
        raise HTTPException(status_code=400, detail="Institution code must be unique")
    
    # Store institution and admin
    institution_id = str(uuid.uuid4())
    institution = {
        "institutionId": institution_id,
        "name": data["name"],
        "code": data["code"],
        "adminCredentials": {
            "email": data["adminEmail"],
            "username": data["adminEmail"],
            "password": data["adminPassword"]
        }
    }
    
    add_institution(institution)
    
    # Create the admin user also in users list for common login
    admin_user = {
        "userId": str(uuid.uuid4()),
        "username": data["adminEmail"],
        "password": data["adminPassword"],
        "role": UserRole.INSTITUTION_ADMIN,
        "institutionId": institution_id,
        "assignedWorkspaces": ["dashboard", "academics", "attendance", "users"] # Default for admin
    }
    add_user(admin_user)
    
    return {"status": "success", "institutionId": institution_id, "admin": admin_user["username"]}

@router.get("/institutions")
async def list_institutions():
    return get_institutions()
