"""
Voice Agent - Controllers
==========================
HTTP request handlers for the Voice Agent API.
Delegates to service layer for business logic.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from .models import *
from .services import (
    DashboardService,
    VoiceCommandService,
    ConversationService,
    LogService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/voice-agent", tags=["Voice Agent"])


class DashboardController:
    """Handle dashboard-related HTTP requests."""

    @staticmethod
    async def get_stats():
        """Get aggregate statistics for the Voice Agent dashboard."""
        try:
            stats = await DashboardService.get_stats()
            return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_activity(limit: int = Query(10, ge=1, le=50)):
        """Get recent activity log entries."""
        try:
            activities = await DashboardService.get_recent_activity(limit)
            return APIResponse(success=True, data=activities, count=len(activities))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


class VoiceCommandController:
    """Handle voice command-related HTTP requests."""

    @staticmethod
    async def create_command(data: VoiceCommandCreate):
        """Create a new voice command."""
        try:
            command_id = await VoiceCommandService.create_command(data.model_dump())
            return APIResponse(success=True, data={"id": command_id}, message="Voice command created")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_commands(enabled: Optional[bool] = None):
        """List all voice commands."""
        try:
            commands = await VoiceCommandService.get_all_commands(enabled)
            return APIResponse(success=True, data=commands, count=len(commands))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


class ConversationController:
    """Handle conversation-related HTTP requests."""

    @staticmethod
    async def create_conversation(data: ConversationCreate):
        """Start a new AI conversation session."""
        try:
            conv_id = await ConversationService.create_conversation(data.model_dump())
            return APIResponse(success=True, data={"id": conv_id}, message="Conversation started")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_conversations(user_id: Optional[str] = None, status: Optional[str] = None):
        """List all conversations."""
        try:
            conversations = await ConversationService.get_all_conversations(user_id, status)
            return APIResponse(success=True, data=conversations, count=len(conversations))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


class LogController:
    """Handle log-related HTTP requests."""

    @staticmethod
    async def create_log(data: LogEntryCreate):
        """Create a new log entry."""
        try:
            log_id = await LogService.create_log(data.model_dump())
            return APIResponse(success=True, data={"id": log_id}, message="Log created")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_logs(limit: int = Query(100, ge=1, le=500)):
        """Get log entries."""
        try:
            logs = await LogService.get_logs(limit=limit)
            return APIResponse(success=True, data=logs, count=len(logs))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


class ReportController:
    """Handle report-related HTTP requests."""

    @staticmethod
    async def create_report(data: ReportCreate):
        """Create a new report."""
        try:
            report_id = await ReportService.create_report(data.model_dump())
            return APIResponse(success=True, data={"id": report_id}, message="Report created")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_reports(report_type: Optional[str] = None):
        """List all reports."""
        try:
            reports = await ReportService.get_all_reports(report_type)
            return APIResponse(success=True, data=reports, count=len(reports))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


class SettingsController:
    """Handle settings-related HTTP requests."""

    @staticmethod
    async def get_settings(institution_id: Optional[str] = None):
        """Get voice agent settings."""
        try:
            settings = await SettingsService.get_settings(institution_id)
            return APIResponse(success=True, data=settings)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def update_settings(data: VoiceAgentSettingsCreate, institution_id: Optional[str] = None):
        """Update voice agent settings."""
        try:
            settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
            return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
