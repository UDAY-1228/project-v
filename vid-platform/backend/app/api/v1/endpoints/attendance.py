from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
async def get_attendance_summary():
    return {"present": 850, "absent": 50, "late": 20}

@router.post("/verify")
async def verify_face():
    return {"status": "verified", "student_id": "ST123"}
