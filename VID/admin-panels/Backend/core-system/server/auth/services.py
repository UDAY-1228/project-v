from ..core.database.mongo_connection import db
from ..core.auth.password_handler import get_password_hash, verify_password
from ..core.auth.jwt_handler import signJWT
import os

SUPER_ADMIN_USERNAME = os.getenv("SUPER_ADMIN_USERNAME", "superadmin")
SUPER_ADMIN_PASSWORD_HASH = get_password_hash(os.getenv("SUPER_ADMIN_PASSWORD", "superpassword"))

async def unified_login(username, password, institution_id=None):
    # Check Super Admin
    if not institution_id and username == SUPER_ADMIN_USERNAME:
        if verify_password(password, SUPER_ADMIN_PASSWORD_HASH):
            return signJWT(username, role="super_admin")
    
    # Check Institution Admin
    if institution_id:
        inst = await db.db.institutions.find_one({"institution_id": institution_id, "admin_username": username})
        if inst and verify_password(password, inst["admin_password"]):
            return signJWT(username, role="admin", institution_id=institution_id)
        
        # Check ordinary user within institution
        user = await db.db.users.find_one({"username": username, "institution_id": institution_id})
        if user and verify_password(password, user["password"]):
            return {
                **signJWT(username, role=user["role"], institution_id=institution_id),
                "assigned_workspaces": user.get("assigned_workspaces", [])
            }
    
    return None
