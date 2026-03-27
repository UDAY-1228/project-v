from fastapi import APIRouter, Depends, HTTPException, status
from .models import UserCreate, LoginSchema
from .services import create_user, list_institution_users, admin_login
from ..core.auth.rbac import RoleChecker

router = APIRouter()

# Admin login
@router.post("/login")
async def login_route(data: LoginSchema):
    token = await admin_login(data.username, data.password, data.institution_id)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid admin credentials or institution ID")
    return token

# User creation (only admins)
@router.post("/users", dependencies=[Depends(RoleChecker(["admin"]))])
async def create_new_user(user: UserCreate, current_admin: dict = Depends(RoleChecker(["admin"]))):
    inst_id = current_admin["institution_id"]
    created_user = await create_user(user, inst_id)
    if not created_user:
        raise HTTPException(status_code=400, detail="User username already exists")
    return {"message": "User created successfully", "data": created_user}

# List institution users (only admins)
@router.get("/users", dependencies=[Depends(RoleChecker(["admin"]))])
async def list_users(current_admin: dict = Depends(RoleChecker(["admin"]))):
    inst_id = current_admin["institution_id"]
    return await list_institution_users(inst_id)
