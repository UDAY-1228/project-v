"""
Sports Officer - Pydantic Models
================================
Data models for all Sports Officer pages: Dashboard, Sports Events,
Teams, Player Records, Reports, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    completed = "completed"
    cancelled = "cancelled"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class DashboardStats(BaseModel):
    total_events: int = 0
    upcoming_events: int = 0
    total_teams: int = 0
    total_players: int = 0
    completed_matches: int = 0
    active_tournaments: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class SportsEventBase(BaseModel):
    event_name: str
    event_type: str
    sport_category: str
    start_date: datetime
    end_date: datetime
    venue: Optional[str] = None
    max_participants: int = 100
    registration_deadline: Optional[datetime] = None
    description: Optional[str] = None
    status: str = "upcoming"
    prize_money: Optional[float] = None


class SportsEventCreate(SportsEventBase):
    pass


class SportsEvent(SportsEventBase):
    id: str
    created_by: Optional[str] = None
    registered_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TeamBase(BaseModel):
    team_name: str
    sport_type: str
    team_code: str
    coach_id: Optional[str] = None
    coach_name: Optional[str] = None
    captain_id: Optional[str] = None
    max_members: int = 25
    founded_year: Optional[int] = None
    home_venue: Optional[str] = None
    status: str = "active"


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: str
    current_members: int = 0
    wins: int = 0
    losses: int = 0
    draws: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class PlayerRecordBase(BaseModel):
    player_name: str
    player_id: str
    team_id: Optional[str] = None
    team_name: Optional[str] = None
    sport_type: str
    position: Optional[str] = None
    jersey_number: Optional[int] = None
    date_of_birth: Optional[datetime] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    status: str = "active"


class PlayerRecordCreate(PlayerRecordBase):
    pass


class PlayerRecord(PlayerRecordBase):
    id: str
    matches_played: int = 0
    total_goals: int = 0
    total_assists: int = 0
    yellow_cards: int = 0
    red_cards: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MatchResult(BaseModel):
    match_id: str
    team1_id: str
    team1_name: str
    team2_id: str
    team2_name: str
    team1_score: int = 0
    team2_score: int = 0
    match_date: datetime
    venue: Optional[str] = None
    man_of_match: Optional[str] = None
    status: str = "completed"


class ReportBase(BaseModel):
    report_name: str
    report_type: str
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    sport_category: Optional[str] = None
    status: str = "pending"


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SportsSettingsBase(BaseModel):
    default_match_duration: int = 90
    overtime_enabled: bool = True
    tiebreaker_method: str = "penalty_shootout"
    max_team_size: int = 25
    min_team_size: int = 11
    notification_preferences: Dict[str, bool] = {
        "email": True,
        "sms": False,
        "push": True
    }


class SportsSettingsCreate(SportsSettingsBase):
    pass


class SportsSettings(SportsSettingsBase):
    id: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
