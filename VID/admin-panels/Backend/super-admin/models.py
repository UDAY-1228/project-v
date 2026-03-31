from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Institution(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    code: str
    location: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    contact_email: str
    contact_phone: Optional[str] = None
    revenue_history: List[dict] = [] # Monthly revenue entries

class Statistic(BaseModel):
    total_institutions: int
    active_institutions: int
    inactive_institutions: int
    total_revenue: float
    monthly_revenue: float
    usage_overview: List[dict] = []
