from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import datetime
from core.backend.auth.security import get_current_user, check_role, get_password_hash, create_access_token, TokenData
from core.backend.models.common import UserCreate, UserRole, UserInDB
from core.backend.database.connection import db

router = APIRouter()

# Admin login
@router.post("/login")
async def admin_login(credentials: dict):
    # Dummy login for initial check
    if credentials.get("username") == "admin" and credentials.get("password") == "admin123":
        # Simulate check-in DB
        access_token = create_access_token(data={"sub": "admin", "role": UserRole.INSTITUTION_ADMIN, "institution_id": "inst_123"})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Create user (teacher, staff, student)
@router.post("/users", response_model=dict, dependencies=[Depends(check_role([UserRole.INSTITUTION_ADMIN]))])
async def create_user(user_data: UserCreate, current_user: TokenData = Depends(get_current_user)):
    # Check if username or email already exists
    existing_user = await db.db.users.find_one({"$or": [{"username": user_data.username}, {"email": user_data.email}]})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username or email already exists")

    # Save user with institutional ID
    user_dict = user_data.dict()
    # Add institution_id from the current admin
    user_dict["institution_id"] = current_user.institution_id
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
    user_dict["created_at"] = user_dict["updated_at"] = datetime.utcnow()
    
    res = await db.db.users.insert_one(user_dict)
    user_id = str(res.inserted_id)

    return {
        "status": "success",
        "user_id": user_id,
        "username": user_data.username,
        "role": user_data.role
    }

@router.get("/users", response_model=List[dict], dependencies=[Depends(check_role([UserRole.INSTITUTION_ADMIN]))])
async def get_institution_users(current_user: TokenData = Depends(get_current_user)):
    cursor = db.db.users.find({"institution_id": current_user.institution_id})
    users = await cursor.to_list(length=100)
    for u in users:
        u["_id"] = str(u["_id"])
        if "hashed_password" in u:
            del u["hashed_password"]
    return users

# Update roles and permissions
@router.patch("/users/{user_id}/role", dependencies=[Depends(check_role([UserRole.INSTITUTION_ADMIN]))])
async def update_user_role(user_id: str, new_role: UserRole, current_user: TokenData = Depends(get_current_user)):
    # Find user and verify they belong to same institution
    user = await db.db.users.find_one({"_id": user_id, "institution_id": current_user.institution_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found in your institution")
    
    await db.db.users.update_one({"_id": user_id}, {"$set": {"role": new_role, "updated_at": datetime.utcnow()}})
    return {"status": "success", "message": f"User role updated to {new_role}"}
