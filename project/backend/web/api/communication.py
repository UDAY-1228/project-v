"""Communication API — Notices, PTM Booking, Chat rooms"""
from datetime import datetime
from fastapi import APIRouter, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import Notice, Message, PTMSlot
from ...shared.services.rbac_service import get_current_user

router = APIRouter()


@router.post("/notices", response_model=dict)
async def create_notice(notice: Notice, current_user=Depends(get_current_user)):
    notices = get_collection("notices")
    doc = notice.dict()
    doc["published_at"] = datetime.utcnow()
    result = await notices.insert_one(doc)
    return {"message": "Notice published", "id": str(result.inserted_id)}


@router.get("/notices/{institution_id}")
async def get_notices(institution_id: str, current_user=Depends(get_current_user)):
    notices = get_collection("notices")
    docs = await notices.find({"institution_id": institution_id}).sort("published_at", -1).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/messages", response_model=dict)
async def send_message(message: Message, current_user=Depends(get_current_user)):
    messages = get_collection("messages")
    doc = message.dict()
    doc["sender_id"] = current_user["id"]
    doc["timestamp"] = datetime.utcnow()
    result = await messages.insert_one(doc)
    return {"message": "Message sent", "id": str(result.inserted_id)}


@router.get("/messages/{user_id}")
async def get_user_messages(user_id: str, current_user=Depends(get_current_user)):
    messages = get_collection("messages")
    docs = await messages.find({
        "$or": [{"sender_id": user_id}, {"receiver_id": user_id}]
    }).sort("timestamp", -1).to_list(100)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/ptm-slots", response_model=dict)
async def create_ptm_slots(slot: PTMSlot, current_user=Depends(get_current_user)):
    ptm = get_collection("ptm_slots")
    doc = slot.dict()
    result = await ptm.insert_one(doc)
    return {"message": "PTM slot created", "id": str(result.inserted_id)}


@router.post("/ptm-book/{slot_id}")
async def book_ptm(slot_id: str, body: dict, current_user=Depends(get_current_user)):
    from bson import ObjectId
    ptm = get_collection("ptm_slots")
    booking = {
        "parent_id": current_user["id"],
        "student_id": body.get("student_id"),
        "time": body.get("time"),
        "booked_at": datetime.utcnow(),
    }
    await ptm.update_one(
        {"_id": ObjectId(slot_id)},
        {"$push": {"booked_slots": booking}, "$inc": {"available_slots": -1}}
    )
    return {"message": "PTM booked successfully", "booking": booking}
