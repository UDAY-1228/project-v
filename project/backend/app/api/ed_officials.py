"""Ed Officials API — Oversight dashboards, compliance reports"""
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.services.rbac_service import get_current_user
from datetime import datetime

router = APIRouter()

@router.get("/compliance-dashboard")
async def compliance_dashboard(current_user=Depends(get_current_user)):
    institutions = get_collection("institutions")
    users = get_collection("users")
    total_inst = await institutions.count_documents({})
    active_inst = await institutions.count_documents({"is_active": True})
    total_students = await users.count_documents({"role": "student"})
    return {
        "total_institutions": total_inst,
        "active_institutions": active_inst,
        "total_students": total_students,
        "compliance_rate": 92.5,
        "last_updated": datetime.utcnow().isoformat(),
    }

@router.get("/institutions-report")
async def institutions_report(current_user=Depends(get_current_user)):
    institutions = get_collection("institutions")
    docs = await institutions.find({}).to_list(200)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs
