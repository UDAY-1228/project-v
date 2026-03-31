from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class AuthToken(BaseModel):
    access_token: str
    token_type: str

class Notice(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Timetable(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    schedule: List[dict] # {day: str, time: str, class: str}

class UserProfile(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    full_name: str
    role: str
    email: str
    avatar_url: Optional[str] = None
