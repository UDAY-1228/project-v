"""Exams API — Exam management, results, online tests"""
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import Exam, ExamResult
from ...shared.services.rbac_service import get_current_user

router = APIRouter()


@router.post("/", response_model=dict)
async def create_exam(exam: Exam, current_user=Depends(get_current_user)):
    exams = get_collection("exams")
    doc = exam.dict()
    doc["created_at"] = datetime.utcnow()
    doc["created_by"] = current_user["id"]
    result = await exams.insert_one(doc)
    return {"message": "Exam created", "id": str(result.inserted_id)}


@router.get("/{institution_id}/{class_name}")
async def list_exams(institution_id: str, class_name: str, current_user=Depends(get_current_user)):
    exams = get_collection("exams")
    docs = await exams.find({"institution_id": institution_id, "class_name": class_name}).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/results", response_model=dict)
async def publish_result(result: ExamResult, current_user=Depends(get_current_user)):
    results = get_collection("exam_results")
    doc = result.dict()
    doc["published_at"] = datetime.utcnow()
    doc["published"] = True
    r = await results.insert_one(doc)
    return {"message": "Result published", "id": str(r.inserted_id)}


@router.get("/results/{student_id}")
async def get_student_results(student_id: str, current_user=Depends(get_current_user)):
    results = get_collection("exam_results")
    docs = await results.find({"student_id": student_id, "published": True}).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.get("/class-report/{exam_id}")
async def class_exam_report(exam_id: str, current_user=Depends(get_current_user)):
    results = get_collection("exam_results")
    docs = await results.find({"exam_id": exam_id}).to_list(200)
    if not docs:
        return {"message": "No results found"}

    marks = [d["marks_obtained"] for d in docs]
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = sum(1 for d in docs if d.get("grade", "F") != "F")

    return {
        "exam_id": exam_id,
        "total_students": len(docs),
        "average": round(avg, 2),
        "highest": highest,
        "lowest": lowest,
        "pass_count": passed,
        "fail_count": len(docs) - passed,
        "pass_percentage": round(passed / len(docs) * 100, 2),
    }
