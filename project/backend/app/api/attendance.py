"""
Attendance API — AI-powered attendance tracking system
Supports: Manual, Face AI, QR scan, Kiosk mode
"""
from datetime import datetime, date
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends, Query

from ...shared.database import get_collection
from ...shared.models.schemas import AttendanceLog, AttendanceSummary, AttendanceStatus
from ...shared.services.rbac_service import get_current_user, require_role

router = APIRouter()


@router.post("/mark", response_model=dict)
async def mark_attendance(
    log: AttendanceLog,
    current_user=Depends(get_current_user),
):
    """Mark attendance for a student (manual/AI)"""
    attendance = get_collection("attendance_logs")

    # Check duplicate
    existing = await attendance.find_one({
        "student_id": log.student_id,
        "date": log.date,
        "subject": log.subject,
    })
    if existing:
        # Update if override
        await attendance.update_one(
            {"_id": existing["_id"]},
            {"$set": {
                "status": log.status,
                "method": log.method,
                "override_reason": log.override_reason,
                "updated_at": datetime.utcnow(),
            }}
        )
        return {"message": "Attendance updated", "action": "updated"}

    doc = log.dict()
    doc["marked_by"] = current_user["id"]
    doc["timestamp"] = datetime.utcnow()
    result = await attendance.insert_one(doc)
    return {"message": "Attendance marked", "id": str(result.inserted_id)}


@router.post("/bulk-mark")
async def bulk_mark_attendance(
    logs: List[AttendanceLog],
    current_user=Depends(get_current_user),
):
    """Bulk mark attendance for entire class"""
    attendance = get_collection("attendance_logs")
    marked = 0
    for log in logs:
        doc = log.dict()
        doc["marked_by"] = current_user["id"]
        doc["timestamp"] = datetime.utcnow()
        await attendance.update_one(
            {"student_id": log.student_id, "date": log.date, "subject": log.subject},
            {"$set": doc},
            upsert=True
        )
        marked += 1
    return {"message": f"Bulk attendance marked for {marked} students"}


@router.get("/summary/{student_id}", response_model=AttendanceSummary)
async def get_attendance_summary(
    student_id: str,
    from_date: Optional[str] = Query(None),
    to_date: Optional[str] = Query(None),
    current_user=Depends(get_current_user),
):
    """Get attendance summary for a student"""
    attendance = get_collection("attendance_logs")
    query: dict = {"student_id": student_id}

    if from_date and to_date:
        query["date"] = {"$gte": from_date, "$lte": to_date}

    logs = await attendance.find(query).to_list(length=None)

    total = len(logs)
    present = sum(1 for l in logs if l["status"] in ["present", "late"])
    absent = sum(1 for l in logs if l["status"] == "absent")
    late = sum(1 for l in logs if l["status"] == "late")
    percentage = round((present / total * 100) if total > 0 else 0, 2)

    return AttendanceSummary(
        student_id=student_id,
        total_days=total,
        present_days=present,
        absent_days=absent,
        late_days=late,
        percentage=percentage,
        at_risk=percentage < 75,
    )


@router.get("/class/{institution_id}/{class_name}/{section}")
async def get_class_attendance(
    institution_id: str,
    class_name: str,
    section: str,
    date_str: str = Query(..., alias="date"),
    current_user=Depends(get_current_user),
):
    """Get attendance data for a class on a specific date"""
    attendance = get_collection("attendance_logs")
    logs = await attendance.find({
        "institution_id": institution_id,
        "class_name": class_name,
        "section": section,
        "date": date_str,
    }).to_list(length=None)
    return {"date": date_str, "class": class_name, "section": section, "attendance": logs}


@router.get("/dashboard/{institution_id}")
async def get_attendance_dashboard(
    institution_id: str,
    current_user=Depends(get_current_user),
):
    """Institution-level attendance dashboard with analytics"""
    attendance = get_collection("attendance_logs")

    today = date.today().isoformat()
    today_logs = await attendance.find({"institution_id": institution_id, "date": today}).to_list(1000)

    total_today = len(today_logs)
    present_today = sum(1 for l in today_logs if l["status"] in ["present", "late"])

    # At-risk students (< 75% attendance)
    pipeline = [
        {"$match": {"institution_id": institution_id}},
        {"$group": {
            "_id": "$student_id",
            "total": {"$sum": 1},
            "present": {"$sum": {"$cond": [{"$in": ["$status", ["present", "late"]]}, 1, 0]}}
        }},
        {"$project": {
            "student_id": "$_id",
            "percentage": {"$multiply": [{"$divide": ["$present", "$total"]}, 100]}
        }},
        {"$match": {"percentage": {"$lt": 75}}}
    ]

    at_risk = await attendance.aggregate(pipeline).to_list(100)

    return {
        "today": {
            "total_students": total_today,
            "present": present_today,
            "absent": total_today - present_today,
            "attendance_rate": round((present_today / total_today * 100) if total_today > 0 else 0, 2),
        },
        "at_risk_students": len(at_risk),
        "at_risk_list": at_risk[:10],
    }


@router.put("/override/{log_id}")
async def override_attendance(
    log_id: str,
    body: dict,
    current_user=Depends(get_current_user),
):
    """Override attendance status with reason"""
    attendance = get_collection("attendance_logs")
    from bson import ObjectId
    result = await attendance.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": {
            "status": body["status"],
            "override_reason": body.get("reason"),
            "overridden_by": current_user["id"],
            "updated_at": datetime.utcnow(),
        }}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Attendance log not found")
    return {"message": "Attendance overridden successfully"}


@router.get("/student/{student_id}/history")
async def get_student_history(
    student_id: str,
    subject: Optional[str] = None,
    current_user=Depends(get_current_user),
):
    """Get full attendance history for a student"""
    attendance = get_collection("attendance_logs")
    query = {"student_id": student_id}
    if subject:
        query["subject"] = subject

    logs = await attendance.find(query).sort("date", -1).to_list(200)
    return logs


@router.get("/flags/{institution_id}")
async def get_flagged_cases(
    institution_id: str,
    current_user=Depends(get_current_user),
):
    """Get flagged attendance cases (AI anomalies, low attendance)"""
    attendance = get_collection("attendance_logs")
    flags = await attendance.find({
        "institution_id": institution_id,
        "ai_confidence": {"$lt": 0.7},
    }).to_list(50)
    return {"flagged_cases": flags, "count": len(flags)}
