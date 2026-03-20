from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import datetime
import secrets
import string
from core.backend.auth.security import get_current_user, check_role, get_password_hash, create_access_token
from core.backend.models.common import InstitutionCreate, Institution, UserCreate, UserRole, UserInDB
from core.backend.database.connection import db

router = APIRouter()

# Super admin login
@router.post("/login")
async def super_admin_login(credentials: dict):
    # For initial testing purposes
    if credentials.get("username") == "superadmin" and credentials.get("password") == "admin123":
        access_token = create_access_token(data={"sub": "superadmin", "role": UserRole.SUPER_ADMIN})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Create institution
@router.post("/institutions", response_model=dict, dependencies=[Depends(check_role([UserRole.SUPER_ADMIN]))])
async def create_institution(institution_data: InstitutionCreate):
    # Check if institution name already exists
    existing = await db.db.institutions.find_one({"name": institution_data.name})
    if existing:
        raise HTTPException(status_code=400, detail="Institution with this name already exists")

    # Save institution
    institution_dict = institution_data.dict()
    institution_dict["created_at"] = institution_dict["updated_at"] = datetime.utcnow()
    res = await db.db.institutions.insert_one(institution_dict)
    inst_id = str(res.inserted_id)

    # Generate credentials for institution admin
    admin_username = f"admin_{institution_data.name.lower().replace(' ', '_')}"
    # Generate random temporary password
    alphabet = string.ascii_letters + string.digits
    temp_password = ''.join(secrets.choice(alphabet) for i in range(12))

    # Create admin user
    admin_user = {
        "username": admin_username,
        "email": institution_data.email,
        "full_name": f"{institution_data.name} Administrator",
        "hashed_password": get_password_hash(temp_password),
        "role": UserRole.INSTITUTION_ADMIN,
        "institution_id": inst_id,
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    
    user_res = await db.db.users.insert_one(admin_user)
    admin_user_id = str(user_res.inserted_id)

    # Update institution with admin user ID
    await db.db.institutions.update_one({"_id": res.inserted_id}, {"$set": {"admin_user_id": admin_user_id}})

    return {
        "status": "success",
        "institution_id": inst_id,
        "admin_credentials": {
            "username": admin_username,
            "temporary_password": temp_password
        }
    }

@router.get("/institutions", response_model=List[dict], dependencies=[Depends(check_role([UserRole.SUPER_ADMIN]))])
async def get_institutions():
    cursor = db.db.institutions.find()
    institutions = await cursor.to_list(length=100)
    # Convert _id to string
    for inst in institutions:
        inst["_id"] = str(inst["_id"])
    return institutions
