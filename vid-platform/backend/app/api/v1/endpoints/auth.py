from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.db.mongodb import get_database
from app.core.security import verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    username: str

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = get_database()
    user = await db.users.find_one({"username": form_data.username})
    
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Get role name
    from bson import ObjectId
    role_doc = await db.roles.find_one({"_id": ObjectId(user["role_id"])})
    role_name = role_doc["name"] if role_doc else "Student"

    access_token = create_access_token(subject=user["username"])
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "role": role_name,
        "username": user["username"]
    }

@router.get("/me")
async def read_users_me(current_user: str = Depends(lambda: "admin")): # Placeholder dependency
    return {"username": current_user}
