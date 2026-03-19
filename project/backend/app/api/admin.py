"""Admin Tools API — Audit logs, backups, system stats"""
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import AuditLog
from ...shared.services.rbac_service import get_current_user, require_role
from ...shared.models.schemas import UserRole
from datetime import datetime

router = APIRouter()

@router.get("/audit-logs")
async def get_audit_logs(institution_id: str = None, limit: int = 100, current_user=Depends(get_current_user)):
    logs = get_collection("audit_logs")
    query = {}
    if institution_id:
        query["institution_id"] = institution_id
    docs = await logs.find(query).sort("timestamp", -1).to_list(limit)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs

@router.post("/audit-logs", response_model=dict)
async def log_action(log: AuditLog, current_user=Depends(get_current_user)):
    logs = get_collection("audit_logs")
    doc = log.dict()
    doc["timestamp"] = datetime.utcnow()
    await logs.insert_one(doc)
    return {"message": "Logged"}

@router.get("/system-stats")
async def system_stats(current_user=Depends(require_role(UserRole.SUPER_ADMIN))):
    from ...shared.database import get_db
    db = get_db()
    stats = await db.command("dbStats")
    return {
        "collections": stats.get("collections"),
        "data_size_mb": round(stats.get("dataSize", 0) / 1024 / 1024, 2),
        "storage_size_mb": round(stats.get("storageSize", 0) / 1024 / 1024, 2),
        "indexes": stats.get("indexes"),
    }
