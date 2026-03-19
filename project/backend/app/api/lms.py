"""LMS API — Courses, Assignments, AI Homework Helper, Submissions"""
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from ...shared.database import get_collection
from ...shared.models.schemas import Course, Assignment, Submission
from ...shared.services.rbac_service import get_current_user
from ...shared.ml.homework_ai import HomeworkAIHelper

router = APIRouter()
ai_helper = HomeworkAIHelper()


@router.post("/courses", response_model=dict)
async def create_course(course: Course, current_user=Depends(get_current_user)):
    courses = get_collection("courses")
    doc = course.dict()
    doc["created_at"] = datetime.utcnow()
    result = await courses.insert_one(doc)
    return {"message": "Course created", "id": str(result.inserted_id)}


@router.get("/courses/{institution_id}")
async def list_courses(institution_id: str, class_name: Optional[str] = None, current_user=Depends(get_current_user)):
    courses = get_collection("courses")
    query = {"institution_id": institution_id}
    if class_name:
        query["class_name"] = class_name
    docs = await courses.find(query).to_list(100)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/assignments", response_model=dict)
async def create_assignment(assignment: Assignment, current_user=Depends(get_current_user)):
    assignments = get_collection("assignments")
    doc = assignment.dict()
    doc["created_at"] = datetime.utcnow()
    result = await assignments.insert_one(doc)
    return {"message": "Assignment created", "id": str(result.inserted_id)}


@router.get("/assignments/{institution_id}/{class_name}")
async def get_assignments(institution_id: str, class_name: str, current_user=Depends(get_current_user)):
    assignments = get_collection("assignments")
    docs = await assignments.find({"institution_id": institution_id, "class_name": class_name}).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/submit/{assignment_id}")
async def submit_assignment(
    assignment_id: str,
    student_id: str = Form(...),
    text_response: Optional[str] = Form(None),
    files: list[UploadFile] = File(default=[]),
    current_user=Depends(get_current_user),
):
    import os, uuid
    from ...shared.config import settings
    saved_files = []
    for f in files:
        fn = f"{uuid.uuid4().hex}_{f.filename}"
        path = os.path.join(settings.UPLOAD_PATH, "submissions", fn)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as fp:
            fp.write(await f.read())
        saved_files.append(f"/uploads/submissions/{fn}")

    submissions = get_collection("submissions")
    doc = {
        "assignment_id": assignment_id,
        "student_id": student_id,
        "submitted_at": datetime.utcnow(),
        "files": saved_files,
        "text_response": text_response,
        "ai_checked": False,
    }
    result = await submissions.insert_one(doc)
    return {"message": "Assignment submitted", "id": str(result.inserted_id)}


@router.post("/grade/{submission_id}")
async def grade_submission(submission_id: str, body: dict, current_user=Depends(get_current_user)):
    from bson import ObjectId
    submissions = get_collection("submissions")
    await submissions.update_one(
        {"_id": ObjectId(submission_id)},
        {"$set": {
            "marks_obtained": body.get("marks"),
            "feedback": body.get("feedback"),
            "graded_by": current_user["id"],
            "graded_at": datetime.utcnow(),
        }}
    )
    return {"message": "Submission graded"}


@router.post("/homework-helper")
async def homework_ai_helper(body: dict, current_user=Depends(get_current_user)):
    """AI homework hint generator"""
    question = body.get("question", "")
    subject = body.get("subject", "general")
    class_level = body.get("class_level", 10)

    if not question:
        raise HTTPException(status_code=400, detail="Question is required")

    result = ai_helper.get_hint(question, subject, class_level)
    return result


@router.get("/practice-questions")
async def get_practice_questions(
    subject: str, topic: str, class_level: int = 10, count: int = 5,
    current_user=Depends(get_current_user),
):
    """Generate AI practice questions"""
    questions = ai_helper.generate_practice_questions(subject, topic, class_level, count)
    return {"questions": questions, "subject": subject, "topic": topic}
