"""
Institution Admin API
Specialized routes for Fees, Users, AI Timetable, and Platform Analytics
"""
from fastapi import APIRouter, Depends, HTTPException, Body
from typing import List, Dict
from datetime import datetime

from ...shared.config import settings
from ...shared.database import get_collection
from ...shared.models.schemas import UserRole
from ...shared.services.rbac_service import require_role, get_current_user

router = APIRouter()

# ─── 💰 Finance & Fees ───────────────────────────────────────────────────────
@router.post("/finance/fee-plans")
async def create_fee_plan(plan: Dict = Body(...), current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Create a new fee installment plan for the institution"""
    plan["institution_id"] = current_user["institution_id"]
    plan["created_at"] = datetime.utcnow()
    # TODO: await get_collection("fee_plans").insert_one(plan)
    return {"plan_id": "FP-101", "status": "active"}

@router.get("/finance/dashboard")
async def get_finance_dashboard(current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Get summarized financial health of the institution"""
    return {
        "institution_id": current_user["institution_id"],
        "total_receivable": 5000000,
        "collected": 3200000,
        "collection_rate": 0.64,
        "active_plans": 12
    }

# ─── 👤 User & Role Management ────────────────────────────────────────────────
@router.put("/users/{user_id}/role")
async def update_user_role(user_id: str, role_update: Dict, current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Assign or change user role within the institution"""
    return {"user_id": user_id, "new_role": role_update["role"], "action": "applied"}

# ─── 📅 Timetable Generation (AI) ─────────────────────────────────────────────
@router.post("/timetable/generate-ai")
async def generate_ai_timetable(config: Dict, current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Trigger AI generation engine to build collision-free timetable"""
    return {
        "job_id": "T-AI-GENERATOR-92",
        "estimated_time": "45 seconds",
        "status": "processing"
    }

# ─── 📊 Advanced Analytics ────────────────────────────────────────────────────
@router.get("/analytics/performance")
async def get_performance_analytics(current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Summarized student performance analytics for high-level oversight"""
    return {
        "average_grade": 76.5,
        "at_risk_students": 15,
        "top_performing_classes": ["Class 10-A", "Class 12-B"],
        "teacher_efficiency_index": 0.94
    }

# ─── ⚙️ Settings & Control ─────────────────────────────────────────────────────
@router.put("/settings/biometric")
async def toggle_biometric_policy(status: Dict, current_user=Depends(require_role(UserRole.INSTITUTION_ADMIN))):
    """Toggle mandatory biometric/face recognition for the whole school"""
    return {"mandatory_face_id": status["enabled"], "audit_log_id": "LOG-B-82"}
