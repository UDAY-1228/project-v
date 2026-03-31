"""
Common - API Routes
====================
FastAPI router for all Common endpoints.
Covers: Login, Register, Forgot Password, Notifications, Profile, Settings
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    AuthService,
    NotificationService,
    ProfileService,
    SettingsService,
)

router = APIRouter(prefix="/common", tags=["Common"])


@router.post("/login", response_model=APIResponse)
async def login(data: LoginCreate):
    try:
        user = await AuthService.login(data.email, data.password)
        if user:
            return APIResponse(
                success=True,
                data={
                    "access_token": user["access_token"],
                    "token_type": "bearer",
                    "user_id": user["user_id"],
                    "email": user["email"],
                    "name": user["name"],
                    "role": user["role"],
                    "workspace": user.get("workspace"),
                },
                message="Login successful"
            )
        return APIResponse(success=False, error="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/register", response_model=APIResponse)
async def register(data: RegisterCreate):
    try:
        if data.password != data.confirm_password:
            return APIResponse(success=False, error="Passwords do not match")
        user_id = await AuthService.register(data.model_dump())
        return APIResponse(
            success=True,
            data={"user_id": user_id},
            message="Registration successful. Please verify your email."
        )
    except ValueError as e:
        return APIResponse(success=False, error=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/verify-email", response_model=APIResponse)
async def verify_email(token: str = Query(...)):
    try:
        verified = await AuthService.verify_email(token)
        return APIResponse(
            success=verified,
            message="Email verified" if verified else "Invalid or expired token"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/forgot-password", response_model=APIResponse)
async def forgot_password(data: ForgotPasswordCreate):
    try:
        token = await AuthService.forgot_password(data.email)
        if token:
            return APIResponse(success=True, message="Password reset link sent to your email")
        return APIResponse(success=False, error="Email not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-password", response_model=APIResponse)
async def reset_password(data: ResetPasswordCreate):
    try:
        if data.new_password != data.confirm_password:
            return APIResponse(success=False, error="Passwords do not match")
        reset = await AuthService.reset_password(data.token, data.new_password)
        return APIResponse(
            success=reset,
            message="Password reset successful" if reset else "Invalid or expired token"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/notifications", response_model=APIResponse)
async def create_notification(data: NotificationCreate):
    try:
        notification_id = await NotificationService.create_notification(data.model_dump())
        return APIResponse(success=True, data={"id": notification_id}, message="Notification created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications", response_model=APIResponse)
async def get_notifications(
    user_id: str = Query(...),
    unread_only: bool = Query(False)
):
    try:
        notifications = await NotificationService.get_user_notifications(user_id, unread_only)
        return APIResponse(success=True, data=notifications, count=len(notifications))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications/count", response_model=APIResponse)
async def get_unread_count(user_id: str = Query(...)):
    try:
        count = await NotificationService.get_unread_count(user_id)
        return APIResponse(success=True, data={"unread_count": count})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/notifications/{notification_id}/read", response_model=APIResponse)
async def mark_notification_read(notification_id: str):
    try:
        marked = await NotificationService.mark_as_read(notification_id)
        return APIResponse(success=marked, message="Marked as read" if marked else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/notifications/read-all", response_model=APIResponse)
async def mark_all_read(user_id: str = Query(...)):
    try:
        count = await NotificationService.mark_all_as_read(user_id)
        return APIResponse(success=True, data={"marked_count": count}, message=f"Marked {count} as read")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/notifications/{notification_id}", response_model=APIResponse)
async def delete_notification(notification_id: str):
    try:
        deleted = await NotificationService.delete_notification(notification_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/profile/{user_id}", response_model=APIResponse)
async def get_profile(user_id: str):
    try:
        profile = await ProfileService.get_profile(user_id)
        if not profile:
            return APIResponse(success=False, error="Profile not found")
        return APIResponse(success=True, data=profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile", response_model=APIResponse)
async def create_profile(user_id: str = Query(...), data: ProfileCreate = ...):
    try:
        profile_id = await ProfileService.create_profile(user_id, data.model_dump())
        return APIResponse(success=True, data={"id": profile_id}, message="Profile created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/profile/{user_id}", response_model=APIResponse)
async def update_profile(user_id: str, data: ProfileUpdate):
    try:
        updated = await ProfileService.update_profile(user_id, data.model_dump(exclude_none=True))
        return APIResponse(success=updated, message="Profile updated" if updated else "No changes")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile/{user_id}/avatar", response_model=APIResponse)
async def update_avatar(user_id: str, avatar_url: str = Query(...)):
    try:
        updated = await ProfileService.update_avatar(user_id, avatar_url)
        return APIResponse(success=updated, message="Avatar updated" if updated else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile/{user_id}/change-password", response_model=APIResponse)
async def change_password(user_id: str, data: ChangePassword):
    try:
        if data.new_password != data.confirm_password:
            return APIResponse(success=False, error="Passwords do not match")
        changed = await ProfileService.change_password(user_id, data.current_password, data.new_password)
        return APIResponse(success=changed, message="Password changed" if changed else "Current password incorrect")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings/{user_id}", response_model=APIResponse)
async def get_settings(user_id: str):
    try:
        settings = await SettingsService.get_settings(user_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings/{user_id}", response_model=APIResponse)
async def update_settings(user_id: str, data: SettingsCreate):
    try:
        settings_id = await SettingsService.upsert_settings(user_id, data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/settings/{user_id}/notifications", response_model=APIResponse)
async def update_notification_preferences(user_id: str, preferences: NotificationPreferences):
    try:
        updated = await SettingsService.update_notification_preferences(user_id, preferences.model_dump())
        return APIResponse(success=updated, message="Preferences updated" if updated else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/settings/{user_id}/security", response_model=APIResponse)
async def update_security_settings(user_id: str, security_data: SecuritySettings):
    try:
        updated = await SettingsService.update_security_settings(user_id, security_data.model_dump())
        return APIResponse(success=updated, message="Security settings updated" if updated else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
