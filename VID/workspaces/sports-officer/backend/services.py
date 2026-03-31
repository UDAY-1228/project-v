"""
Sports Officer - Services Layer
===============================
Business logic for all Sports Officer modules.
"""

from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional
from .mongodb_connection import get_collection


def _serialize(doc: dict) -> dict:
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc


def _serialize_list(docs: list) -> list:
    return [_serialize(d) for d in docs]


class DashboardService:
    @staticmethod
    async def get_stats() -> Dict[str, Any]:
        stats = {
            "total_events": await get_collection("sports_events").count_documents({}),
            "upcoming_events": await get_collection("sports_events").count_documents({"status": "upcoming"}),
            "total_teams": await get_collection("teams").count_documents({}),
            "total_players": await get_collection("player_records").count_documents({}),
            "completed_matches": await get_collection("match_results").count_documents({"status": "completed"}),
            "active_tournaments": await get_collection("sports_events").count_documents({"event_type": "tournament", "status": "active"}),
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
            "action": action, "actor": actor, "module": module,
            "description": description, "timestamp": datetime.utcnow(),
        })


class SportsEventService:
    @staticmethod
    async def create_event(data: dict) -> str:
        col = get_collection("sports_events")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_events(status: Optional[str] = None, sport_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("sports_events")
        query = {}
        if status:
            query["status"] = status
        if sport_type:
            query["sport_category"] = sport_type
        cursor = col.find(query).sort("start_date", 1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_event(event_id: str) -> Optional[Dict]:
        col = get_collection("sports_events")
        doc = await col.find_one({"_id": ObjectId(event_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_event(event_id: str, data: dict) -> bool:
        col = get_collection("sports_events")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(event_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_event(event_id: str) -> bool:
        col = get_collection("sports_events")
        result = await col.delete_one({"_id": ObjectId(event_id)})
        return result.deleted_count > 0

    @staticmethod
    async def register_participant(event_id: str, team_id: str) -> bool:
        col = get_collection("sports_events")
        result = await col.update_one({"_id": ObjectId(event_id)}, {"$inc": {"registered_count": 1}})
        return result.modified_count > 0


class TeamService:
    @staticmethod
    async def create_team(data: dict) -> str:
        col = get_collection("teams")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_teams(sport_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("teams")
        query = {"sport_type": sport_type} if sport_type else {}
        cursor = col.find(query).sort("team_name", 1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_team(team_id: str) -> Optional[Dict]:
        col = get_collection("teams")
        doc = await col.find_one({"_id": ObjectId(team_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_team(team_id: str, data: dict) -> bool:
        col = get_collection("teams")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(team_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_team(team_id: str) -> bool:
        col = get_collection("teams")
        result = await col.delete_one({"_id": ObjectId(team_id)})
        return result.deleted_count > 0

    @staticmethod
    async def update_stats(team_id: str, win: bool = False, loss: bool = False, draw: bool = False) -> bool:
        col = get_collection("teams")
        update = {}
        if win: update["wins"] = 1
        elif loss: update["losses"] = 1
        elif draw: update["draws"] = 1
        if update:
            result = await col.update_one({"_id": ObjectId(team_id)}, {"$inc": update})
            return result.modified_count > 0
        return False


class PlayerRecordService:
    @staticmethod
    async def create_player(data: dict) -> str:
        col = get_collection("player_records")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_players(team_id: Optional[str] = None, sport_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("player_records")
        query = {}
        if team_id: query["team_id"] = team_id
        if sport_type: query["sport_type"] = sport_type
        cursor = col.find(query).sort("player_name", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_player(player_id: str) -> Optional[Dict]:
        col = get_collection("player_records")
        doc = await col.find_one({"_id": ObjectId(player_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_player(player_id: str, data: dict) -> bool:
        col = get_collection("player_records")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(player_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_player(player_id: str) -> bool:
        col = get_collection("player_records")
        result = await col.delete_one({"_id": ObjectId(player_id)})
        return result.deleted_count > 0

    @staticmethod
    async def update_stats(player_id: str, goals: int = 0, assists: int = 0, yellow: int = 0, red: int = 0) -> bool:
        col = get_collection("player_records")
        update = {"matches_played": 1}
        if goals: update["total_goals"] = goals
        if assists: update["total_assists"] = assists
        if yellow: update["yellow_cards"] = yellow
        if red: update["red_cards"] = red
        result = await col.update_one({"_id": ObjectId(player_id)}, {"$inc": update})
        return result.modified_count > 0


class ReportService:
    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["created_at"] = datetime.utcnow()
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
    async def delete_report(report_id: str) -> bool:
        col = get_collection("reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
        return result.deleted_count > 0


class SportsSettingsService:
    @staticmethod
    async def get_settings() -> Optional[Dict]:
        col = get_collection("settings")
        doc = await col.find_one({})
        return _serialize(doc) if doc else None

    @staticmethod
    async def upsert_settings(data: dict) -> str:
        col = get_collection("settings")
        data["updated_at"] = datetime.utcnow()
        existing = await col.find_one({})
        if existing:
            await col.update_one({"_id": existing["_id"]}, {"$set": data})
            return str(existing["_id"])
        else:
            data["created_at"] = datetime.utcnow()
            result = await col.insert_one(data)
            return str(result.inserted_id)
