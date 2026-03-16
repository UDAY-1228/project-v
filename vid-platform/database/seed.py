import os
import sys
from datetime import datetime
from pymongo import MongoClient
import bcrypt

# Add project root to path to import models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models
from models import Role, Institution

def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def seed_database():
    client = MongoClient(os.getenv("MONGODB_URL", "mongodb://localhost:27017"))
    db = client["vid_platform"]

    print("Initializing collections and seeding default data...")

    # 1. Seed Roles
    roles = [
        {"name": "SuperAdmin", "permissions": ["all"]},
        {"name": "Admin", "permissions": ["manage_students", "manage_exams", "manage_fees", "manage_notices", "manage_timetable", "manage_clubs", "manage_feedback"]},
        {"name": "Teacher", "permissions": ["manage_homework", "manage_lms", "manage_results", "manage_practice", "manage_feedback"]},
        {"name": "Student", "permissions": ["view_homework", "view_lms", "view_results", "view_timetable"]},
        {"name": "Parent", "permissions": ["view_attendance", "view_results", "pay_fees"]}
    ]
    db.roles.delete_many({})
    db.roles.insert_many(roles)
    print(f"Seeded {len(roles)} roles.")

    # Get Role IDs
    role_map = {r["name"]: str(db.roles.find_one({"name": r["name"]})["_id"]) for r in roles}

    # 2. Seed default Institution
    institution = {
        "name": "Dolla Academic Excellence",
        "code": "DAE001",
        "license_type": "premium",
        "settings": {
            "attendance_threshold": 75.0,
            "theme": "indigo",
            "branding_url": "https://placehold.co/200x50"
        },
        "created_at": datetime.utcnow()
    }
    db.institutions.delete_many({})
    inst_id = str(db.institutions.insert_one(institution).inserted_id)
    print(f"Seeded default institution: {institution['name']}")

    # 3. Seed Users
    users = [
        {
            "username": "superadmin",
            "email": "superadmin@dolla.edu",
            "hashed_password": get_password_hash("admin123"),
            "role_id": role_map["SuperAdmin"],
            "inst_id": inst_id,
            "is_active": True,
            "created_at": datetime.utcnow()
        },
        {
            "username": "admin",
            "email": "admin@dolla.edu",
            "hashed_password": get_password_hash("admin123"),
            "role_id": role_map["Admin"],
            "inst_id": inst_id,
            "is_active": True,
            "created_at": datetime.utcnow()
        },
        {
            "username": "teacher",
            "email": "teacher@dolla.edu",
            "hashed_password": get_password_hash("teacher123"),
            "role_id": role_map["Teacher"],
            "inst_id": inst_id,
            "is_active": True,
            "created_at": datetime.utcnow()
        }
    ]
    db.users.delete_many({})
    db.users.insert_many(users)
    print(f"Seeded {len(users)} default users.")

    # 4. Other collections (Empty initialization)
    collections = [
        "students", "teachers", "exams", "fees", "notices", 
        "homework", "feedback", "timetable", "notifications", "lms_content"
    ]
    for coll in collections:
        if coll not in db.list_collection_names():
            db.create_collection(coll)
            print(f"Created collection: {coll}")

    print("Database seeding completed successfully.")

if __name__ == "__main__":
    seed_database()
