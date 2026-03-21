from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
import uuid
from core.backend.database.connection import db
from core.backend.auth.security import TokenData, get_current_token # Simplified for UI

router = APIRouter()

@router.post("/users")
async def create_institutional_user(data: dict):
    # data: name, role, username, password, assignedWorkspaces
    # institutionId comes from the admin's token in a real app, here we assume it's passed or stored in session
    
    # Store with its credentials
    user_id = str(uuid.uuid4())
    user = {
        "userId": user_id,
        "name": data["name"],
        "role": data["role"],
        "username": data["username"],
        "password": data["password"],
        "assignedWorkspaces": data["assignedWorkspaces"],
        "institutionId": data.get("institutionId")
    }
    
    await db.db["users"].insert_one(user)
    
    return {"status": "success", "userId": user_id, "name": user["name"]}

@router.get("/users")
async def list_institution_users(institutionId: Optional[str] = None):
    query = {"institutionId": institutionId} if institutionId else {}
    users = await db.db["users"].find(query, {"_id": 0}).to_list(1000)
    return users
