"""
RBAC Service — Role-Based Access Control
JWT token validation + permission matrix
"""
from typing import List, Optional
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from functools import wraps

from .config import settings
from .database import get_collection
from .models.schemas import UserRole

security = HTTPBearer()

# ─── Permission Matrix (from PDFs) ────────────────────────────────────────────
PERMISSIONS = {
    UserRole.SUPER_ADMIN: [
        "institution:*", "user:*", "virtual_id:*", "attendance:*",
        "timetable:*", "fees:*", "lms:*", "exams:*", "analytics:*",
        "communication:*", "admin:*", "ed_officials:*", "notifications:*",
    ],
    UserRole.INSTITUTION_ADMIN: [
        "institution:read", "institution:update",
        "user:create", "user:read", "user:update", "user:delete",
        "virtual_id:generate", "virtual_id:revoke",
        "attendance:read", "attendance:update",
        "timetable:create", "timetable:read", "timetable:update",
        "fees:create", "fees:read", "fees:update",
        "lms:create", "lms:read", "lms:update",
        "exams:create", "exams:read", "exams:update",
        "analytics:read",
        "communication:create", "communication:read",
        "admin:read", "admin:audit",
    ],
    UserRole.FACULTY: [
        "user:read",
        "attendance:create", "attendance:read", "attendance:update",
        "timetable:read",
        "lms:create", "lms:read", "lms:update",
        "exams:create", "exams:read", "exams:update",
        "analytics:read_class",
        "communication:create", "communication:read",
    ],
    UserRole.ED_OFFICIAL: [
        "institution:read",
        "user:read",
        "attendance:read",
        "analytics:read",
        "exams:read",
        "fees:read",
        "communication:read",
    ],
    UserRole.STUDENT: [
        "user:read_self",
        "attendance:read_self",
        "timetable:read",
        "fees:read_self",
        "lms:read",
        "exams:read_self", "exams:submit",
        "communication:read", "communication:send_direct",
        "notifications:read",
        "virtual_id:read_self",
    ],
    UserRole.PARENT: [
        "user:read_child",
        "attendance:read_child",
        "timetable:read_child",
        "fees:read_child", "fees:pay",
        "exams:read_child",
        "communication:read", "communication:message_teacher",
        "notifications:read",
        "virtual_id:read_child",
    ],
}


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Decode JWT and return current user"""
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {
            "id": user_id,
            "email": payload.get("email"),
            "role": payload.get("role"),
            "institution_id": payload.get("institution_id"),
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def require_role(*allowed_roles: UserRole):
    """Dependency to require specific roles"""
    async def role_checker(current_user=Depends(get_current_user)):
        if current_user["role"] not in [r.value for r in allowed_roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {[r.value for r in allowed_roles]}",
            )
        return current_user
    return role_checker


def has_permission(role: str, permission: str) -> bool:
    """Check if a role has a specific permission"""
    role_permissions = PERMISSIONS.get(UserRole(role), [])
    return permission in role_permissions or f"{permission.split(':')[0]}:*" in role_permissions


def require_permission(permission: str):
    """Dependency to check specific permission"""
    async def permission_checker(current_user=Depends(get_current_user)):
        if not has_permission(current_user["role"], permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied: {permission}",
            )
        return current_user
    return permission_checker
