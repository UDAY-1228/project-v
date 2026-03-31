"""
Common - Pydantic Models
=========================
Data models for all Common pages:
Login, Register, Forgot Password, Notifications, Profile, Settings
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    verified = "verified"
    suspended = "suspended"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class LoginBase(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool = False


class LoginCreate(LoginBase):
    pass


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: str
    email: str
    name: str
    role: str
    workspace: Optional[str] = None
    expires_in: int = 3600


class RegisterBase(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    first_name: str
    last_name: str
    phone: Optional[str] = None
    organization: Optional[str] = None
    agree_to_terms: bool = True


class RegisterCreate(RegisterBase):
    pass


class RegisterResponse(BaseModel):
    user_id: str
    email: str
    message: str = "Registration successful. Please verify your email."


class ForgotPasswordBase(BaseModel):
    email: EmailStr


class ForgotPasswordCreate(ForgotPasswordBase):
    pass


class ResetPasswordBase(BaseModel):
    token: str
    new_password: str
    confirm_password: str


class ResetPasswordCreate(ResetPasswordBase):
    pass


class PasswordResetResponse(BaseModel):
    message: str = "Password reset link sent to your email."


class NotificationBase(BaseModel):
    title: str
    message: str
    notification_type: str = Field(default="info")
    user_id: str
    is_read: bool = False
    priority: str = "normal"
    action_url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = {}


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    read_at: Optional[datetime] = None


class NotificationPreferences(BaseModel):
    email_notifications: bool = True
    push_notifications: bool = True
    sms_notifications: bool = False
    notify_on_mentions: bool = True
    notify_on_assignments: bool = True
    notify_on_comments: bool = True
    digest_frequency: str = "daily"


class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    organization: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    linkedin_url: Optional[str] = None
    twitter_handle: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: str
    user_id: str
    role: Optional[str] = None
    is_verified: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    organization: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    linkedin_url: Optional[str] = None
    twitter_handle: Optional[str] = None


class ChangePassword(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str


class SettingsBase(BaseModel):
    theme: str = "dark"
    language: str = "en"
    timezone: str = "UTC"
    date_format: str = "MM/DD/YYYY"
    time_format: str = "12h"
    compact_mode: bool = False
    animations_enabled: bool = True
    notification_preferences: NotificationPreferences = NotificationPreferences()


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: str
    user_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TwoFactorAuth(BaseModel):
    enabled: bool = False
    method: Optional[str] = None
    backup_codes: Optional[List[str]] = None


class SecuritySettings(BaseModel):
    two_factor_auth: TwoFactorAuth = TwoFactorAuth()
    session_timeout: int = 3600
    login_alerts: bool = True
    trusted_devices: List[str] = []
