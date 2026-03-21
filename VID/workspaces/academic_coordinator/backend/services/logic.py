from typing import List, Dict, Any
from core.backend.database.connection import db

async def get_data(collection_name: str, institution_id: str):
    try:
        # Support both MongoDB direct queries and converting ObjectIds
        cursor = db.db[collection_name].find({"institution_id": institution_id})
        data = await cursor.to_list(length=1000)
        
        # Format the output so _id is cast to a string for JSON serialization
        formatted = []
        for d in data:
            if "_id" in d:
                d["_id"] = str(d["_id"])
            formatted.append(d)
        return formatted
    except Exception as e:
        print(f"MongoDB Error in get_data({collection_name}): {e}")
        return []

async def create_item(collection_name: str, item_data: Dict[str, Any]):
    try:
        result = await db.db[collection_name].insert_one(item_data)
        return str(result.inserted_id)
    except Exception as e:
        print(f"MongoDB Error in create_item({collection_name}): {e}")
        return None
