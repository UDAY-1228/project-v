"""Notifications API"""
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import Notification
from ...shared.services.rbac_service import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=dict)
async def create_notification(notif: Notification, current_user=Depends(get_current_user)):
    notifs = get_collection("notifications")
    doc = notif.dict()
    doc["created_at"] = datetime.utcnow()
    result = await notifs.insert_one(doc)
    return {"message": "Notification sent", "id": str(result.inserted_id)}

@router.get("/my")
async def get_my_notifications(current_user=Depends(get_current_user)):
    notifs = get_collection("notifications")
    docs = await notifs.find({"user_id": current_user["id"]}).sort("created_at", -1).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs

@router.put("/mark-read/{notif_id}")
async def mark_read(notif_id: str, current_user=Depends(get_current_user)):
    from bson import ObjectId
    notifs = get_collection("notifications")
    await notifs.update_one({"_id": ObjectId(notif_id)}, {"$set": {"read": True}})
    return {"message": "Marked as read"}
