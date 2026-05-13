"""
VID Auth Service – Pydantic Schemas
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


# ── Request Schemas ────────────────────────────────────────────────────────────

class LoginRequest(BaseModel):
    email:    EmailStr
    password: str = Field(..., min_length=6)


class RegisterRequest(BaseModel):
    email:          EmailStr
    password:       str       = Field(..., min_length=8)
    first_name:     str       = Field(..., min_length=1, max_length=100)
    last_name:      str       = Field(..., min_length=1, max_length=100)
    phone:          Optional[str] = None
    user_type:      str       = Field(default="STAFF")
    institution_id: Optional[UUID] = None


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(..., min_length=6)
    new_password:     str = Field(..., min_length=8)


class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ── Response Schemas ────────────────────────────────────────────────────────────

class TokenResponse(BaseModel):
    access_token:  str
    refresh_token: str
    token_type:    str = "bearer"
    expires_in:    int  # seconds


class UserResponse(BaseModel):
    id:               UUID
    email:            str
    first_name:       str
    last_name:        str
    user_type:        str
    institution_id:   Optional[UUID]
    is_active:        bool
    is_email_verified:bool
    last_login_at:    Optional[datetime]
    created_at:       datetime

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    user:   UserResponse
    tokens: TokenResponse


class MessageResponse(BaseModel):
    message: str
    success: bool = True
