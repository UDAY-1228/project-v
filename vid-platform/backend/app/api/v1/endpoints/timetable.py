from fastapi import APIRouter
from app.db.mongodb import get_database

router = APIRouter()

@router.get("/")
async def get_timetable(grade: str = "10", section: str = "A"):
    return {
        "grade": grade,
        "section": section,
        "schedule": [
            {"day": "Monday", "periods": [
                {"time": "09:00 - 10:00", "subject": "Math", "teacher": "Dr. Smith"},
                {"time": "10:00 - 11:00", "subject": "Physics", "teacher": "Prof. Jones"}
            ]},
            {"day": "Tuesday", "periods": [
                {"time": "09:00 - 10:00", "subject": "History", "teacher": "Ms. Doe"},
                {"time": "10:00 - 11:00", "subject": "Biology", "teacher": "Dr. Brown"}
            ]}
        ]
    }
