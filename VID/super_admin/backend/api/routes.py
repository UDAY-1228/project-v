from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import datetime
import uuid
from core.backend.database.connection import db
from core.backend.auth.security import create_access_token, UserRole

router = APIRouter()

@router.post("/institutions")
async def create_new_institution(data: dict):
    # Validating uniqueness of code
    existing = await db.db["institutions"].find_one({"code": data["code"]})
    if existing:
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
    
    await db.db["institutions"].insert_one(institution)
    
    # Create the admin user also in users list for common login
    admin_user = {
        "userId": str(uuid.uuid4()),
        "username": data["adminEmail"],
        "password": data["adminPassword"],
        "role": UserRole.INSTITUTION_ADMIN,
        "institutionId": institution_id,
        "assignedWorkspaces": ["dashboard", "academics", "attendance", "users"] # Default for admin
    }
    await db.db["users"].insert_one(admin_user)
    
    return {"status": "success", "institutionId": institution_id, "admin": admin_user["username"]}

@router.get("/institutions")
async def list_institutions():
    return await db.db["institutions"].find({}, {"_id": 0}).to_list(1000)
