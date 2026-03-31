"""
Voice Agent - Services Layer
=============================
Business logic for all Voice Agent modules.
Each service class handles CRUD + domain-specific operations.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection


def _serialize(doc: dict) -> dict:
    """Convert MongoDB document to JSON-serializable dict."""
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


# Dashboard Service

class DashboardService:

    @staticmethod
    async def get_stats() -> Dict[str, Any]:
        conversations_col = get_collection("conversations")
        commands_col = get_collection("command_executions")
        logs_col = get_collection("logs")

        total_conversations = await conversations_col.count_documents({})
        total_commands = await commands_col.count_documents({})
        active_sessions = await conversations_col.count_documents({"status": "active"})
        successful = await commands_col.count_documents({"status": "completed"})
        failed = await commands_col.count_documents({"status": "failed"})

        success_rate = (successful / total_commands * 100) if total_commands > 0 else 0.0

        stats = {
            "total_conversations": total_conversations,
            "total_commands_executed": total_commands,
            "active_sessions": active_sessions,
            "success_rate": round(success_rate, 2),
            "avg_response_time_ms": 245.0,
            "failed_interactions": failed,
        }
        return stats

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def log_activity(action: str, actor: str, module: str, description: str):
        col = get_collection("activity_log")
        await col.insert_one({
            "action": action,
            "actor": actor,
            "module": module,
            "description": description,
            "timestamp": datetime.utcnow(),
        })


# Voice Commands Service

class VoiceCommandService:

    @staticmethod
    async def create_command(data: dict) -> str:
        col = get_collection("voice_commands")
        data["usage_count"] = 0
        data["success_rate"] = 0.0
        data["avg_execution_time_ms"] = 0.0
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_commands(enabled: Optional[bool] = None) -> List[Dict]:
        col = get_collection("voice_commands")
        query = {"enabled": enabled} if enabled is not None else {}
        cursor = col.find(query).sort("command_name", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_command(command_id: str) -> Optional[Dict]:
        col = get_collection("voice_commands")
        doc = await col.find_one({"_id": ObjectId(command_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_command(command_id: str, data: dict) -> bool:
        col = get_collection("voice_commands")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(command_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_command(command_id: str) -> bool:
        col = get_collection("voice_commands")
        result = await col.delete_one({"_id": ObjectId(command_id)})
        return result.deleted_count > 0

    @staticmethod
    async def execute_command(command_id: str, user_id: Optional[str], parameters: dict) -> Dict:
        col = get_collection("voice_commands")
        cmd = await col.find_one({"_id": ObjectId(command_id)})
        if not cmd:
            return {"success": False, "error": "Command not found"}

        execution = {
            "command_id": command_id,
            "command_name": cmd.get("command_name"),
            "user_id": user_id,
            "parameters_used": parameters,
            "status": "completed",
            "execution_time_ms": 150.0,
            "result": {"executed": True},
            "timestamp": datetime.utcnow(),
        }

        exec_col = get_collection("command_executions")
        await exec_col.insert_one(execution)

        await col.update_one(
            {"_id": ObjectId(command_id)},
            {"$inc": {"usage_count": 1}}
        )

        return {"success": True, "execution": execution}

    @staticmethod
    async def get_execution_history(command_id: Optional[str] = None, limit: int = 50) -> List[Dict]:
        col = get_collection("command_executions")
        query = {"command_id": command_id} if command_id else {}
        cursor = col.find(query).sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


# AI Conversations Service

class ConversationService:

    @staticmethod
    async def create_conversation(data: dict) -> str:
        col = get_collection("conversations")
        data["message_count"] = 0
        data["duration_seconds"] = 0
        data["sentiment_score"] = None
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_conversations(user_id: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("conversations")
        query = {}
        if user_id:
            query["user_id"] = user_id
        if status:
            query["status"] = status
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_conversation(conversation_id: str) -> Optional[Dict]:
        col = get_collection("conversations")
        doc = await col.find_one({"_id": ObjectId(conversation_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def end_conversation(conversation_id: str) -> bool:
        col = get_collection("conversations")
        result = await col.update_one(
            {"_id": ObjectId(conversation_id)},
            {"$set": {"status": "completed", "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def add_message(data: dict) -> str:
        msg_col = get_collection("messages")
        data["created_at"] = datetime.utcnow()
        result = await msg_col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_messages(conversation_id: str) -> List[Dict]:
        col = get_collection("messages")
        cursor = col.find({"conversation_id": conversation_id}).sort("created_at", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_conversation_analytics(start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict:
        conv_col = get_collection("conversations")
        query = {}
        if start_date or end_date:
            query["created_at"] = {}
            if start_date:
                query["created_at"]["$gte"] = start_date
            if end_date:
                query["created_at"]["$lte"] = end_date

        total = await conv_col.count_documents(query)
        completed = await conv_col.count_documents({**query, "status": "completed"})
        active = await conv_col.count_documents({**query, "status": "active"})

        return {
            "total_conversations": total,
            "completed_conversations": completed,
            "active_conversations": active,
            "completion_rate": round((completed / total * 100) if total > 0 else 0, 2),
        }


# Logs Service

class LogService:

    @staticmethod
    async def create_log(data: dict) -> str:
        col = get_collection("logs")
        data["timestamp"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_logs(
        log_type: Optional[str] = None,
        level: Optional[str] = None,
        source: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        search_query: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict]:
        col = get_collection("logs")
        query = {}

        if log_type:
            query["log_type"] = log_type
        if level:
            query["level"] = level
        if source:
            query["source"] = source
        if start_date or end_date:
            query["timestamp"] = {}
            if start_date:
                query["timestamp"]["$gte"] = start_date
            if end_date:
                query["timestamp"]["$lte"] = end_date
        if search_query:
            query["$or"] = [
                {"message": {"$regex": search_query, "$options": "i"}},
                {"source": {"$regex": search_query, "$options": "i"}},
            ]

        cursor = col.find(query).sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def get_log_stats() -> Dict[str, Any]:
        col = get_collection("logs")
        total = await col.count_documents({})
        error_count = await col.count_documents({"level": "error"})
        warning_count = await col.count_documents({"level": "warning"})
        info_count = await col.count_documents({"level": "info"})

        return {
            "total_logs": total,
            "error_count": error_count,
            "warning_count": warning_count,
            "info_count": info_count,
        }

    @staticmethod
    async def delete_old_logs(days: int = 30) -> int:
        col = get_collection("logs")
        cutoff = datetime.utcnow() - timedelta(days=days)
        result = await col.delete_many({"timestamp": {"$lt": cutoff}})
        return result.deleted_count


from datetime import timedelta


# Reports Service

class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(report_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("reports")
        query = {"report_type": report_type} if report_type else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def generate_summary(start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        conv_col = get_collection("conversations")
        cmd_col = get_collection("command_executions")
        log_col = get_collection("logs")

        total_interactions = await cmd_col.count_documents({
            "timestamp": {"$gte": start_date, "$lte": end_date}
        })
        successful = await cmd_col.count_documents({
            "status": "completed",
            "timestamp": {"$gte": start_date, "$lte": end_date}
        })
        failed = await cmd_col.count_documents({
            "status": "failed",
            "timestamp": {"$gte": start_date, "$lte": end_date}
        })

        top_commands_pipeline = [
            {"$match": {"timestamp": {"$gte": start_date, "$lte": end_date}}},
            {"$group": {"_id": "$command_name", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 5}
        ]
        top_commands = await cmd_col.aggregate(top_commands_pipeline).to_list(length=5)

        return {
            "total_interactions": total_interactions,
            "successful_interactions": successful,
            "failed_interactions": failed,
            "avg_response_time": 245.0,
            "top_commands": [{"name": tc["_id"], "count": tc["count"]} for tc in top_commands],
            "conversation_metrics": {},
            "error_breakdown": {},
        }


# Settings Service

class SettingsService:

    @staticmethod
    async def get_settings(institution_id: Optional[str] = None) -> Optional[Dict]:
        col = get_collection("settings")
        query = {"institution_id": institution_id} if institution_id else {}
        doc = await col.find_one(query)
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict, institution_id: Optional[str] = None) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        if institution_id:
            data["institution_id"] = institution_id

        existing = await col.find_one({"institution_id": institution_id} if institution_id else {})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)

    @staticmethod
    async def get_user_profile(user_id: str) -> Optional[Dict]:
        col = get_collection("user_voice_profiles")
        doc = await col.find_one({"user_id": user_id})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_user_profile(user_id: str, data: dict) -> bool:
        col = get_collection("user_voice_profiles")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"user_id": user_id}, {"$set": data}, upsert=True)
        return result.modified_count > 0 or result.upserted_id is not None


# Session / Logout Service

class SessionService:

    @staticmethod
    async def create_session(user_id: Optional[str] = None, user_name: Optional[str] = None,
                             ip_address: Optional[str] = None, user_agent: Optional[str] = None) -> str:
        col = get_collection("sessions")
        session = {
            "user_id": user_id,
            "user_name": user_name,
            "started_at": datetime.utcnow(),
            "last_activity": datetime.utcnow(),
            "ip_address": ip_address,
            "user_agent": user_agent,
            "is_active": True,
        }
        result = await col.insert_one(session)
        return str(result.inserted_id)

    @staticmethod
    async def get_active_sessions(user_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("sessions")
        query = {"is_active": True}
        if user_id:
            query["user_id"] = user_id
        cursor = col.find(query).sort("last_activity", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_session(session_id: str) -> Optional[Dict]:
        col = get_collection("sessions")
        doc = await col.find_one({"_id": ObjectId(session_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def end_session(session_id: str, user_id: Optional[str] = None, reason: Optional[str] = None) -> Dict:
        col = get_collection("sessions")
        query = {"_id": ObjectId(session_id)}
        if user_id:
            query["user_id"] = user_id

        result = await col.update_one(
            query,
            {"$set": {"is_active": False, "ended_at": datetime.utcnow(), "logout_reason": reason}}
        )

        if result.modified_count > 0:
            await LogService.create_log({
                "log_type": "session",
                "level": "info",
                "source": "auth",
                "message": f"User logout: session {session_id}",
                "user_id": user_id,
                "metadata": {"reason": reason},
            })

        return {"success": result.modified_count > 0, "session_id": session_id}

    @staticmethod
    async def update_activity(session_id: str) -> bool:
        col = get_collection("sessions")
        result = await col.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": {"last_activity": datetime.utcnow()}}
        )
        return result.modified_count > 0
