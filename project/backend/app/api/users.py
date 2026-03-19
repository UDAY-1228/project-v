"""Users & Institutions API stubs"""
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import UserResponse, UserUpdate, InstitutionCreate, Institution
from ...shared.services.rbac_service import get_current_user
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=list)
async def list_users(institution_id: str = None, role: str = None, current_user=Depends(get_current_user)):
    users = get_collection("users")
    query = {}
    if institution_id:
        query["institution_id"] = institution_id
    if role:
        query["role"] = role
    docs = await users.find(query).to_list(500)
    for d in docs:
        d["id"] = str(d.pop("_id"))
        d.pop("password", None)
    return docs

@router.get("/{user_id}")
async def get_user(user_id: str, current_user=Depends(get_current_user)):
    from bson import ObjectId
    users = get_collection("users")
    user = await users.find_one({"_id": ObjectId(user_id)})
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user.pop("_id"))
    user.pop("password", None)
    return user

@router.put("/{user_id}")
async def update_user(user_id: str, update: UserUpdate, current_user=Depends(get_current_user)):
    from bson import ObjectId
    users = get_collection("users")
    await users.update_one({"_id": ObjectId(user_id)}, {"$set": {**update.dict(exclude_none=True), "updated_at": datetime.utcnow()}})
    return {"message": "User updated"}

@router.delete("/{user_id}")
async def deactivate_user(user_id: str, current_user=Depends(get_current_user)):
    from bson import ObjectId
    users = get_collection("users")
    await users.update_one({"_id": ObjectId(user_id)}, {"$set": {"is_active": False, "updated_at": datetime.utcnow()}})
    return {"message": "User deactivated"}
