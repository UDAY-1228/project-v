from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import create_model
from typing import List, Any, Dict, Optional, Type
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

class VIDBackendGenerator:
    def __init__(self, service_name: str, mongo_uri: str):
        self.app = FastAPI(title=f"VID {service_name} API")
        self.service_name = service_name
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client.vid_core

    def auto_generate_routes(self, module_name: str, schema_fields: Dict[str, Any]):
        """
        Creates a new Pydantic model and corresponding CRUD routes for a given module.
        """
        # 1. Create Pydantic Model Dynamically
        Model = create_model(f"{module_name}Model", **schema_fields, __base__=None)
        
        # 2. Add Routes
        @self.app.get(f"/{module_name.lower()}", response_model=List[Model], tags=[module_name])
        async def list_items():
            cursor = self.db[module_name.lower()].find()
            return await cursor.to_list(length=100)

        @self.app.post(f"/{module_name.lower()}", response_model=Model, status_code=201, tags=[module_name])
        async def create_item(item: Model):
            item_dict = item.dict()
            item_dict["created_at"] = datetime.utcnow()
            await self.db[module_name.lower()].insert_one(item_dict)
            return item

        print(f"[*] Auto-generated routes for: {module_name}")

# Example Usage for Super Admin
if __name__ == "__main__":
    generator = VIDBackendGenerator("Super Admin", os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    
    # Auto-generate 'Institutions' based on frontend requirement
    generator.auto_generate_routes("Institution", {
        "name": (str, ...),
        "institution_id": (str, ...),
        "admin_email": (str, ...),
        "status": (str, "active"),
        "created_at": (datetime, None)
    })
    
    import uvicorn
    uvicorn.run(generator.app, host="0.0.0.0", port=8000)
