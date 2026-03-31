from fastapi import APIRouter, HTTPException, Request, Depends
from .models import AuthToken, Notice, Timetable, UserProfile
from .services import AuthService, NoticeBoardService, TimetableService, ProfileService
from typing import List

router = APIRouter()

# Auth & Login APIs
@router.post("/login", response_model=AuthToken)
def login(payload: dict):
    user = AuthService.authenticate_user(payload.get("username"), payload.get("password"))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = AuthService.create_access_token(
        data={"sub": str(user["_id"]), "role": user.get("role", "user")}
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Dashboard APIs
@router.get("/dashboard/overview", response_model=dict)
def get_dashboard_overview():
    # Return quick access stats, workspace list, and brief notifications
    return {
        "user_overview": {},
        "workspace_access": [],
        "recent_notifications": NoticeBoardService.get_notices()[:5],
        "quick_access": []
    }

# Notice Board APIs
@router.get("/notices", response_model=List[dict])
def get_notices():
    return NoticeBoardService.get_notices()

# Timetable APIs
@router.get("/timetable/{user_id}", response_model=dict)
def get_timetable(user_id: str):
    res = TimetableService.get_user_timetable(user_id)
    if not res:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return res

# User Panel & Settings APIs
@router.get("/profile/{user_id}", response_model=dict)
def get_user_profile(user_id: str):
    return ProfileService.get_profile(user_id)

@router.put("/profile/{user_id}/security")
def update_profile_security(user_id: str, data: dict):
    return ProfileService.update_profile(user_id, data)
