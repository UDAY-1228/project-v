"""
Team Owner - FastAPI Routes
===========================
API endpoints for the Team Owner workspace.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from . import models
from . import services

router = APIRouter(prefix="/api/team-owner", tags=["Team Owner"])


@router.get("/dashboard", response_model=models.DashboardStats)
async def get_dashboard():
    """Get dashboard statistics."""
    return await services.DashboardService.get_stats()


@router.get("/dashboard/stats", response_model=models.DashboardStats)
async def get_dashboard_stats():
    """Get dashboard statistics (alias)."""
    return await services.DashboardService.get_stats()


@router.post("/workspaces", response_model=models.Workspace)
async def create_workspace(workspace: models.WorkspaceCreate):
    """Create a new workspace."""
    return await services.WorkspaceService.create(workspace.model_dump())


@router.get("/workspaces", response_model=List[models.Workspace])
async def get_all_workspaces():
    """Get all workspaces."""
    return await services.WorkspaceService.get_all()


@router.get("/workspaces/{workspace_id}", response_model=models.Workspace)
async def get_workspace(workspace_id: str):
    """Get workspace by ID."""
    workspace = await services.WorkspaceService.get_by_id(workspace_id)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return workspace


@router.get("/workspaces/owner/{owner_id}", response_model=List[models.Workspace])
async def get_workspaces_by_owner(owner_id: str):
    """Get workspaces by owner ID."""
    return await services.WorkspaceService.get_by_owner(owner_id)


@router.put("/workspaces/{workspace_id}", response_model=models.Workspace)
async def update_workspace(workspace_id: str, workspace: models.WorkspaceUpdate):
    """Update a workspace."""
    updated = await services.WorkspaceService.update(workspace_id, workspace.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return updated


@router.delete("/workspaces/{workspace_id}")
async def delete_workspace(workspace_id: str):
    """Delete a workspace."""
    deleted = await services.WorkspaceService.delete(workspace_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return {"message": "Workspace deleted successfully"}


@router.post("/members", response_model=models.Member)
async def create_member(member: models.MemberCreate):
    """Create a new member."""
    return await services.MemberService.create(member.model_dump())


@router.get("/members", response_model=List[models.Member])
async def get_all_members():
    """Get all members."""
    return await services.MemberService.get_all()


@router.get("/members/{member_id}", response_model=models.Member)
async def get_member(member_id: str):
    """Get member by ID."""
    member = await services.MemberService.get_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.get("/members/workspace/{workspace_id}", response_model=List[models.Member])
async def get_members_by_workspace(workspace_id: str):
    """Get members by workspace ID."""
    return await services.MemberService.get_by_workspace(workspace_id)


@router.get("/members/user/{user_id}", response_model=List[models.Member])
async def get_members_by_user(user_id: str):
    """Get members by user ID."""
    return await services.MemberService.get_by_user(user_id)


@router.put("/members/{member_id}", response_model=models.Member)
async def update_member(member_id: str, member: models.MemberUpdate):
    """Update a member."""
    updated = await services.MemberService.update(member_id, member.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated


@router.delete("/members/{member_id}")
async def delete_member(member_id: str):
    """Delete a member."""
    deleted = await services.MemberService.delete(member_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted successfully"}


@router.post("/access-controls", response_model=models.AccessControl)
async def create_access_control(control: models.AccessControlCreate):
    """Create a new access control."""
    return await services.AccessControlService.create(control.model_dump())


@router.get("/access-controls", response_model=List[models.AccessControl])
async def get_all_access_controls():
    """Get all access controls."""
    return await services.AccessControlService.get_all()


@router.get("/access-controls/{control_id}", response_model=models.AccessControl)
async def get_access_control(control_id: str):
    """Get access control by ID."""
    control = await services.AccessControlService.get_by_id(control_id)
    if not control:
        raise HTTPException(status_code=404, detail="Access control not found")
    return control


@router.get("/access-controls/workspace/{workspace_id}", response_model=List[models.AccessControl])
async def get_access_controls_by_workspace(workspace_id: str):
    """Get access controls by workspace ID."""
    return await services.AccessControlService.get_by_workspace(workspace_id)


@router.get("/access-controls/user/{user_id}", response_model=List[models.AccessControl])
async def get_access_controls_by_user(user_id: str):
    """Get access controls by user ID."""
    return await services.AccessControlService.get_by_user(user_id)


@router.put("/access-controls/{control_id}", response_model=models.AccessControl)
async def update_access_control(control_id: str, control: models.AccessControlUpdate):
    """Update an access control."""
    updated = await services.AccessControlService.update(control_id, control.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Access control not found")
    return updated


@router.delete("/access-controls/{control_id}")
async def delete_access_control(control_id: str):
    """Delete an access control."""
    deleted = await services.AccessControlService.delete(control_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Access control not found")
    return {"message": "Access control deleted successfully"}


@router.post("/reports", response_model=models.Report)
async def create_report(report: models.ReportCreate):
    """Create a new report."""
    return await services.ReportService.create(report.model_dump())


@router.get("/reports", response_model=List[models.Report])
async def get_all_reports():
    """Get all reports."""
    return await services.ReportService.get_all()


@router.get("/reports/type/{report_type}", response_model=List[models.Report])
async def get_reports_by_type(report_type: str):
    """Get reports by type."""
    return await services.ReportService.get_by_type(report_type)


@router.get("/settings")
async def get_settings():
    """Get settings."""
    settings = await services.SettingsService.get()
    if not settings:
        return {"workspace_name": "Team Owner", "default_role": "member", "auto_approval": False}
    return settings


@router.put("/settings")
async def update_settings(settings: dict):
    """Update settings."""
    return await services.SettingsService.update(settings)


@router.post("/logout")
async def logout():
    """Logout endpoint."""
    return {"message": "Logged out successfully"}
