from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
async def login():
    return {"message": "Login successful"}

@router.post("/refresh")
async def refresh_token():
    return {"message": "Token refreshed"}
