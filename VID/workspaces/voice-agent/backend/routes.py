"""
Voice Agent - API Routes
=========================
FastAPI router for all Voice Agent endpoints.
Covers: Dashboard, Voice Commands, AI Conversations, Logs, Reports, Settings
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from datetime import datetime
from .models import *
from .services import (
    DashboardService,
    VoiceCommandService,
    ConversationService,
    LogService,
    ReportService,
    SettingsService,
    SessionService,
)

router = APIRouter(prefix="/voice-agent", tags=["Voice Agent"])


# ════════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ════════════════════════════════════════════════════════════════════════════════

@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats():
    """Get aggregate statistics for the Voice Agent dashboard."""
    try:
        stats = await DashboardService.get_stats()
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(limit: int = Query(10, ge=1, le=50)):
    """Get recent activity log entries."""
    try:
        activities = await DashboardService.get_recent_activity(limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# VOICE COMMANDS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/commands", response_model=APIResponse)
async def create_command(data: VoiceCommandCreate):
    """Create a new voice command."""
    try:
        command_id = await VoiceCommandService.create_command(data.model_dump())
        return APIResponse(success=True, data={"id": command_id}, message="Voice command created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/commands", response_model=APIResponse)
async def get_commands(enabled: Optional[bool] = None):
    """List all voice commands."""
    try:
        commands = await VoiceCommandService.get_all_commands(enabled)
        return APIResponse(success=True, data=commands, count=len(commands))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/commands/{command_id}", response_model=APIResponse)
async def get_command(command_id: str):
    """Get a specific voice command by ID."""
    try:
        command = await VoiceCommandService.get_command(command_id)
        if not command:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=command)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/commands/{command_id}", response_model=APIResponse)
async def update_command(command_id: str, data: VoiceCommandCreate):
    """Update an existing voice command."""
    try:
        updated = await VoiceCommandService.update_command(command_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/commands/{command_id}", response_model=APIResponse)
async def delete_command(command_id: str):
    """Delete a voice command."""
    try:
        deleted = await VoiceCommandService.delete_command(command_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/commands/{command_id}/execute", response_model=APIResponse)
async def execute_command(command_id: str, user_id: Optional[str] = None, parameters: Optional[dict] = None):
    """Execute a voice command."""
    try:
        result = await VoiceCommandService.execute_command(command_id, user_id, parameters or {})
        return APIResponse(success=result.get("success", False), data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/commands/{command_id}/history", response_model=APIResponse)
async def get_command_history(command_id: str, limit: int = Query(50, ge=1, le=200)):
    """Get execution history for a voice command."""
    try:
        history = await VoiceCommandService.get_execution_history(command_id, limit)
        return APIResponse(success=True, data=history, count=len(history))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# AI CONVERSATIONS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/conversations", response_model=APIResponse)
async def create_conversation(data: ConversationCreate):
    """Start a new AI conversation session."""
    try:
        conv_id = await ConversationService.create_conversation(data.model_dump())
        return APIResponse(success=True, data={"id": conv_id}, message="Conversation started")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/conversations", response_model=APIResponse)
async def get_conversations(user_id: Optional[str] = None, status: Optional[str] = None):
    """List all conversations."""
    try:
        conversations = await ConversationService.get_all_conversations(user_id, status)
        return APIResponse(success=True, data=conversations, count=len(conversations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/conversations/{conversation_id}", response_model=APIResponse)
async def get_conversation(conversation_id: str):
    """Get a specific conversation by ID."""
    try:
        conversation = await ConversationService.get_conversation(conversation_id)
        if not conversation:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=conversation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/conversations/{conversation_id}/end", response_model=APIResponse)
async def end_conversation(conversation_id: str):
    """End an active conversation."""
    try:
        ended = await ConversationService.end_conversation(conversation_id)
        return APIResponse(success=ended, message="Conversation ended" if ended else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/conversations/{conversation_id}/messages", response_model=APIResponse)
async def add_message(conversation_id: str, data: MessageCreate):
    """Add a message to a conversation."""
    try:
        data_dict = data.model_dump()
        data_dict["conversation_id"] = conversation_id
        msg_id = await ConversationService.add_message(data_dict)
        return APIResponse(success=True, data={"id": msg_id}, message="Message added")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/conversations/{conversation_id}/messages", response_model=APIResponse)
async def get_messages(conversation_id: str):
    """Get all messages in a conversation."""
    try:
        messages = await ConversationService.get_messages(conversation_id)
        return APIResponse(success=True, data=messages, count=len(messages))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/conversations/analytics", response_model=APIResponse)
async def get_conversation_analytics(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    """Get conversation analytics."""
    try:
        analytics = await ConversationService.get_conversation_analytics(start_date, end_date)
        return APIResponse(success=True, data=analytics)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# LOGS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/logs", response_model=APIResponse)
async def create_log(data: LogEntryCreate):
    """Create a new log entry."""
    try:
        log_id = await LogService.create_log(data.model_dump())
        return APIResponse(success=True, data={"id": log_id}, message="Log created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/logs", response_model=APIResponse)
async def get_logs(
    log_type: Optional[str] = None,
    level: Optional[str] = None,
    source: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    search_query: Optional[str] = None,
    limit: int = Query(100, ge=1, le=500)
):
    """Get filtered log entries."""
    try:
        logs = await LogService.get_logs(
            log_type, level, source, start_date, end_date, search_query, limit
        )
        return APIResponse(success=True, data=logs, count=len(logs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/logs/stats", response_model=APIResponse)
async def get_log_stats():
    """Get log statistics."""
    try:
        stats = await LogService.get_log_stats()
        return APIResponse(success=True, data=stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/logs/cleanup", response_model=APIResponse)
async def cleanup_old_logs(days: int = Query(30, ge=1)):
    """Delete logs older than specified days."""
    try:
        deleted = await LogService.delete_old_logs(days)
        return APIResponse(success=True, message=f"Deleted {deleted} old logs")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# REPORTS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/reports", response_model=APIResponse)
async def create_report(data: ReportCreate):
    """Create a new report."""
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None):
    """List all reports."""
    try:
        reports = await ReportService.get_all_reports(report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    """Get a specific report by ID."""
    try:
        report = await ReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/generate", response_model=APIResponse)
async def generate_report_summary(
    start_date: datetime,
    end_date: datetime,
    report_type: str = Query(..., description="Type of report: usage, performance, errors")
):
    """Generate a summary report for the specified date range."""
    try:
        summary = await ReportService.generate_summary(start_date, end_date)
        return APIResponse(success=True, data=summary, message=f"{report_type} report generated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

@router.get("/settings", response_model=APIResponse)
async def get_settings(institution_id: Optional[str] = None):
    """Get voice agent settings."""
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: VoiceAgentSettingsCreate, institution_id: Optional[str] = None):
    """Update voice agent settings."""
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings/profile/{user_id}", response_model=APIResponse)
async def get_user_voice_profile(user_id: str):
    """Get user-specific voice profile."""
    try:
        profile = await SettingsService.get_user_profile(user_id)
        if not profile:
            return APIResponse(success=False, error="Profile not found")
        return APIResponse(success=True, data=profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings/profile/{user_id}", response_model=APIResponse)
async def update_user_voice_profile(user_id: str, data: dict):
    """Update user-specific voice profile."""
    try:
        updated = await SettingsService.update_user_profile(user_id, data)
        return APIResponse(success=updated, message="Profile updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# LOGOUT / SESSION
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/logout", response_model=APIResponse)
async def logout(request: LogoutRequest):
    """End a user session (logout)."""
    try:
        result = await SessionService.end_session(request.session_id, request.user_id, request.reason)
        return APIResponse(success=result.get("success", False), data=result, message="Logged out successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions", response_model=APIResponse)
async def get_active_sessions(user_id: Optional[str] = None):
    """Get active sessions."""
    try:
        sessions = await SessionService.get_active_sessions(user_id)
        return APIResponse(success=True, data=sessions, count=len(sessions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}", response_model=APIResponse)
async def get_session(session_id: str):
    """Get session details."""
    try:
        session = await SessionService.get_session(session_id)
        if not session:
            return APIResponse(success=False, error="Session not found")
        return APIResponse(success=True, data=session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
