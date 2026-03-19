"""Institutions API"""
from fastapi import APIRouter, HTTPException, Depends
from ...shared.database import get_collection
from ...shared.models.schemas import InstitutionCreate
from ...shared.services.rbac_service import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=dict)
async def create_institution(inst: InstitutionCreate, current_user=Depends(get_current_user)):
    insts = get_collection("institutions")
    existing = await insts.find_one({"code": inst.code})
    if existing:
        raise HTTPException(status_code=400, detail="Institution code already exists")
    doc = inst.dict()
    doc["created_at"] = datetime.utcnow()
    doc["created_by"] = current_user["id"]
    result = await insts.insert_one(doc)
    return {"message": "Institution created", "id": str(result.inserted_id)}

@router.get("/")
async def list_institutions(current_user=Depends(get_current_user)):
    insts = get_collection("institutions")
    docs = await insts.find({}).to_list(200)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs

@router.get("/{institution_id}")
async def get_institution(institution_id: str, current_user=Depends(get_current_user)):
    from bson import ObjectId
    insts = get_collection("institutions")
    inst = await insts.find_one({"_id": ObjectId(institution_id)})
    if not inst:
        raise HTTPException(status_code=404, detail="Institution not found")
    inst["_id"] = str(inst["_id"])
    return inst

@router.put("/{institution_id}")
async def update_institution(institution_id: str, body: dict, current_user=Depends(get_current_user)):
    from bson import ObjectId
    insts = get_collection("institutions")
    body["updated_at"] = datetime.utcnow()
    await insts.update_one({"_id": ObjectId(institution_id)}, {"$set": body})
    return {"message": "Institution updated"}
