from fastapi import APIRouter, Depends, HTTPException, status
from core.backend.database.connection import db
import secrets

router = APIRouter()

@router.post("/login")
async def unified_login(credentials: dict):
    username = credentials.get("username")
    password = credentials.get("password")
    
    # Hardcoded Super Admin (default)
    if username == "superadmin" and password == "superpass":
        return {
            "token": "sa-token-" + str(secrets.token_hex(8)),
            "role": "super-admin",
            "redirect": "/super-admin/dashboard",
            "assignedWorkspaces": ["institutions", "analytics", "health"] # All for super admin
        }
    
    # Check institutional admin and users in MongoDB storage
    user = await db.db["users"].find_one({"username": username, "password": password})
    
    if user:
        # Smarter Redirection
        if user["role"] == "admin":
            redirect = "/admin/dashboard"
        elif user.get("assignedWorkspaces"):
            # Redirect to the first assigned workspace dashboard
            ws_slug = user["assignedWorkspaces"][0]
            redirect = f"/{ws_slug}/dashboard"
        else:
            redirect = "/common/home" # Fallback
            
        return {
            "token": "user-token-" + str(secrets.token_hex(8)),
            "userId": user["userId"],
            "role": user["role"],
            "institutionId": user.get("institutionId"),
            "redirect": redirect,
            "assignedWorkspaces": user.get("assignedWorkspaces", [])
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")
