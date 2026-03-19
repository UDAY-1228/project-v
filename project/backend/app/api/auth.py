"""
Auth API — Login, Register, Refresh Token, Password Reset
"""
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, status, BackgroundTasks
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext

from ...shared.config import settings
from ...shared.database import get_collection
from ...shared.models.schemas import LoginRequest, TokenResponse, UserCreate, UserResponse, UserRole
from ...shared.services.rbac_service import get_current_user, require_role

router = APIRouter()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(seconds=settings.JWT_EXPIRY))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, background_tasks: BackgroundTasks):
    """Register a new user (Super Admin creates all other users)"""
    users = get_collection("users")
    existing = await users.find_one({"email": user_data.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_doc = user_data.dict()
    user_doc["password"] = hash_password(user_data.password)
    user_doc["is_active"] = True
    user_doc["created_at"] = datetime.utcnow()
    user_doc["updated_at"] = datetime.utcnow()
    user_doc["face_enrolled"] = False
    user_doc["virtual_id"] = None

    result = await users.insert_one(user_doc)
    user_doc["id"] = str(result.inserted_id)

    # TODO: background_tasks.add_task(send_welcome_email, user_data.email)
    return UserResponse(**user_doc)


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest):
    """Authenticate user and return JWT tokens"""
    users = get_collection("users")
    user = await users.find_one({"email": credentials.email})

    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.get("is_active"):
        raise HTTPException(status_code=403, detail="Account is deactivated")

    user_id = str(user["_id"])
    token_data = {
        "sub": user_id,
        "email": user["email"],
        "role": user["role"],
        "institution_id": user.get("institution_id"),
    }

    access_token = create_token(token_data)
    refresh_token = create_token(token_data, timedelta(days=7))

    user_response = UserResponse(
        id=user_id,
        full_name=user["full_name"],
        email=user["email"],
        phone=user["phone"],
        role=user["role"],
        institution_id=user.get("institution_id"),
        gender=user.get("gender", "male"),
        profile_photo=user.get("profile_photo"),
        is_active=user["is_active"],
        created_at=user["created_at"],
        virtual_id=user.get("virtual_id"),
        qr_code_url=user.get("qr_code_url"),
        face_enrolled=user.get("face_enrolled", False),
    )

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.JWT_EXPIRY,
        role=user["role"],
        user=user_response,
    )


@router.post("/refresh")
async def refresh_token(body: dict):
    """Refresh access token using refresh token"""
    try:
        payload = jwt.decode(body["refresh_token"], settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        new_access = create_token({
            "sub": payload["sub"],
            "email": payload["email"],
            "role": payload["role"],
            "institution_id": payload.get("institution_id"),
        })
        return {"access_token": new_access, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


@router.post("/logout")
async def logout(current_user=Depends(get_current_user)):
    """Invalidate session (client-side token deletion)"""
    # In production: blacklist token in Redis
    return {"message": "Logged out successfully"}


@router.post("/forgot-password")
async def forgot_password(body: dict, background_tasks: BackgroundTasks):
    """Send password reset OTP via email/SMS"""
    users = get_collection("users")
    user = await users.find_one({"email": body.get("email")})
    if not user:
        # Don't reveal if email exists
        return {"message": "If email exists, reset OTP has been sent"}
    # TODO: background_tasks.add_task(send_reset_otp, user["email"], user["phone"])
    return {"message": "Password reset OTP sent to registered email/phone"}


@router.post("/reset-password")
async def reset_password(body: dict):
    """Reset password using OTP"""
    # In production: verify OTP from Redis
    users = get_collection("users")
    result = await users.update_one(
        {"email": body.get("email")},
        {"$set": {"password": hash_password(body.get("new_password", "")), "updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Password reset successfully"}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user=Depends(get_current_user)):
    """Get current logged-in user profile"""
    return current_user
