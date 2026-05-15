"""
VID Auth Service – Authentication Router
"""
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID

from database import get_db
from models import User, Session as UserSession, UserRole, Role
from schemas import (
    LoginRequest, LoginResponse, RegisterRequest, 
    UserResponse, TokenResponse, MessageResponse, ChangePasswordRequest
)
from utils import (
    get_password_hash, verify_password, 
    create_access_token, create_refresh_token
)

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)):
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == payload.email))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=payload.email,
        password_hash=get_password_hash(payload.password),
        first_name=payload.first_name,
        last_name=payload.last_name,
        phone=payload.phone,
        user_type=payload.user_type,
        institution_id=payload.institution_id,
        is_active=True
    )
    db.add(new_user)
    await db.flush()
    return new_user

@auth_router.post("/login", response_model=LoginResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == payload.email))
    user = result.scalars().first()
    
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is disabled")

    # Fetch user roles
    roles_result = await db.execute(
        select(Role.code)
        .join(UserRole, Role.id == UserRole.role_id)
        .where(UserRole.user_id == user.id)
    )
    user_roles = roles_result.scalars().all()

    # Generate tokens
    token_data = {
        "sub": str(user.id),
        "institution_id": str(user.institution_id) if user.institution_id else None,
        "user_type": user.user_type,
        "roles": list(user_roles)
    }
    
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)

    # Store session
    new_session = UserSession(
        user_id=user.id,
        refresh_token=refresh_token,
        expires_at=datetime.utcnow() + timedelta(days=30)
    )
    db.add(new_session)
    
    # Update last login
    user.last_login_at = datetime.utcnow()
    
    return {
        "user": user,
        "tokens": {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": 3600
        }
    }

@auth_router.get("/me", response_model=UserResponse)
async def get_me(request: Request, db: AsyncSession = Depends(get_db)):
    # In a real gateway scenario, the gateway extracts the user_id from JWT
    # and passes it via X-User-ID header.
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@auth_router.post("/change-password", response_model=MessageResponse)
async def change_password(request: Request, payload: ChangePasswordRequest, db: AsyncSession = Depends(get_db)):
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
        
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    
    if not user or not verify_password(payload.current_password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid current password")
        
    user.password_hash = get_password_hash(payload.new_password)
    return {"message": "Password changed successfully"}
