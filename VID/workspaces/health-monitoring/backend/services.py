"""
Health Monitoring - Services Layer
====================================
Business logic for all Health Monitoring modules.
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
            "total_patients": await get_collection("health_records").count_documents({}),
            "total_records": await get_collection("medical_reports").count_documents({}),
            "pending_alerts": await get_collection("alerts").count_documents({"status": "pending"}),
            "critical_alerts": await get_collection("alerts").count_documents({"severity": "critical"}),
            "reports_generated": await get_collection("reports").count_documents({}),
            "active_campaigns": 0,
        }

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class HealthRecordService:
    @staticmethod
    async def create_record(data: dict) -> str:
        col = get_collection("health_records")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_records(student_id: Optional[str] = None) -> List[Dict]:
        col = get_collection("health_records")
        query = {"student_id": student_id} if student_id else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_record(record_id: str) -> Optional[Dict]:
        col = get_collection("health_records")
        doc = await col.find_one({"_id": ObjectId(record_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_record(record_id: str, data: dict) -> bool:
        col = get_collection("health_records")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(record_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_record(record_id: str) -> bool:
        col = get_collection("health_records")
        result = await col.delete_one({"_id": ObjectId(record_id)})
        return result.deleted_count > 0


class MedicalReportService:
    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("medical_reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(student_id: Optional[str] = None, report_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("medical_reports")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if report_type:
            query["report_type"] = report_type
        cursor = col.find(query).sort("examination_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("medical_reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_report(report_id: str, data: dict) -> bool:
        col = get_collection("medical_reports")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(report_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("medical_reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
        return result.deleted_count > 0


class AlertService:
    @staticmethod
    async def create_alert(data: dict) -> str:
        col = get_collection("alerts")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_alerts(severity: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        col = get_collection("alerts")
        query = {}
        if severity:
            query["severity"] = severity
        if status:
            query["status"] = status
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_alert(alert_id: str) -> Optional[Dict]:
        col = get_collection("alerts")
        doc = await col.find_one({"_id": ObjectId(alert_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_alert(alert_id: str, data: dict) -> bool:
        col = get_collection("alerts")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(alert_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def resolve_alert(alert_id: str, resolved_by: str) -> bool:
        col = get_collection("alerts")
        result = await col.update_one(
            {"_id": ObjectId(alert_id)},
            {"$set": {"status": "resolved", "resolved_at": datetime.utcnow(), "resolved_by": resolved_by, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete_alert(alert_id: str) -> bool:
        col = get_collection("alerts")
        result = await col.delete_one({"_id": ObjectId(alert_id)})
        return result.deleted_count > 0


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
