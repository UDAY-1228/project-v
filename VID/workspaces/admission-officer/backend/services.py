"""
Admission Officer - Services Layer
====================================
Business logic for all Admission Officer modules.
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
        stats = {
            "total_applications": await get_collection("applications").count_documents({}),
            "pending_applications": await get_collection("applications").count_documents({"status": "pending"}),
            "approved_applications": await get_collection("applications").count_documents({"status": "approved"}),
            "rejected_applications": await get_collection("applications").count_documents({"status": "rejected"}),
            "total_admissions": await get_collection("admissions").count_documents({}),
            "verified_documents": await get_collection("documents").count_documents({"status": "approved"}),
        }
        return stats

    @staticmethod
    async def get_recent_activity(limit: int = 10) -> List[Dict]:
        col = get_collection("activity_log")
        cursor = col.find().sort("timestamp", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))


class ApplicationService:

    @staticmethod
    async def create_application(data: dict) -> str:
        col = get_collection("applications")
        data["application_number"] = f"APP-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        data["submitted_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_applications(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("applications")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("submitted_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_application(app_id: str) -> Optional[Dict]:
        col = get_collection("applications")
        doc = await col.find_one({"_id": ObjectId(app_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_application(app_id: str, data: dict) -> bool:
        col = get_collection("applications")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(app_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_application(app_id: str) -> bool:
        col = get_collection("applications")
        result = await col.delete_one({"_id": ObjectId(app_id)})
        return result.deleted_count > 0


class StudentAdmissionService:

    @staticmethod
    async def create_admission(data: dict) -> str:
        col = get_collection("admissions")
        data["admission_number"] = f"ADM-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        data["admission_date"] = datetime.utcnow()
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_admissions(course: Optional[str] = None, batch: Optional[str] = None) -> List[Dict]:
        col = get_collection("admissions")
        query = {}
        if course:
            query["course"] = course
        if batch:
            query["batch"] = batch
        cursor = col.find(query).sort("admission_date", -1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_admission(admission_id: str) -> Optional[Dict]:
        col = get_collection("admissions")
        doc = await col.find_one({"_id": ObjectId(admission_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_admission(admission_id: str, data: dict) -> bool:
        col = get_collection("admissions")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(admission_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_admission(admission_id: str) -> bool:
        col = get_collection("admissions")
        result = await col.delete_one({"_id": ObjectId(admission_id)})
        return result.deleted_count > 0


class DocumentVerificationService:

    @staticmethod
    async def create_verification(data: dict) -> str:
        col = get_collection("documents")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_verifications(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("documents")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_verification(ver_id: str) -> Optional[Dict]:
        col = get_collection("documents")
        doc = await col.find_one({"_id": ObjectId(ver_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_verification(ver_id: str, data: dict) -> bool:
        col = get_collection("documents")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(ver_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def approve_document(ver_id: str, verified_by: str) -> bool:
        col = get_collection("documents")
        result = await col.update_one(
            {"_id": ObjectId(ver_id)},
            {"$set": {"status": "approved", "verified_by": verified_by, "verified_at": datetime.utcnow(), "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0


class FeeDetailsService:

    @staticmethod
    async def create_fee_details(data: dict) -> str:
        col = get_collection("fees")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_fee_details(student_id: Optional[str] = None, payment_status: Optional[str] = None) -> List[Dict]:
        col = get_collection("fees")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if payment_status:
            query["payment_status"] = payment_status
        cursor = col.find(query).sort("due_date", 1)
        return _serialize_list(await cursor.to_list(length=500))

    @staticmethod
    async def get_fee_details(fee_id: str) -> Optional[Dict]:
        col = get_collection("fees")
        doc = await col.find_one({"_id": ObjectId(fee_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_fee_details(fee_id: str, data: dict) -> bool:
        col = get_collection("fees")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(fee_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def record_payment(fee_id: str, amount: float, payment_method: str) -> bool:
        col = get_collection("fees")
        doc = await col.find_one({"_id": ObjectId(fee_id)})
        if doc:
            new_paid = doc.get("paid_amount", 0) + amount
            new_pending = doc.get("total_amount", 0) - new_paid
            status = "completed" if new_pending <= 0 else "partial"
            await col.update_one(
                {"_id": ObjectId(fee_id)},
                {"$set": {"paid_amount": new_paid, "pending_amount": max(0, new_pending), "payment_status": status, "updated_at": datetime.utcnow()},
                 "$push": {"payment_history": {"amount": amount, "method": payment_method, "date": datetime.utcnow()}}}
            )
            return True
        return False


class ReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("reports")
        data["generated_at"] = datetime.utcnow()
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


class SettingsService:

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
