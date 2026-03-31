"""
Transport Coordinator - Services Layer
======================================
Business logic for all Transport Coordinator modules.
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
    async def get_stats() -> Dict[str, int]:
        return {
            "total_vehicles": await get_collection("vehicles").count_documents({}),
            "active_vehicles": await get_collection("vehicles").count_documents({"status": "active"}),
            "total_routes": await get_collection("routes").count_documents({}),
            "total_students_transported": await get_collection("student_transports").count_documents({"is_active": True}),
            "pending_maintenance": await get_collection("vehicles").count_documents({"status": "maintenance"}),
            "active_trips": await get_collection("trip_logs").count_documents({"status": "on_route"}),
        }

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class VehicleService:
    @staticmethod
    async def create_vehicle(data: dict) -> str:
        col = get_collection("vehicles")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_vehicles(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("vehicles")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("vehicle_number", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_vehicle(vehicle_id: str) -> Optional[Dict]:
        col = get_collection("vehicles")
        doc = await col.find_one({"_id": ObjectId(vehicle_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_vehicle(vehicle_id: str, data: dict) -> bool:
        col = get_collection("vehicles")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(vehicle_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_vehicle(vehicle_id: str) -> bool:
        col = get_collection("vehicles")
        result = await col.delete_one({"_id": ObjectId(vehicle_id)})
        return result.deleted_count > 0


class RouteService:
    @staticmethod
    async def create_route(data: dict) -> str:
        col = get_collection("routes")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_routes(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("routes")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("route_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_route(route_id: str) -> Optional[Dict]:
        col = get_collection("routes")
        doc = await col.find_one({"_id": ObjectId(route_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_route(route_id: str, data: dict) -> bool:
        col = get_collection("routes")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(route_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_route(route_id: str) -> bool:
        col = get_collection("routes")
        result = await col.delete_one({"_id": ObjectId(route_id)})
        return result.deleted_count > 0


class StudentTransportService:
    @staticmethod
    async def create_student_transport(data: dict) -> str:
        col = get_collection("student_transports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_student_transports(route_id: Optional[str] = None, is_active: Optional[bool] = None) -> List[Dict]:
        col = get_collection("student_transports")
        query = {}
        if route_id:
            query["route_id"] = route_id
        if is_active is not None:
            query["is_active"] = is_active
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_student_transport(transport_id: str) -> Optional[Dict]:
        col = get_collection("student_transports")
        doc = await col.find_one({"_id": ObjectId(transport_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_student_transport(transport_id: str, data: dict) -> bool:
        col = get_collection("student_transports")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(transport_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_student_transport(transport_id: str) -> bool:
        col = get_collection("student_transports")
        result = await col.delete_one({"_id": ObjectId(transport_id)})
        return result.deleted_count > 0


class TripLogService:
    @staticmethod
    async def create_trip_log(data: dict) -> str:
        col = get_collection("trip_logs")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_trip_logs(vehicle_id: Optional[str] = None, route_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("trip_logs")
        query = {}
        if vehicle_id:
            query["vehicle_id"] = vehicle_id
        if route_id:
            query["route_id"] = route_id
        cursor = col.find(query).sort("trip_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def update_trip_log(trip_id: str, data: dict) -> bool:
        col = get_collection("trip_logs")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(trip_id)}, {"$set": data})
        return result.modified_count > 0


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
    async def delete_report(report_id: str) -> bool:
        col = get_collection("reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
        return result.deleted_count > 0


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
