from fastapi import APIRouter, Depends, HTTPException, status
from .models import InstitutionCreate, LoginSchema
from .services import create_institution, get_all_institutions, super_admin_login
from ..core.auth.rbac import RoleChecker

router = APIRouter()

# Super admin login
@router.post("/login")
async def login(data: LoginSchema):
    token = await super_admin_login(data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials for Super Admin")
    return token

# Create institution (only super admins)
@router.post("/institutions", dependencies=[Depends(RoleChecker(["super_admin"]))])
async def create_new_institution(institution: InstitutionCreate):
    created = await create_institution(institution)
    if not created:
        raise HTTPException(status_code=400, detail="Institution ID already exists")
    return {"message": "Institution created successfully", "data": created}

# List institutions (only super admins)
@router.get("/institutions", dependencies=[Depends(RoleChecker(["super_admin"]))])
async def list_institutions():
    return await get_all_institutions()
