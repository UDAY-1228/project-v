from fastapi import APIRouter
from app.db.mongodb import get_database

router = APIRouter()

@router.get("/")
async def get_exams():
    db = get_database()
    exams = await db.exams.find().to_list(100)
    # Mock data if empty
    if not exams:
        return [
            {"id": "1", "name": "Mid-Term Examination", "date": "2024-04-15", "status": "Upcoming"},
            {"id": "2", "name": "Annual Assessment", "date": "2024-06-10", "status": "Scheduled"}
        ]
    return exams

@router.get("/results/{student_id}")
async def get_results(student_id: str):
    return {
        "student_id": student_id,
        "results": [
            {"subject": "Mathematics", "marks": 85, "grade": "A"},
            {"subject": "Science", "marks": 78, "grade": "B+"},
            {"subject": "English", "marks": 92, "grade": "A+"}
        ]
    }
