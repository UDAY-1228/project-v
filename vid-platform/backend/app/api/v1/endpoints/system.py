from fastapi import APIRouter

router = APIRouter()

@router.get("/config")
def get_platform_config():
    """Returns the unified configuration for transition between Web and Mobile."""
    return {
        "platform_name": "VID Platform",
        "version": "1.0.0",
        "modules": [
            {"id": "auth", "name": "Authentication", "enabled": True},
            {"id": "profiles", "name": "User Profiles", "enabled": True},
            {"id": "attendance", "name": "Smart Attendance", "enabled": True},
            {"id": "fees", "name": "Finance & Fees", "enabled": True},
            {"id": "lms", "name": "Learning Management", "enabled": True},
            {"id": "timetable", "name": "AI Timetable", "enabled": True},
            {"id": "exams", "name": "Exams & Results", "enabled": True},
            {"id": "analytics", "name": "Performance Analytics", "enabled": True},
            {"id": "messaging", "name": "Communication", "enabled": True},
            {"id": "notifications", "name": "Notifications", "enabled": True},
        ],
        "roles": ["Student", "Parent", "Teacher", "Admin", "SuperAdmin"],
        "api_base_url": "http://localhost:8000/api/v1"
    }

@router.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected", "storage": "available"}
