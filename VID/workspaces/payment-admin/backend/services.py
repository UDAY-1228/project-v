"""
Payment Admin - Services Layer
===============================
Business logic for all Payment Admin modules.
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
            "total_revenue": 0.0,
            "total_transactions": await get_collection("transactions").count_documents({}),
            "pending_payments": await get_collection("student_fees").count_documents({"payment_status": "pending"}),
            "completed_payments": await get_collection("transactions").count_documents({"status": "completed"}),
            "failed_payments": await get_collection("transactions").count_documents({"status": "failed"}),
            "pending_invoices": await get_collection("invoices").count_documents({"status": "pending"}),
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


class TransactionService:

    @staticmethod
    async def create_transaction(data: dict) -> str:
        col = get_collection("transactions")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_transactions(
        status: Optional[str] = None,
        student_id: Optional[str] = None,
        payment_type: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict]:
        col = get_collection("transactions")
        query = {}
        if status:
            query["status"] = status
        if student_id:
            query["student_id"] = student_id
        if payment_type:
            query["payment_type"] = payment_type
        cursor = col.find(query).sort("transaction_date", -1).limit(limit)
        return _serialize_list(await cursor.to_list(length=limit))

    @staticmethod
    async def get_transaction(transaction_id: str) -> Optional[Dict]:
        col = get_collection("transactions")
        doc = await col.find_one({"_id": ObjectId(transaction_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_transaction(transaction_id: str, data: dict) -> bool:
        col = get_collection("transactions")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(transaction_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_transaction(transaction_id: str) -> bool:
        col = get_collection("transactions")
        result = await col.delete_one({"_id": ObjectId(transaction_id)})
        return result.deleted_count > 0

    @staticmethod
    async def search_transactions(query: str) -> List[Dict]:
        col = get_collection("transactions")
        search_query = {
            "$or": [
                {"student_name": {"$regex": query, "$options": "i"}},
                {"transaction_id": {"$regex": query, "$options": "i"}},
                {"reference_number": {"$regex": query, "$options": "i"}}
            ]
        }
        cursor = col.find(search_query).limit(50)
        return _serialize_list(await cursor.to_list(length=50))


class FeeCollectionService:

    @staticmethod
    async def create_fee_structure(data: dict) -> str:
        col = get_collection("fee_structures")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_fee_structures(
        course_id: Optional[str] = None,
        academic_year: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("fee_structures")
        query = {}
        if course_id:
            query["course_id"] = course_id
        if academic_year:
            query["academic_year"] = academic_year
        cursor = col.find(query).sort("fee_name", 1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_fee_structure(fee_id: str) -> Optional[Dict]:
        col = get_collection("fee_structures")
        doc = await col.find_one({"_id": ObjectId(fee_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_fee_structure(fee_id: str, data: dict) -> bool:
        col = get_collection("fee_structures")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(fee_id)}, {"$set": data})
        return result.modified_count > 0

    @staticmethod
    async def delete_fee_structure(fee_id: str) -> bool:
        col = get_collection("fee_structures")
        result = await col.delete_one({"_id": ObjectId(fee_id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_student_fees(
        student_id: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        col = get_collection("student_fees")
        query = {}
        if student_id:
            query["student_id"] = student_id
        if status:
            query["payment_status"] = status
        cursor = col.find(query).sort("due_date", 1)
        return _serialize_list(await cursor.to_list(length=500))


class PaymentReportService:

    @staticmethod
    async def create_report(data: dict) -> str:
        col = get_collection("payment_reports")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_reports(report_type: Optional[str] = None) -> List[Dict]:
        col = get_collection("payment_reports")
        query = {"report_type": report_type} if report_type else {}
        cursor = col.find(query).sort("created_at", -1)
        return _serialize_list(await cursor.to_list(length=100))

    @staticmethod
    async def get_report(report_id: str) -> Optional[Dict]:
        col = get_collection("payment_reports")
        doc = await col.find_one({"_id": ObjectId(report_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def delete_report(report_id: str) -> bool:
        col = get_collection("payment_reports")
        result = await col.delete_one({"_id": ObjectId(report_id)})
        return result.deleted_count > 0


class RevenueStatsService:

    @staticmethod
    async def get_revenue_by_period(period_type: str = "monthly") -> List[Dict]:
        col = get_collection("revenue_stats")
        cursor = col.find({"period_type": period_type}).sort("created_at", -1).limit(12)
        return _serialize_list(await cursor.to_list(length=12))

    @staticmethod
    async def get_course_revenue() -> List[Dict]:
        col = get_collection("course_revenue")
        cursor = col.find().sort("total_revenue", -1)
        return _serialize_list(await cursor.to_list(length=50))

    @staticmethod
    async def get_daily_revenue(days: int = 30) -> List[Dict]:
        col = get_collection("transactions")
        pipeline = [
            {"$match": {"status": "completed", "transaction_date": {"$gte": datetime.utcnow()}}},
            {"$group": {"_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$transaction_date"}}, "total": {"$sum": "$amount"}, "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ]
        cursor = col.aggregate(pipeline)
        return [{"date": doc["_id"], "total": doc["total"], "count": doc["count"]} for doc in await cursor.to_list(length=days)]


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


class InvoiceService:

    @staticmethod
    async def create_invoice(data: dict) -> str:
        col = get_collection("invoices")
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = await col.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_invoices(status: Optional[str] = None) -> List[Dict]:
        col = get_collection("invoices")
        query = {"status": status} if status else {}
        cursor = col.find(query).sort("issued_date", -1)
        return _serialize_list(await cursor.to_list(length=200))

    @staticmethod
    async def get_invoice(invoice_id: str) -> Optional[Dict]:
        col = get_collection("invoices")
        doc = await col.find_one({"_id": ObjectId(invoice_id)})
        return _serialize(doc) if doc else None

    @staticmethod
    async def update_invoice(invoice_id: str, data: dict) -> bool:
        col = get_collection("invoices")
        data["updated_at"] = datetime.utcnow()
        result = await col.update_one({"_id": ObjectId(invoice_id)}, {"$set": data})
        return result.modified_count > 0
