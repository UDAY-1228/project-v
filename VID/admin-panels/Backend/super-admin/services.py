from bson import ObjectId
from .mongodb_connection import get_db_connection
from .models import Institution
from datetime import datetime

db = get_db_connection()
institutions_collection = db["institutions"]
logs_collection = db["system_logs"]

class InstitutionService:
    @staticmethod
    def create_institution(data: dict):
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        result = institutions_collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_all_institutions():
        return list(institutions_collection.find())

    @staticmethod
    def get_institution_by_id(inst_id: str):
        return institutions_collection.find_one({"_id": ObjectId(inst_id)})

    @staticmethod
    def update_institution(inst_id: str, data: dict):
        data["updated_at"] = datetime.utcnow()
        result = institutions_collection.update_one(
            {"_id": ObjectId(inst_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    def delete_institution(inst_id: str):
        result = institutions_collection.delete_one({"_id": ObjectId(inst_id)})
        return result.deleted_count > 0

    @staticmethod
    def activate_deactivate_institution(inst_id: str, is_active: bool):
        result = institutions_collection.update_one(
            {"_id": ObjectId(inst_id)}, {"$set": {"is_active": is_active, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

class StatisticsService:
    @staticmethod
    def get_overview_statistics():
        total = institutions_collection.count_documents({})
        active = institutions_collection.count_documents({"is_active": True})
        inactive = total - active
        # Simplified revenue calculation for current statistics view
        # In practice, this would query a revenue tracking collection
        return {
            "total_institutions": total,
            "active_institutions": active,
            "inactive_institutions": inactive,
            "total_revenue": 0.0, # Placeholder
            "monthly_revenue": 0.0, # Placeholder
            "usage_overview": []
        }

class MonitoringService:
    @staticmethod
    def get_system_logs():
        return list(logs_collection.find().limit(100).sort("timestamp", -1))
