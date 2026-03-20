import os
import json
from datetime import datetime
from core.backend.database.connection import db

# Use the JSON file as a fallback or for initial data
DATABASE_JSON = os.path.join(os.path.dirname(__file__), "..", "..", "database", "database.json")

async def get_transport_data(collection_name: str, institution_id: str):
    # Try MongoDB first
    cursor = db.db[collection_name].find({"institution_id": institution_id})
    items = await cursor.to_list(length=100)
    
    # If MongoDB is empty, check JSON mock
    if not items and os.path.exists(DATABASE_JSON):
        try:
            with open(DATABASE_JSON, 'r') as f:
                data = json.load(f)
                items = data.get(collection_name, [])
        except Exception as e:
            print(f"Error reading JSON database: {e}")
            
    for item in items:
        if "_id" in item:
            item["_id"] = str(item["_id"])
    return items

async def create_transport_item(collection_name: str, item_data: dict, institution_id: str):
    item_data["institution_id"] = institution_id
    item_data["created_at"] = item_data["updated_at"] = datetime.utcnow()
    res = await db.db[collection_name].insert_one(item_data)
    return {"id": str(res.inserted_id), **item_data}
