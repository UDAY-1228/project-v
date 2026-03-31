"""
HRMS - Services
===============
Business logic services for the HRMS workspace.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, date
from bson import ObjectId
from .mongodb_connection import get_collection


def serialize_doc(doc: Dict) -> Dict:
    """Convert MongoDB document to JSON-serializable dict."""
    if doc is None:
        return None
    doc["_id"] = str(doc["_id"])
    return doc


def serialize_docs(docs: List[Dict]) -> List[Dict]:
    """Convert multiple MongoDB documents to JSON-serializable dicts."""
    return [serialize_doc(doc) for doc in docs]


class EmployeeService:
    collection_name = "employees"

    @staticmethod
    async def create_employee(employee_data: Dict) -> Dict:
        employee_data["created_at"] = datetime.utcnow()
        employee_data["updated_at"] = datetime.utcnow()
        collection = get_collection(EmployeeService.collection_name)
        result = await collection.insert_one(employee_data)
        employee_data["_id"] = str(result.inserted_id)
        return employee_data

    @staticmethod
    async def get_employee(employee_id: str) -> Optional[Dict]:
        collection = get_collection(EmployeeService.collection_name)
        doc = await collection.find_one({"employee_id": employee_id})
        return serialize_doc(doc)

    @staticmethod
    async def get_employee_by_id(id: str) -> Optional[Dict]:
        collection = get_collection(EmployeeService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_all_employees(
        skip: int = 0, limit: int = 100, department: Optional[str] = None, status: Optional[str] = None
    ) -> List[Dict]:
        collection = get_collection(EmployeeService.collection_name)
        query = {}
        if department:
            query["department"] = department
        if status:
            query["status"] = status
        cursor = collection.find(query).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_employee(employee_id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(EmployeeService.collection_name)
        update_data["updated_at"] = datetime.utcnow()
        result = await collection.find_one_and_update(
            {"employee_id": employee_id}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_employee(employee_id: str) -> bool:
        collection = get_collection(EmployeeService.collection_name)
        result = await collection.delete_one({"employee_id": employee_id})
        return result.deleted_count > 0

    @staticmethod
    async def count_employees(status: Optional[str] = None) -> int:
        collection = get_collection(EmployeeService.collection_name)
        query = {"status": status} if status else {}
        return await collection.count_documents(query)

    @staticmethod
    async def count_employees_joined_after(joined_after: date) -> int:
        collection = get_collection(EmployeeService.collection_name)
        return await collection.count_documents({"joining_date": {"$gte": joined_after.isoformat()}})


class AttendanceService:
    collection_name = "attendance"

    @staticmethod
    async def create_attendance(attendance_data: Dict) -> Dict:
        collection = get_collection(AttendanceService.collection_name)
        result = await collection.insert_one(attendance_data)
        attendance_data["_id"] = str(result.inserted_id)
        return attendance_data

    @staticmethod
    async def get_attendance(employee_id: str, date_val: date) -> Optional[Dict]:
        collection = get_collection(AttendanceService.collection_name)
        doc = await collection.find_one({"employee_id": employee_id, "date": date_val})
        return serialize_doc(doc)

    @staticmethod
    async def get_attendance_by_id(id: str) -> Optional[Dict]:
        collection = get_collection(AttendanceService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_attendance_records(
        skip: int = 0, limit: int = 100, employee_id: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None
    ) -> List[Dict]:
        collection = get_collection(AttendanceService.collection_name)
        query = {}
        if employee_id:
            query["employee_id"] = employee_id
        if start_date and end_date:
            query["date"] = {"$gte": start_date, "$lte": end_date}
        cursor = collection.find(query).sort("date", -1).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_attendance(id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(AttendanceService.collection_name)
        result = await collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_attendance(id: str) -> bool:
        collection = get_collection(AttendanceService.collection_name)
        result = await collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_present_today() -> int:
        collection = get_collection(AttendanceService.collection_name)
        today = date.today()
        return await collection.count_documents({"date": today, "status": {"$in": ["present", "late"]}})


class LeaveService:
    collection_name = "leave_requests"

    @staticmethod
    async def create_leave_request(leave_data: Dict) -> Dict:
        leave_data["created_at"] = datetime.utcnow()
        collection = get_collection(LeaveService.collection_name)
        result = await collection.insert_one(leave_data)
        leave_data["_id"] = str(result.inserted_id)
        return leave_data

    @staticmethod
    async def get_leave_request(id: str) -> Optional[Dict]:
        collection = get_collection(LeaveService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_leave_requests(
        skip: int = 0, limit: int = 100, employee_id: Optional[str] = None, status: Optional[str] = None
    ) -> List[Dict]:
        collection = get_collection(LeaveService.collection_name)
        query = {}
        if employee_id:
            query["employee_id"] = employee_id
        if status:
            query["status"] = status
        cursor = collection.find(query).sort("created_at", -1).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_leave_request(id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(LeaveService.collection_name)
        if update_data.get("status") == "approved":
            update_data["approved_date"] = datetime.utcnow()
        result = await collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_leave_request(id: str) -> bool:
        collection = get_collection(LeaveService.collection_name)
        result = await collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_on_leave_count() -> int:
        collection = get_collection(LeaveService.collection_name)
        today = date.today()
        return await collection.count_documents({
            "status": "approved",
            "start_date": {"$lte": today},
            "end_date": {"$gte": today}
        })


class PayrollService:
    collection_name = "payroll"

    @staticmethod
    async def create_payroll(payroll_data: Dict) -> Dict:
        payroll_data["net_salary"] = (
            payroll_data["basic_salary"]
            + payroll_data.get("allowances", 0)
            + payroll_data.get("overtime_pay", 0)
            + payroll_data.get("bonuses", 0)
            - payroll_data.get("deductions", 0)
            - payroll_data.get("tax", 0)
        )
        collection = get_collection(PayrollService.collection_name)
        result = await collection.insert_one(payroll_data)
        payroll_data["_id"] = str(result.inserted_id)
        return payroll_data

    @staticmethod
    async def get_payroll(id: str) -> Optional[Dict]:
        collection = get_collection(PayrollService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_payroll_records(
        skip: int = 0, limit: int = 100, employee_id: Optional[str] = None, month: Optional[int] = None, year: Optional[int] = None
    ) -> List[Dict]:
        collection = get_collection(PayrollService.collection_name)
        query = {}
        if employee_id:
            query["employee_id"] = employee_id
        if month:
            query["month"] = month
        if year:
            query["year"] = year
        cursor = collection.find(query).sort([("year", -1), ("month", -1)]).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_payroll(id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(PayrollService.collection_name)
        result = await collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_payroll(id: str) -> bool:
        collection = get_collection(PayrollService.collection_name)
        result = await collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_pending_payroll_count() -> int:
        collection = get_collection(PayrollService.collection_name)
        return await collection.count_documents({"status": "pending"})


class RecruitmentService:
    collection_name = "positions"

    @staticmethod
    async def create_position(position_data: Dict) -> Dict:
        position_data["created_at"] = datetime.utcnow()
        collection = get_collection(RecruitmentService.collection_name)
        result = await collection.insert_one(position_data)
        position_data["_id"] = str(result.inserted_id)
        return position_data

    @staticmethod
    async def get_position(id: str) -> Optional[Dict]:
        collection = get_collection(RecruitmentService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_positions(
        skip: int = 0, limit: int = 100, department: Optional[str] = None, status: Optional[str] = None
    ) -> List[Dict]:
        collection = get_collection(RecruitmentService.collection_name)
        query = {}
        if department:
            query["department"] = department
        if status:
            query["status"] = status
        cursor = collection.find(query).sort("created_at", -1).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_position(id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(RecruitmentService.collection_name)
        result = await collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_position(id: str) -> bool:
        collection = get_collection(RecruitmentService.collection_name)
        result = await collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_open_positions_count() -> int:
        collection = get_collection(RecruitmentService.collection_name)
        return await collection.count_documents({"status": "open"})


class ApplicationService:
    collection_name = "applications"

    @staticmethod
    async def create_application(application_data: Dict) -> Dict:
        application_data["applied_at"] = datetime.utcnow()
        collection = get_collection(ApplicationService.collection_name)
        result = await collection.insert_one(application_data)
        application_data["_id"] = str(result.inserted_id)
        return application_data

    @staticmethod
    async def get_application(id: str) -> Optional[Dict]:
        collection = get_collection(ApplicationService.collection_name)
        doc = await collection.find_one({"_id": ObjectId(id)})
        return serialize_doc(doc)

    @staticmethod
    async def get_applications(
        skip: int = 0, limit: int = 100, position_id: Optional[str] = None, status: Optional[str] = None
    ) -> List[Dict]:
        collection = get_collection(ApplicationService.collection_name)
        query = {}
        if position_id:
            query["position_id"] = position_id
        if status:
            query["status"] = status
        cursor = collection.find(query).sort("applied_at", -1).skip(skip).limit(limit)
        docs = await cursor.to_list(length=limit)
        return serialize_docs(docs)

    @staticmethod
    async def update_application(id: str, update_data: Dict) -> Optional[Dict]:
        collection = get_collection(ApplicationService.collection_name)
        result = await collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_data}, return_document=True
        )
        return serialize_doc(result)

    @staticmethod
    async def delete_application(id: str) -> bool:
        collection = get_collection(ApplicationService.collection_name)
        result = await collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_new_applications_count() -> int:
        collection = get_collection(ApplicationService.collection_name)
        return await collection.count_documents({"status": "new"})


class ReportsService:
    collection_name = "employees"

    @staticmethod
    async def get_employee_report(department: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> Dict:
        collection = get_collection(ReportsService.collection_name)
        query = {}
        if department:
            query["department"] = department
        if start_date and end_date:
            query["joining_date"] = {"$gte": start_date.isoformat() if start_date else None, "$lte": end_date.isoformat() if end_date else None}
        
        pipeline = [
            {"$match": query},
            {"$group": {
                "_id": "$department",
                "count": {"$sum": 1},
                "avg_salary": {"$avg": "$salary"}
            }}
        ]
        
        cursor = collection.aggregate(pipeline)
        results = await cursor.to_list(length=100)
        
        thirty_days_ago = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        thirty_days_ago = thirty_days_ago.replace(day=max(1, thirty_days_ago.day - 30))
        
        recent_hires = await collection.count_documents({
            **query,
            "joining_date": {"$gte": thirty_days_ago.isoformat() if hasattr(thirty_days_ago, "isoformat") else str(thirty_days_ago.date())}
        })
        
        return {
            "department_breakdown": [{"department": r["_id"], "count": r["count"], "avg_salary": r.get("avg_salary", 0)} for r in results],
            "total_employees": await collection.count_documents(query),
            "recent_hires": recent_hires
        }

    @staticmethod
    async def get_attendance_report(start_date: date, end_date: date, department: Optional[str] = None) -> Dict:
        attendance_collection = get_collection("attendance")
        employee_collection = get_collection("employees")
        
        query = {"date": {"$gte": start_date, "$lte": end_date}}
        pipeline = [
            {"$match": query},
            {"$group": {
                "_id": "$status",
                "count": {"$sum": 1}
            }}
        ]
        
        cursor = attendance_collection.aggregate(pipeline)
        status_counts = await cursor.to_list(length=100)
        
        return {
            "status_breakdown": {r["_id"]: r["count"] for r in status_counts},
            "total_records": sum(r["count"] for r in status_counts)
        }


class SettingsService:
    collection_name = "settings"

    @staticmethod
    async def get_settings() -> Dict:
        collection = get_collection(SettingsService.collection_name)
        doc = await collection.find_one({"type": "system"})
        if doc:
            return serialize_doc(doc)
        default_settings = {
            "type": "system",
            "company_name": "Organization",
            "working_hours_start": "09:00",
            "working_hours_end": "17:00",
            "late_threshold_minutes": 15,
            "overtime_rate": 1.5,
            "casual_leave_limit": 12,
            "sick_leave_limit": 10,
            "annual_leave_limit": 20
        }
        result = await collection.insert_one(default_settings)
        default_settings["_id"] = str(result.inserted_id)
        return default_settings

    @staticmethod
    async def update_settings(settings_data: Dict) -> Dict:
        collection = get_collection(SettingsService.collection_name)
        result = await collection.find_one_and_update(
            {"type": "system"}, {"$set": settings_data}, upsert=True, return_document=True
        )
        return serialize_doc(result)
