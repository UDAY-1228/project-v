from core.backend.database.connection import db
from datetime import datetime

async def get_items(institution_id: str):
    cursor = db.db.items.find({"institution_id": institution_id})
    items = await cursor.to_list(length=100)
    for item in items:
        item["_id"] = str(item["_id"])
    return items

async def create_item(item_data: dict, institution_id: str):
    item_data["institution_id"] = institution_id
    item_data["created_at"] = item_data["updated_at"] = datetime.utcnow()
    res = await db.db.items.insert_one(item_data)
    return {"id": str(res.inserted_id), **item_data}

async def get_item_by_id(item_id: str, institution_id: str):
    item = await db.db.items.find_one({"_id": item_id, "institution_id": institution_id})
    if item:
        item["_id"] = str(item["_id"])
    return item
