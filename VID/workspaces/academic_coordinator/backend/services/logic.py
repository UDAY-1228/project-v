import os
import json
from typing import List, Dict, Any
from core.backend.database.connection import db

# Use the JSON file as a fallback or for initial data
DATABASE_JSON = os.path.join(os.path.dirname(__file__), "..", "..", "database", "database.json")

async def get_academic_data(collection_name: str, institution_id: str):
    # Try MongoDB first
    try:
        cursor = db[collection_name].find({"institution_id": institution_id})
        data = await cursor.to_list(length=100)
        if data:
            return data
    except Exception:
        pass

    # Fallback to local JSON
    try:
        with open(DATABASE_JSON, 'r') as f:
            data = json.load(f)
            return data.get(collection_name, [])
    except Exception as e:
        print(f"Error reading academic database: {e}")
        return []

async def create_academic_item(collection_name: str, item_data: Dict[str, Any]):
    try:
        result = await db[collection_name].insert_one(item_data)
        return str(result.inserted_id)
    except Exception:
        # If DB fails, we just return a mock ID for now
        return "mock_id_123"
