"""
VID Academic Service – FastAPI Microservice
"""
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

app = FastAPI(title="VID Academic Service")

class ClassResponse(BaseModel):
    id: UUID
    name: str
    section: Optional[str]
    institution_id: str

@app.get("/health")
async def health():
    return {"status": "ok", "service": "academic-service"}

@app.get("/classes/", response_model=List[ClassResponse])
async def list_classes(x_institution_id: str = Header(None, alias="X-Institution-ID")):
    if not x_institution_id:
        return []
    # Mock data
    return [
        {"id": "550e8400-e29b-41d4-a716-446655440000", "name": "10th Grade", "section": "A", "institution_id": x_institution_id}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
