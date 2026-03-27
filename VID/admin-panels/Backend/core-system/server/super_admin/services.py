from ..core.database.mongo_connection import db
from .models import InstitutionCreate
from ..core.auth.password_handler import get_password_hash, verify_password
from ..core.auth.jwt_handler import signJWT
import os

SUPER_ADMIN_USERNAME = os.getenv("SUPER_ADMIN_USERNAME", "superadmin")
SUPER_ADMIN_PASSWORD_HASH = get_password_hash(os.getenv("SUPER_ADMIN_PASSWORD", "superpassword"))

async def super_admin_login(username, password):
    if username == SUPER_ADMIN_USERNAME and verify_password(password, SUPER_ADMIN_PASSWORD_HASH):
        return signJWT(username, role="super_admin")
    return None

async def create_institution(institution: InstitutionCreate):
    existing = await db.db.institutions.find_one({"institution_id": institution.institution_id})
    if existing:
        return None
    
    hashed_pass = get_password_hash(institution.admin_password)
    new_institution = institution.dict()
    new_institution["admin_password"] = hashed_pass
    
    await db.db.institutions.insert_one(new_institution)
    return new_institution

async def get_all_institutions():
    cursor = db.db.institutions.find({})
    institutions = await cursor.to_list(length=100)
    # Don't return password hashes
    for inst in institutions:
        inst["_id"] = str(inst["_id"])
        del inst["admin_password"]
    return institutions
