from fastapi import APIRouter
from app.db.mongodb import get_database

router = APIRouter()

@router.get("/courses")
async def get_courses():
    return [
        {"id": "c1", "title": "Advanced Mathematics", "instructor": "Dr. Smith", "progress": 65},
        {"id": "c2", "title": "Modern Physics", "instructor": "Prof. Jones", "progress": 40}
    ]

@router.get("/assignments")
async def get_assignments():
    return [
        {"id": "a1", "title": "Calculus Problem Set 1", "due_date": "2024-03-25", "status": "Pending"},
        {"id": "a2", "title": "Circuit Design Lab Report", "due_date": "2024-03-30", "status": "Submitted"}
    ]
