from fastapi import APIRouter
from app.db.mongodb import get_database

router = APIRouter()

@router.get("/summary")
async def get_summary():
    return {
        "students": 1250,
        "teachers": 85,
        "attendance_rate": 92.5,
        "fees_collected": 750000,
        "active_notices": 12,
        "revenue_trend": [12000, 15000, 13000, 18000, 22000, 20000],
        "attendance_trend": [95, 94, 92, 93, 89, 92]
    }
