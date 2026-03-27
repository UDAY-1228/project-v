from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Institution(BaseModel):
    name: str
    institution_id: str
    admin_username: str
    admin_password: str
    contact_email: str
    workspaces_enabled: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

class InstitutionCreate(BaseModel):
    name: str
    institution_id: str
    admin_username: str
    admin_password: str
    contact_email: str
    workspaces_enabled: List[str]

class LoginSchema(BaseModel):
    username: str
    password: str
    institution_id: Optional[str] = None
