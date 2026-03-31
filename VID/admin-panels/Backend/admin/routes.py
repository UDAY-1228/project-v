from fastapi import APIRouter, HTTPException
from .models import User, Notice, AdminDashboardStats
from .services import UserService, WorkspaceService, NoticeService, AnalyticsService
from typing import List

router = APIRouter()

# User Management APIs
@router.post("/users", response_model=str)
def create_user(user: dict):
    return UserService.create_user(user)

@router.get("/users", response_model=List[dict])
def get_users():
    return UserService.get_all_users()

@router.get("/users/{user_id}", response_model=dict)
def get_user(user_id: str):
    res = UserService.get_user_by_id(user_id)
    if not res:
        raise HTTPException(status_code=404, detail="User not found")
    return res

@router.patch("/users/{user_id}/activation")
def patch_activation(user_id: str, payload: dict):
    return UserService.toggle_user_activation(user_id, payload.get("is_active", True))

@router.put("/users/{user_id}/workspaces")
def assign_workspaces(user_id: str, payload: dict):
    return UserService.assign_workspace(user_id, payload.get("workspaces", []))

# Institution/Workspace Operations APIs
@router.get("/workspaces", response_model=List[dict])
def get_workspaces():
    return WorkspaceService.get_all_workspaces()

@router.put("/workspaces/{workspace_id}/access")
def update_workspace_access(workspace_id: str, data: dict):
    return WorkspaceService.update_workspace_access(workspace_id, data)

# Notice Board APIs
@router.post("/notices", response_model=str)
def create_notice(notice: dict):
    return NoticeService.create_notice(notice)

@router.get("/notices", response_model=List[dict])
def get_notices():
    return NoticeService.get_all_notices()

@router.delete("/notices/{notice_id}")
def delete_notice(notice_id: str):
    return NoticeService.delete_notice(notice_id)

# Reports & Analytics APIs
@router.get("/dashboard/stats", response_model=dict)
def get_dashboard_stats():
    return AnalyticsService.get_admin_dashboard_stats()
