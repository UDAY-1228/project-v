"""
Voice Agent - Pydantic Models
==============================
Data models for all Voice Agent pages:
Dashboard, Voice Commands, AI Conversations, Logs, Reports, Settings
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
    failed = "failed"
    processing = "processing"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class PaginationParams(BaseModel):
    page: int = 1
    limit: int = 20
    sort_by: str = "created_at"
    sort_order: str = "desc"


# Dashboard

class DashboardStats(BaseModel):
    total_conversations: int = 0
    total_commands_executed: int = 0
    active_sessions: int = 0
    success_rate: float = 0.0
    avg_response_time_ms: float = 0.0
    failed_interactions: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Voice Commands

class VoiceCommandBase(BaseModel):
    command_name: str
    command_phrase: str
    description: Optional[str] = None
    intent: str
    parameters: List[Dict[str, Any]] = []
    module_target: str
    access_level: str = "user"
    enabled: bool = True
    status: StatusEnum = StatusEnum.active


class VoiceCommandCreate(VoiceCommandBase):
    pass


class VoiceCommand(VoiceCommandBase):
    id: str
    usage_count: int = 0
    success_rate: float = 0.0
    avg_execution_time_ms: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CommandExecution(BaseModel):
    id: Optional[str] = None
    command_id: str
    command_name: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    parameters_used: Dict[str, Any] = {}
    status: StatusEnum = StatusEnum.completed
    execution_time_ms: float = 0.0
    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# AI Conversations

class ConversationBase(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    conversation_type: str = "voice"
    language: str = "en"
    context: Dict[str, Any] = {}
    status: StatusEnum = StatusEnum.active


class ConversationCreate(ConversationBase):
    pass


class Conversation(ConversationBase):
    id: str
    message_count: int = 0
    duration_seconds: int = 0
    sentiment_score: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MessageBase(BaseModel):
    conversation_id: str
    role: str = "user"
    content: str
    message_type: str = "text"
    audio_url: Optional[str] = None
    intent_detected: Optional[str] = None
    entities_extracted: List[Dict[str, Any]] = []
    confidence_score: float = 1.0
    metadata: Dict[str, Any] = {}


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Logs

class LogEntryBase(BaseModel):
    log_type: str
    level: str = "info"
    source: str
    message: str
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    metadata: Dict[str, Any] = {}
    tags: List[str] = []


class LogEntryCreate(LogEntryBase):
    pass


class LogEntry(LogEntryBase):
    id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LogFilter(BaseModel):
    log_type: Optional[str] = None
    level: Optional[str] = None
    source: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    user_id: Optional[str] = None
    search_query: Optional[str] = None


# Reports

class ReportBase(BaseModel):
    report_name: str
    report_type: str
    date_range_start: datetime
    date_range_end: datetime
    generated_by: Optional[str] = None
    filters: Dict[str, Any] = {}
    status: StatusEnum = StatusEnum.pending


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: str
    file_url: Optional[str] = None
    summary: Optional[Dict[str, Any]] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReportSummary(BaseModel):
    total_interactions: int = 0
    successful_interactions: int = 0
    failed_interactions: int = 0
    avg_response_time: float = 0.0
    top_commands: List[Dict[str, Any]] = []
    conversation_metrics: Dict[str, Any] = {}
    error_breakdown: Dict[str, int] = {}


# Settings

class VoiceAgentSettingsBase(BaseModel):
    wake_word: str = "hey assistant"
    language: str = "en-US"
    voice_id: str = "default"
    speech_to_text_model: str = "base"
    text_to_speech_enabled: bool = True
    noise_cancellation: bool = True
    ambient_noise_adjustment: bool = True
    conversation_timeout_seconds: int = 300
    max_conversation_duration_minutes: int = 30
    ai_provider: str = "openai"
    ai_model: str = "gpt-4"
    context_retention_messages: int = 10
    sentiment_analysis_enabled: bool = True
    logging_level: str = "info"
    notification_preferences: Dict[str, bool] = {
        "email": False,
        "push": True,
        "sms": False,
    }


class VoiceAgentSettingsCreate(VoiceAgentSettingsBase):
    pass


class VoiceAgentSettings(VoiceAgentSettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserVoiceProfile(BaseModel):
    user_id: str
    user_name: Optional[str] = None
    voice_embedding: Optional[List[float]] = None
    preferred_language: str = "en"
    preferred_voice_id: str = "default"
    custom_commands: List[str] = []
    disabled_commands: List[str] = []
    sensitivity_level: str = "normal"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Logout / Session Management

class SessionInfo(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    started_at: datetime = Field(default_factory=datetime.utcnow)
    last_activity: datetime = Field(default_factory=datetime.utcnow)
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    is_active: bool = True


class LogoutRequest(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    reason: Optional[str] = None


class LogoutResponse(BaseModel):
    success: bool
    message: str
    session_ended_at: datetime = Field(default_factory=datetime.utcnow)
