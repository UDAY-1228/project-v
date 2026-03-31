"""
Team Owner - Service Methods
=============================
Service layer for the Team Owner workspace.
"""

from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .mongodb_connection import get_collection


def serialize_doc(doc: dict) -> dict:
    if doc is None:
        return None
    doc["_id"] = str(doc["_id"])
    if "created_at" in doc:
        doc["created_at"] = doc["created_at"].isoformat()
    if "updated_at" in doc:
        doc["updated_at"] = doc["updated_at"].isoformat()
    if "joined_at" in doc:
        doc["joined_at"] = doc["joined_at"].isoformat()
    return doc


class WorkspaceService:
    collection = "workspaces"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        data["is_active"] = True
        result = await get_collection(WorkspaceService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(WorkspaceService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(workspace_id: str) -> Optional[dict]:
        doc = await get_collection(WorkspaceService.collection).find_one({"_id": ObjectId(workspace_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def get_by_owner(owner_id: str) -> List[dict]:
        cursor = get_collection(WorkspaceService.collection).find({"owner_id": owner_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(workspace_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(WorkspaceService.collection).find_one_and_update(
            {"_id": ObjectId(workspace_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(workspace_id: str) -> bool:
        result = await get_collection(WorkspaceService.collection).delete_one({"_id": ObjectId(workspace_id)})
        return result.deleted_count > 0


class MemberService:
    collection = "members"

    @staticmethod
    async def create(data: dict) -> dict:
        data["joined_at"] = datetime.utcnow()
        result = await get_collection(MemberService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(MemberService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(member_id: str) -> Optional[dict]:
        doc = await get_collection(MemberService.collection).find_one({"_id": ObjectId(member_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def get_by_workspace(workspace_id: str) -> List[dict]:
        cursor = get_collection(MemberService.collection).find({"workspace_id": workspace_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_user(user_id: str) -> List[dict]:
        cursor = get_collection(MemberService.collection).find({"user_id": user_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(member_id: str, data: dict) -> Optional[dict]:
        result = await get_collection(MemberService.collection).find_one_and_update(
            {"_id": ObjectId(member_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(member_id: str) -> bool:
        result = await get_collection(MemberService.collection).delete_one({"_id": ObjectId(member_id)})
        return result.deleted_count > 0


class AccessControlService:
    collection = "access_controls"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(AccessControlService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(AccessControlService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_id(control_id: str) -> Optional[dict]:
        doc = await get_collection(AccessControlService.collection).find_one({"_id": ObjectId(control_id)})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def get_by_workspace(workspace_id: str) -> List[dict]:
        cursor = get_collection(AccessControlService.collection).find({"workspace_id": workspace_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_user(user_id: str) -> List[dict]:
        cursor = get_collection(AccessControlService.collection).find({"user_id": user_id})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def update(control_id: str, data: dict) -> Optional[dict]:
        data["updated_at"] = datetime.utcnow()
        result = await get_collection(AccessControlService.collection).find_one_and_update(
            {"_id": ObjectId(control_id)},
            {"$set": data},
            return_document=True
        )
        return serialize_doc(result) if result else None

    @staticmethod
    async def delete(control_id: str) -> bool:
        result = await get_collection(AccessControlService.collection).delete_one({"_id": ObjectId(control_id)})
        return result.deleted_count > 0


class ReportService:
    collection = "reports"

    @staticmethod
    async def create(data: dict) -> dict:
        data["created_at"] = datetime.utcnow()
        result = await get_collection(ReportService.collection).insert_one(data)
        data["_id"] = str(result.inserted_id)
        return serialize_doc(data)

    @staticmethod
    async def get_all() -> List[dict]:
        cursor = get_collection(ReportService.collection).find()
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]

    @staticmethod
    async def get_by_type(report_type: str) -> List[dict]:
        cursor = get_collection(ReportService.collection).find({"report_type": report_type})
        docs = await cursor.to_list(length=None)
        return [serialize_doc(d) for d in docs]


class DashboardService:
    @staticmethod
    async def get_stats() -> dict:
        total_workspaces = await get_collection(WorkspaceService.collection).count_documents({})
        active_workspaces = await get_collection(WorkspaceService.collection).count_documents({"is_active": True})
        total_members = await get_collection(MemberService.collection).count_documents({})
        total_access_controls = await get_collection(AccessControlService.collection).count_documents({})

        return {
            "total_workspaces": total_workspaces,
            "active_workspaces": active_workspaces,
            "total_members": total_members,
            "total_access_controls": total_access_controls
        }


class SettingsService:
    collection = "settings"

    @staticmethod
    async def get() -> Optional[dict]:
        doc = await get_collection(SettingsService.collection).find_one({"type": "team_owner"})
        return serialize_doc(doc) if doc else None

    @staticmethod
    async def update(data: dict) -> dict:
        result = await get_collection(SettingsService.collection).find_one_and_update(
            {"type": "team_owner"},
            {"$set": {**data, "updated_at": datetime.utcnow()}},
            upsert=True,
            return_document=True
        )
        return serialize_doc(result)
