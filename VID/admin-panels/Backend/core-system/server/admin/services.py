from ..core.database.mongo_connection import db
from .models import UserCreate, UserBase
from ..core.auth.password_handler import get_password_hash, verify_password
from ..core.auth.jwt_handler import signJWT
from datetime import datetime
import uuid

async def admin_login(username, password, institution_id):
    inst = await db.db.institutions.find_one({"institution_id": institution_id, "admin_username": username})
    if inst and verify_password(password, inst["admin_password"]):
        return signJWT(username, role="admin", institution_id=institution_id)
    return None

async def create_user(user: UserCreate, institution_id: str):
    existing = await db.db.users.find_one({"username": user.username, "institution_id": institution_id})
    if existing:
        return None
    
    hashed_pass = get_password_hash(user.password)
    new_user = user.dict()
    new_user["password"] = hashed_pass
    new_user["institution_id"] = institution_id
    new_user["created_at"] = datetime.utcnow()
    new_user["user_id"] = str(uuid.uuid4())
    
    await db.db.users.insert_one(new_user)
    # Don't return password hash
    del new_user["password"]
    return new_user

async def list_institution_users(institution_id: str):
    cursor = db.db.users.find({"institution_id": institution_id})
    users = await cursor.to_list(length=100)
    # Cleanup for response
    for u in users:
        u["_id"] = str(u["_id"])
        del u["password"]
    return users
