"""
Analytics API — Dashboard data, at-risk students, institution stats
"""
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.services.rbac_service import get_current_user
from ...shared.ml.attendance_predictor import AtRiskPredictor
from datetime import date, timedelta

router = APIRouter()
predictor = AtRiskPredictor()


@router.get("/institution/{institution_id}/dashboard")
async def institution_dashboard(
    institution_id: str,
    current_user=Depends(get_current_user),
):
    """Comprehensive institution analytics dashboard"""
    users = get_collection("users")
    attendance = get_collection("attendance_logs")
    fees = get_collection("fees_invoices")
    exams = get_collection("exam_results")

    # User counts by role
    students = await users.count_documents({"institution_id": institution_id, "role": "student"})
    faculty = await users.count_documents({"institution_id": institution_id, "role": "faculty"})

    # Today's attendance
    today = date.today().isoformat()
    today_present = await attendance.count_documents({
        "institution_id": institution_id,
        "date": today,
        "status": {"$in": ["present", "late"]},
    })

    # Fee collection (current month)
    paid_fees = await fees.count_documents({
        "institution_id": institution_id,
        "status": "paid",
    })
    overdue_fees = await fees.count_documents({
        "institution_id": institution_id,
        "status": "overdue",
    })

    # Weekly attendance trend
    trend = []
    for i in range(7):
        d = (date.today() - timedelta(days=i)).isoformat()
        count = await attendance.count_documents({
            "institution_id": institution_id,
            "date": d,
            "status": {"$in": ["present", "late"]},
        })
        trend.append({"date": d, "present": count})

    return {
        "total_students": students,
        "total_faculty": faculty,
        "today_attendance": today_present,
        "today_attendance_pct": round((today_present / students * 100) if students > 0 else 0, 1),
        "fee_collected": paid_fees,
        "fee_overdue": overdue_fees,
        "weekly_attendance_trend": trend[::-1],
    }


@router.get("/at-risk/{institution_id}")
async def get_at_risk_students(
    institution_id: str,
    top_n: int = 20,
    current_user=Depends(get_current_user),
):
    """Get at-risk student predictions using ML model"""
    users = get_collection("users")
    attendance = get_collection("attendance_logs")

    students = await users.find(
        {"institution_id": institution_id, "role": "student", "is_active": True}
    ).to_list(500)

    at_risk_list = []
    for student in students:
        sid = str(student["_id"])
        logs = await attendance.find({"student_id": sid}).to_list(200)

        total = len(logs)
        present = sum(1 for l in logs if l["status"] in ["present", "late"])
        absent = sum(1 for l in logs if l["status"] == "absent")
        late = sum(1 for l in logs if l["status"] == "late")
        pct = (present / total * 100) if total > 0 else 100

        student_data = {
            "student_id": sid,
            "attendance_pct": pct,
            "absent_days": absent,
            "late_days": late,
            "avg_marks": 65,  # TODO: pull from exam_results
            "fee_payment_delay_days": 0,  # TODO: pull from fees
            "assignments_submitted_pct": 80,
            "parent_meetings_attended": 1,
        }

        prediction = predictor.predict_risk(student_data)
        if prediction["risk_level"] in ["high", "medium"]:
            at_risk_list.append({
                "student_id": sid,
                "full_name": student["full_name"],
                "class": student.get("class_name", ""),
                **prediction,
            })

    # Sort by risk score descending
    at_risk_list.sort(key=lambda x: x["risk_score"], reverse=True)
    return {"at_risk_students": at_risk_list[:top_n], "total_at_risk": len(at_risk_list)}


@router.get("/super-admin/platform")
async def platform_analytics(current_user=Depends(get_current_user)):
    """Super admin platform-wide analytics"""
    institutions = get_collection("institutions")
    users = get_collection("users")

    total_institutions = await institutions.count_documents({})
    active_institutions = await institutions.count_documents({"is_active": True})
    total_users = await users.count_documents({})
    total_students = await users.count_documents({"role": "student"})

    # Institution-wise counts
    pipeline = [
        {"$group": {"_id": "$institution_id", "user_count": {"$sum": 1}}},
        {"$sort": {"user_count": -1}},
        {"$limit": 10}
    ]
    top_institutions = await users.aggregate(pipeline).to_list(10)

    return {
        "total_institutions": total_institutions,
        "active_institutions": active_institutions,
        "total_users": total_users,
        "total_students": total_students,
        "top_institutions_by_users": top_institutions,
    }
