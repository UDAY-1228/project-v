#!/usr/bin/env python3
"""
VID Workspace Backend Generator
Generates complete backend files for all workspace modules
"""

import os
from datetime import datetime

WORKSPACES = {
    "academic-coordinator": {
        "collection": "academic_coordinator",
        "pages": ["Dashboard", "Academic Management", "Courses", "Subjects", "Timetable", "Assessments", "Reports", "Notice Board", "Settings", "Logout"],
        "models": {
            "Course": {"name": "str", "code": "str", "credits": "int", "department": "str", "status": "str"},
            "Subject": {"name": "str", "code": "str", "course_id": "str", "faculty_id": "str", "semester": "str"},
            "Assessment": {"title": "str", "subject_id": "str", "type": "str", "max_marks": "int", "date": "datetime"},
            "Notice": {"title": "str", "content": "str", "priority": "str", "target_audience": "str"}
        }
    },
    "hrms": {
        "collection": "hrms",
        "pages": ["Dashboard", "Employee Management", "Attendance", "Payroll", "Leave Management", "Recruitment", "Reports", "Settings", "Logout"],
        "models": {
            "Employee": {"name": "str", "employee_id": "str", "email": "str", "department": "str", "designation": "str", "joining_date": "datetime"},
            "Attendance": {"employee_id": "str", "date": "date", "check_in": "datetime", "check_out": "datetime", "status": "str"},
            "Payroll": {"employee_id": "str", "month": "str", "basic_salary": "float", "deductions": "float", "net_salary": "float"},
            "Leave": {"employee_id": "str", "leave_type": "str", "start_date": "date", "end_date": "date", "status": "str", "reason": "str"},
            "Recruitment": {"position": "str", "department": "str", "requirements": "str", "status": "str", "posted_date": "datetime"}
        }
    },
    "admission-officer": {
        "collection": "admission_officer",
        "pages": ["Dashboard", "Applications", "Student Admissions", "Document Verification", "Fee Details", "Reports", "Settings", "Logout"],
        "models": {
            "Application": {"student_name": "str", "course": "str", "application_no": "str", "status": "str", "applied_date": "datetime"},
            "Admission": {"student_id": "str", "application_id": "str", "course": "str", "batch": "str", "admission_date": "datetime"},
            "Document": {"student_id": "str", "document_type": "str", "file_path": "str", "verified": "bool", "remarks": "str"},
            "FeeDetail": {"student_id": "str", "amount": "float", "payment_type": "str", "status": "str", "paid_date": "datetime"}
        }
    },
    "library-admin": {
        "collection": "library_admin",
        "pages": ["Dashboard", "Book Control", "Issue/Return", "Fine Control", "Reports", "Settings", "Logout"],
        "models": {
            "Book": {"title": "str", "author": "str", "isbn": "str", "category": "str", "copies": "int", "available": "int"},
            "Issue": {"book_id": "str", "member_id": "str", "issue_date": "datetime", "due_date": "datetime", "return_date": "datetime"},
            "Fine": {"member_id": "str", "book_id": "str", "amount": "float", "reason": "str", "paid": "bool", "paid_date": "datetime"}
        }
    },
    "ai-yantra": {
        "collection": "ai_yantra",
        "pages": ["Dashboard", "AI Tools", "Automation Panel", "Model Control", "Analytics", "Reports", "Settings", "Logout"],
        "models": {
            "AITool": {"name": "str", "type": "str", "endpoint": "str", "status": "str", "config": "dict"},
            "Automation": {"name": "str", "trigger": "str", "action": "str", "schedule": "str", "enabled": "bool"},
            "Model": {"name": "str", "version": "str", "accuracy": "float", "last_trained": "datetime", "status": "str"},
            "Analytics": {"metric": "str", "value": "float", "timestamp": "datetime", "category": "str"}
        }
    },
    "library-management": {
        "collection": "library_management",
        "pages": ["Dashboard", "Book Catalog", "Issue/Return", "Member Records", "Reports", "Settings", "Logout"],
        "models": {
            "Book": {"title": "str", "author": "str", "isbn": "str", "publisher": "str", "category": "str", "copies": "int"},
            "Member": {"name": "str", "member_id": "str", "email": "str", "phone": "str", "membership_type": "str"},
            "Issue": {"book_id": "str", "member_id": "str", "issue_date": "datetime", "due_date": "datetime", "status": "str"}
        }
    },
    "alumni-coordinator": {
        "collection": "alumni_coordinator",
        "pages": ["Dashboard", "Alumni Records", "Events", "Communication", "Reports", "Settings", "Logout"],
        "models": {
            "Alumni": {"name": "str", "graduation_year": "int", "course": "str", "email": "str", "company": "str", "designation": "str"},
            "Event": {"title": "str", "date": "datetime", "venue": "str", "attendees": "list", "status": "str"},
            "Communication": {"alumni_id": "str", "type": "str", "subject": "str", "sent_date": "datetime", "response": "str"}
        }
    },
    "parent-portal": {
        "collection": "parent_portal",
        "pages": ["Dashboard", "Student Progress", "Attendance", "Fee Status", "Notifications", "Settings", "Logout"],
        "models": {
            "StudentProgress": {"student_id": "str", "subject": "str", "marks": "float", "grade": "str", "term": "str"},
            "Attendance": {"student_id": "str", "date": "date", "status": "str", "period": "str", "remarks": "str"},
            "FeeStatus": {"student_id": "str", "amount": "float", "paid": "float", "due": "float", "status": "str"},
            "Notification": {"student_id": "str", "type": "str", "message": "str", "date": "datetime", "read": "bool"}
        }
    },
    "alumni-management": {
        "collection": "alumni_management",
        "pages": ["Dashboard", "Alumni Database", "Donations", "Events", "Reports", "Settings", "Logout"],
        "models": {
            "Alumni": {"name": "str", "email": "str", "phone": "str", "graduation_year": "int", "course": "str", "current_company": "str"},
            "Donation": {"alumni_id": "str", "amount": "float", "purpose": "str", "date": "datetime", "receipt_no": "str", "status": "str"},
            "Event": {"title": "str", "date": "datetime", "location": "str", "description": "str", "attendees": "list"}
        }
    },
    "payment-admin": {
        "collection": "payment_admin",
        "pages": ["Dashboard", "Transactions", "Fee Collection", "Payment Reports", "Revenue Stats", "Settings", "Logout"],
        "models": {
            "Transaction": {"transaction_id": "str", "student_id": "str", "amount": "float", "type": "str", "mode": "str", "date": "datetime", "status": "str"},
            "FeeCollection": {"student_id": "str", "total_fee": "float", "paid": "float", "due": "float", "due_date": "date"},
            "RevenueStats": {"month": "str", "total_collection": "float", "pending": "float", "category": "str"}
        }
    },
    "common": {
        "collection": "common",
        "pages": ["Login", "Register", "Forgot Password", "Notifications", "Profile", "Settings"],
        "models": {
            "User": {"username": "str", "email": "str", "password_hash": "str", "role": "str", "institution_id": "str"},
            "Notification": {"user_id": "str", "title": "str", "message": "str", "type": "str", "read": "bool", "created_at": "datetime"},
            "Profile": {"user_id": "str", "full_name": "str", "phone": "str", "avatar": "str", "bio": "str"}
        }
    },
    "placement-cell": {
        "collection": "placement_cell",
        "pages": ["Dashboard", "Companies", "Job Drives", "Student Applications", "Reports", "Settings", "Logout"],
        "models": {
            "Company": {"name": "str", "industry": "str", "contact_person": "str", "email": "str", "visiting_date": "datetime"},
            "JobDrive": {"company_id": "str", "position": "str", "package": "float", "eligibility": "str", "status": "str"},
            "Application": {"student_id": "str", "job_drive_id": "str", "status": "str", "applied_date": "datetime", "result": "str"}
        }
    },
    "course-coordinator": {
        "collection": "course_coordinator",
        "pages": ["Dashboard", "Course Planning", "Subjects", "Faculty Allocation", "Reports", "Settings", "Logout"],
        "models": {
            "Course": {"name": "str", "code": "str", "duration": "str", "semesters": "int", "department": "str"},
            "Subject": {"name": "str", "code": "str", "credits": "int", "course_id": "str", "semester": "str"},
            "FacultyAllocation": {"faculty_id": "str", "subject_id": "str", "course_id": "str", "semester": "str", "academic_year": "str"}
        }
    },
    "principal-dashboard": {
        "collection": "principal_dashboard",
        "pages": ["Dashboard", "Institution Overview", "Staff Stats", "Student Stats", "Reports", "Policies", "Settings", "Logout"],
        "models": {
            "InstitutionStats": {"total_students": "int", "total_staff": "int", "total_courses": "int", "department": "str"},
            "Policy": {"title": "str", "description": "str", "effective_date": "date", "status": "str", "category": "str"},
            "Report": {"title": "str", "type": "str", "generated_date": "datetime", "file_path": "str"}
        }
    },
    "disciplinary-committee": {
        "collection": "disciplinary_committee",
        "pages": ["Dashboard", "Complaints", "Case Records", "Actions", "Reports", "Settings", "Logout"],
        "models": {
            "Complaint": {"complainant": "str", "respondent": "str", "description": "str", "date": "datetime", "status": "str"},
            "CaseRecord": {"complaint_id": "str", "case_no": "str", "hearing_date": "datetime", "decision": "str", "status": "str"},
            "Action": {"case_id": "str", "action_type": "str", "description": "str", "taken_by": "str", "date": "datetime"}
        }
    },
    "research-development": {
        "collection": "research_development",
        "pages": ["Dashboard", "Research Projects", "Publications", "Grants", "Reports", "Settings", "Logout"],
        "models": {
            "Project": {"title": "str", "principal_investigator": "str", "department": "str", "funding": "float", "start_date": "datetime", "status": "str"},
            "Publication": {"title": "str", "authors": "list", "journal": "str", "year": "int", "citations": "int"},
            "Grant": {"project_id": "str", "agency": "str", "amount": "float", "sanctioned_date": "datetime", "status": "str"}
        }
    },
    "employee": {
        "collection": "employee",
        "pages": ["Dashboard", "Attendance", "Tasks", "Leave Requests", "Profile", "Settings", "Logout"],
        "models": {
            "Task": {"title": "str", "description": "str", "assigned_by": "str", "due_date": "date", "status": "str", "priority": "str"},
            "LeaveRequest": {"leave_type": "str", "start_date": "date", "end_date": "date", "reason": "str", "status": "str"},
            "Attendance": {"date": "date", "check_in": "datetime", "check_out": "datetime", "status": "str", "remarks": "str"}
        }
    },
    "sports-officer": {
        "collection": "sports_officer",
        "pages": ["Dashboard", "Sports Events", "Teams", "Player Records", "Reports", "Settings", "Logout"],
        "models": {
            "Event": {"name": "str", "date": "datetime", "venue": "str", "type": "str", "status": "str"},
            "Team": {"name": "str", "sport": "str", "captain": "str", "members": "list", "coach": "str"},
            "PlayerRecord": {"player_id": "str", "sport": "str", "matches": "int", "achievements": "str", "performance": "str"}
        }
    },
    "event-management": {
        "collection": "event_management",
        "pages": ["Dashboard", "Events", "Registrations", "Scheduling", "Reports", "Settings", "Logout"],
        "models": {
            "Event": {"title": "str", "date": "datetime", "venue": "str", "organizer": "str", "status": "str", "max_attendees": "int"},
            "Registration": {"event_id": "str", "participant_id": "str", "name": "str", "email": "str", "registered_date": "datetime"},
            "Schedule": {"event_id": "str", "time": "datetime", "activity": "str", "speaker": "str", "venue": "str"}
        }
    },
    "student": {
        "collection": "student",
        "pages": ["Dashboard", "Courses", "Attendance", "Exams", "Results", "Fee Status", "Notifications", "Profile", "Settings", "Logout"],
        "models": {
            "Course": {"name": "str", "code": "str", "credits": "int", "faculty": "str", "semester": "str"},
            "Attendance": {"subject": "str", "date": "date", "status": "str", "percentage": "float"},
            "Exam": {"subject": "str", "date": "datetime", "duration": "str", "venue": "str", "status": "str"},
            "Result": {"subject": "str", "marks": "float", "grade": "str", "semester": "str", "exam_type": "str"},
            "FeeStatus": {"amount": "float", "paid": "float", "due": "float", "due_date": "date", "status": "str"}
        }
    },
    "examination": {
        "collection": "examination",
        "pages": ["Dashboard", "Exam Schedule", "Hall Tickets", "Results", "Reports", "Settings", "Logout"],
        "models": {
            "ExamSchedule": {"subject": "str", "date": "datetime", "time": "str", "duration": "str", "venue": "str"},
            "HallTicket": {"student_id": "str", "exam_ids": "list", "issued_date": "datetime", "status": "str"},
            "Result": {"student_id": "str", "subject": "str", "marks": "float", "total": "float", "grade": "str", "semester": "str"}
        }
    },
    "team-owner": {
        "collection": "team_owner",
        "pages": ["Dashboard", "Workspace Control", "Members", "Access Control", "Reports", "Settings", "Logout"],
        "models": {
            "Workspace": {"name": "str", "type": "str", "members": "list", "created_date": "datetime", "status": "str"},
            "Member": {"user_id": "str", "role": "str", "joined_date": "datetime", "permissions": "list"},
            "AccessControl": {"member_id": "str", "resource": "str", "permissions": "list", "granted_by": "str"}
        }
    },
    "faculty": {
        "collection": "faculty",
        "pages": ["Dashboard", "Classes", "Attendance", "Assignments", "Exams", "Reports", "Profile", "Settings", "Logout"],
        "models": {
            "Class": {"subject": "str", "course": "str", "semester": "str", "timing": "str", "students": "list"},
            "Assignment": {"title": "str", "subject": "str", "due_date": "datetime", "max_marks": "int", "description": "str"},
            "Exam": {"subject": "str", "date": "datetime", "duration": "str", "max_marks": "int", "type": "str"}
        }
    },
    "timetable": {
        "collection": "timetable",
        "pages": ["Dashboard", "Schedule Creation", "Class Allocation", "Room Allocation", "Reports", "Settings", "Logout"],
        "models": {
            "Schedule": {"course": "str", "subject": "str", "faculty": "str", "day": "str", "time": "str", "room": "str"},
            "ClassAllocation": {"course": "str", "semester": "str", "subjects": "list", "faculty": "str"},
            "RoomAllocation": {"room": "str", "day": "str", "period": "str", "allocation_type": "str", "reference_id": "str"}
        }
    },
    "health-monitoring": {
        "collection": "health_monitoring",
        "pages": ["Dashboard", "Health Records", "Medical Reports", "Alerts", "Reports", "Settings", "Logout"],
        "models": {
            "HealthRecord": {"student_id": "str", "blood_group": "str", "allergies": "list", "conditions": "list", "emergency_contact": "str"},
            "MedicalReport": {"student_id": "str", "report_type": "str", "date": "datetime", "doctor": "str", "findings": "str"},
            "Alert": {"student_id": "str", "type": "str", "message": "str", "severity": "str", "created_at": "datetime", "resolved": "bool"}
        }
    },
    "transport-coordinator": {
        "collection": "transport_coordinator",
        "pages": ["Dashboard", "Vehicles", "Routes", "Student Transport", "Reports", "Settings", "Logout"],
        "models": {
            "Vehicle": {"vehicle_no": "str", "type": "str", "capacity": "int", "driver_name": "str", "status": "str"},
            "Route": {"route_no": "str", "stops": "list", "pickup_time": "str", "drop_time": "str", "vehicle_id": "str"},
            "StudentTransport": {"student_id": "str", "route_id": "str", "pickup_point": "str", "drop_point": "str", "status": "str"}
        }
    },
    "hostel-admin": {
        "collection": "hostel_admin",
        "pages": ["Dashboard", "Rooms", "Students", "Fee Records", "Complaints", "Reports", "Settings", "Logout"],
        "models": {
            "Room": {"room_no": "str", "block": "str", "capacity": "int", "occupied": "int", "floor": "int", "status": "str"},
            "Student": {"student_id": "str", "name": "str", "room_id": "str", "join_date": "datetime", "status": "str"},
            "FeeRecord": {"student_id": "str", "amount": "float", "due_date": "date", "paid": "float", "status": "str"},
            "Complaint": {"student_id": "str", "room_id": "str", "subject": "str", "description": "str", "status": "str", "date": "datetime"}
        }
    },
    "voice-agent": {
        "collection": "voice_agent",
        "pages": ["Dashboard", "Voice Commands", "AI Conversations", "Logs", "Reports", "Settings", "Logout"],
        "models": {
            "VoiceCommand": {"command": "str", "intent": "str", "entities": "dict", "executed": "bool", "timestamp": "datetime"},
            "Conversation": {"session_id": "str", "user_id": "str", "messages": "list", "created_at": "datetime"},
            "Log": {"action": "str", "user_id": "str", "timestamp": "datetime", "status": "str", "details": "str"}
        }
    }
}

def generate_mongodb_connection(workspace: str) -> str:
    return f'''from pymongo import MongoClient
import os

def get_db_connection():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongo_uri)
    db = client["vid_{workspace.replace("-", "_")}"]
    return db

def get_collection(collection_name: str):
    db = get_db_connection()
    return db[collection_name]
'''

def generate_models(workspace: str, models: dict) -> str:
    lines = [
        "from pydantic import BaseModel, Field",
        "from typing import Optional, List, Dict",
        "from datetime import datetime, date",
        f"from .{mongodb_connection} import get_collection",
        "",
        "",
    ]
    
    for model_name, fields in models.items():
        lines.append(f"class {model_name}(BaseModel):")
        lines.append(f'    id: Optional[str] = Field(None, alias="_id")')
        for field_name, field_type in fields.items():
            lines.append(f"    {field_name}: {field_type}")
        lines.append("")
    
    lines.append("")
    return "\n".join(lines)

def generate_services(workspace: str, models: dict) -> str:
    collection = WORKSPACES[workspace]["collection"]
    lines = [
        "from .mongodb_connection import get_collection",
        "from datetime import datetime",
        "from typing import List, Optional",
        "from bson import ObjectId",
        "",
    ]
    
    for model_name in models.keys():
        collection_name = collection
        model_var = model_name.lower()
        lines.extend([
            f"",
            f"class {model_name}Service:",
            f'    collection_name = "{collection_name}"',
            f"",
            f"    @staticmethod",
            f"    async def create(data: dict) -> dict:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        data['created_at'] = datetime.utcnow()",
            f"        data['updated_at'] = datetime.utcnow()",
            f"        result = collection.insert_one(data)",
            f"        data['_id'] = str(result.inserted_id)",
            f"        return data",
            f"",
            f"    @staticmethod",
            f"    async def get_all(limit: int = 100) -> List[dict]:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        items = list(collection.find().limit(limit))",
            f"        for item in items:",
            f"            item['_id'] = str(item['_id'])",
            f"        return items",
            f"",
            f"    @staticmethod",
            f"    async def get_by_id(id: str) -> Optional[dict]:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        item = collection.find_one({{'_id': ObjectId(id)}})",
            f"        if item:",
            f"            item['_id'] = str(item['_id'])",
            f"        return item",
            f"",
            f"    @staticmethod",
            f"    async def update(id: str, data: dict) -> Optional[dict]:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        data['updated_at'] = datetime.utcnow()",
            f"        result = collection.update_one({{'_id': ObjectId(id)}}, {{'$set': data}})",
            f"        if result.modified_count:",
            f"            return await {model_name}Service.get_by_id(id)",
            f"        return None",
            f"",
            f"    @staticmethod",
            f"    async def delete(id: str) -> bool:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        result = collection.delete_one({{'_id': ObjectId(id)}})",
            f"        return result.deleted_count > 0",
            f"",
            f"    @staticmethod",
            f"    async def search(query: dict, limit: int = 100) -> List[dict]:",
            f"        collection = get_collection({model_name}Service.collection_name)",
            f"        items = list(collection.find(query).limit(limit))",
            f"        for item in items:",
            f"            item['_id'] = str(item['_id'])",
            f"        return items",
        ])
    
    return "\n".join(lines)

def generate_routes(workspace: str, models: dict) -> str:
    lines = [
        "from fastapi import APIRouter, HTTPException, Depends, Query",
        "from typing import List, Optional",
        "from datetime import datetime",
        "from .services import *",
        "",
        "router = APIRouter()",
        "",
    ]
    
    for model_name in models.keys():
        service = f"{model_name}Service"
        model_var = model_name.lower()
        lines.extend([
            "",
            f"@router.post('/{model_var}s', response_model=dict, status_code=201)",
            f"async def create_{model_var}(data: dict):",
            f"    return await {service}.create(data)",
            "",
            f"@router.get('/{model_var}s', response_model=List[dict])",
            f"async def get_{model_var}s(limit: int = Query(100, ge=1, le=500)):",
            f"    return await {service}.get_all(limit)",
            "",
            f"@router.get('/{model_var}s/{{id}}', response_model=dict)",
            f"async def get_{model_var}(id: str):",
            f"    result = await {service}.get_by_id(id)",
            f"    if not result:",
            f"        raise HTTPException(status_code=404, detail='{model_name} not found')",
            f"    return result",
            "",
            f"@router.put('/{model_var}s/{{id}}', response_model=dict)",
            f"async def update_{model_var}(id: str, data: dict):",
            f"    result = await {service}.update(id, data)",
            f"    if not result:",
            f"        raise HTTPException(status_code=404, detail='{model_name} not found')",
            f"    return result",
            "",
            f"@router.delete('/{model_var}s/{{id}}')",
            f"async def delete_{model_var}(id: str):",
            f"    success = await {service}.delete(id)",
            f"    if not success:",
            f"        raise HTTPException(status_code=404, detail='{model_name} not found')",
            f"    return {{'message': '{model_name} deleted successfully'}}",
            "",
            f"@router.post('/{model_var}s/search', response_model=List[dict])",
            f"async def search_{model_var}s(query: dict, limit: int = Query(100, ge=1, le=500)):",
            f"    return await {service}.search(query, limit)",
        ])
    
    lines.extend([
        "",
        "@router.get('/health')",
        "async def health_check():",
        "    return {'status': 'healthy', 'workspace': '" + workspace + "', 'timestamp': datetime.utcnow().isoformat()}",
    ])
    
    return "\n".join(lines)

def generate_frontend_component(page: str, workspace: str) -> str:
    return f'''import React, {{ useState, useEffect }} from 'react';
import {{ LayoutDashboard, Search, Bell, Settings, LogOut, ChevronRight, Plus, Edit, Trash2, Eye }} from 'lucide-react';

const {page.replace(" ", "")}Page: React.FC = () => {{
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {{
    fetchData();
  }}, []);

  const fetchData = async () => {{
    try {{
      setLoading(true);
      // API call would go here
      setData([]);
    }} catch (error) {{
      console.error('Error fetching data:', error);
    }} finally {{
      setLoading(false);
    }}
  }};

  const filteredData = data.filter(item =>
    JSON.stringify(item).toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flex flex-col gap-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-black">{page}</h1>
          <p className="text-gray-500 mt-1">Manage {page.toLowerCase()} for your institution</p>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-black text-white rounded-xl font-semibold hover:bg-gray-800 transition-all">
          <Plus size={18} />
          Add New
        </button>
      </header>

      <div className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
        <div className="flex items-center gap-4 mb-6">
          <div className="relative flex-1 max-w-md">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
            <input
              type="text"
              placeholder="Search..."
              value={{searchTerm}}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
            />
          </div>
        </div>

        {{loading ? (
          <div className="text-center py-12 text-gray-500">Loading...</div>
        ) : filteredData.length === 0 ? (
          <div className="text-center py-12 text-gray-500">
            No {page.toLowerCase()} found. Click "Add New" to create one.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-100">
                  <th className="text-left py-3 px-4 text-xs font-bold text-gray-400 uppercase tracking-wider">ID</th>
                  <th className="text-left py-3 px-4 text-xs font-bold text-gray-400 uppercase tracking-wider">Name</th>
                  <th className="text-left py-3 px-4 text-xs font-bold text-gray-400 uppercase tracking-wider">Status</th>
                  <th className="text-left py-3 px-4 text-xs font-bold text-gray-400 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody>
                {{filteredData.map((item, index) => (
                  <tr key={{index}} className="border-b border-gray-50 hover:bg-gray-50">
                    <td className="py-3 px-4 text-sm">{{item._id || 'N/A'}}</td>
                    <td className="py-3 px-4 text-sm font-medium">{{item.name || 'N/A'}}</td>
                    <td className="py-3 px-4">
                      <span className="px-2 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full">
                        {{item.status || 'Active'}}
                      </span>
                    </td>
                    <td className="py-3 px-4">
                      <div className="flex items-center gap-2">
                        <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                          <Eye size={16} className="text-gray-500" />
                        </button>
                        <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                          <Edit size={16} className="text-gray-500" />
                        </button>
                        <button className="p-2 hover:bg-red-50 rounded-lg transition-colors">
                          <Trash2 size={16} className="text-red-500" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}}
              </tbody>
            </table>
          </div>
        )}}
      </div>
    </div>
  );
}};

export default {page.replace(" ", "")}Page;
'''

def generate_frontend_dashboard(workspace: str, pages: list) -> str:
    pages_json = ", ".join([f'"{p}"' for p in pages])
    return f'''import React, {{ useState, useEffect }} from 'react';
import {{ Link, useLocation }} from 'react-router-dom';
import {{ 
  LayoutDashboard, Users, BookOpen, Calendar, FileText, 
  Settings, LogOut, Bell, Search, ChevronRight, 
  BarChart3, Clock, CheckCircle, AlertCircle
}} from 'lucide-react';

const DashboardPage: React.FC = () => {{
  const location = useLocation();
  const [stats, setStats] = useState([
    {{ label: 'Total Records', value: '0', icon: FileText, color: 'bg-blue-50' }},
    {{ label: 'Active', value: '0', icon: CheckCircle, color: 'bg-green-50' }},
    {{ label: 'Pending', value: '0', icon: Clock, color: 'bg-yellow-50' }},
    {{ label: 'Reports', value: '0', icon: BarChart3, color: 'bg-purple-50' }},
  ]);

  const pages = [{pages_json}];

  const recentActivity = [
    {{ id: 1, action: 'Record created', time: '2 hours ago', type: 'success' }},
    {{ id: 2, action: 'Status updated', time: '5 hours ago', type: 'info' }},
    {{ id: 3, action: 'New entry added', time: '1 day ago', type: 'success' }},
  ];

  return (
    <div className="flex flex-col gap-8">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-black text-black capitalize">{workspace.replace('-', ' ')}</h1>
          <p className="text-lg text-gray-500 mt-1">Welcome back! Here\'s your workspace overview.</p>
        </div>
        <div className="flex gap-4">
          <button className="p-3 bg-white rounded-xl border border-gray-200 hover:border-black transition-colors relative">
            <Bell size={20} className="text-gray-600" />
            <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full"></span>
          </button>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {{stats.map((stat, index) => (
          <div key={{index}} className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
            <div className={{`w-12 h-12 ${{stat.color}} rounded-xl flex items-center justify-center mb-4`}}>
              <stat.icon size={24} className="text-gray-700" />
            </div>
            <span className="text-3xl font-black text-black">{{stat.value}}</span>
            <span className="block text-sm text-gray-500 mt-1">{{stat.label}}</span>
          </div>
        ))}}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
          <h2 className="text-xl font-bold mb-4">Quick Actions</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {{pages.filter(p => !['Settings', 'Logout', 'Dashboard'].includes(p)).slice(0, 6).map((page, index) => (
              <Link
                key={{index}}
                to={{`/workspaces/{workspace}/${{page.toLowerCase().replace(/ /g, '-')}}`}}
                className="p-4 rounded-xl border border-dashed border-gray-200 hover:border-black hover:bg-gray-50 transition-all text-center group"
              >
                <span className="text-2xl mb-2 block">{{['📋', '👥', '📚', '📅', '📊', '📝'][index] || '📄'}}</span>
                <span className="text-sm font-medium text-gray-600 group-hover:text-black">{{page}}</span>
              </Link>
            ))}}
          </div>
        </div>

        <div className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
          <h2 className="text-xl font-bold mb-4">Recent Activity</h2>
          <div className="space-y-4">
            {{recentActivity.map((activity) => (
              <div key={{activity.id}} className="flex items-start gap-3">
                <div className={{`w-2 h-2 mt-2 rounded-full ${{
                  'bg-green-500': activity.type === 'success',
                  'bg-blue-500': activity.type === 'info',
                  'bg-yellow-500': activity.type === 'warning'
                }}}`}} />
                <div>
                  <p className="text-sm font-medium">{{activity.action}}</p>
                  <p className="text-xs text-gray-500">{{activity.time}}</p>
                </div>
              </div>
            ))}}
          </div>
        </div>
      </div>
    </div>
  );
}};

export default DashboardPage;
'''

def generate_frontend_settings(workspace: str) -> str:
    return f'''import React, {{ useState }} from 'react';
import {{ Settings, User, Bell, Shield, Palette, Globe } from 'lucide-react';

const SettingsPage: React.FC = () => {{
  const [activeTab, setActiveTab] = useState('profile');
  const [formData, setFormData] = useState({{
    fullName: '',
    email: '',
    phone: '',
    currentPassword: '',
    newPassword: '',
    notifications: true,
    emailNotifications: true,
  }});

  const tabs = [
    {{ id: 'profile', label: 'Profile', icon: User }},
    {{ id: 'notifications', label: 'Notifications', icon: Bell }},
    {{ id: 'security', label: 'Security', icon: Shield }},
    {{ id: 'preferences', label: 'Preferences', icon: Palette }},
  ];

  const handleSubmit = (e: React.FormEvent) => {{
    e.preventDefault();
    console.log('Settings saved:', formData);
  }};

  return (
    <div className="flex flex-col gap-6">
      <header>
        <h1 className="text-3xl font-bold text-black">Settings</h1>
        <p className="text-gray-500 mt-1">Manage your account settings and preferences</p>
      </header>

      <div className="bg-white rounded-2xl border border-gray-200 overflow-hidden">
        <div className="flex">
          <div className="w-64 border-r border-gray-100 p-6">
            <nav className="space-y-1">
              {{tabs.map((tab) => (
                <button
                  key={{tab.id}}
                  onClick={() => setActiveTab(tab.id)}
                  className={{`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all ${{
                    activeTab === tab.id 
                      ? 'bg-black text-white' 
                      : 'text-gray-600 hover:bg-gray-100'
                  }}}`}}
                >
                  <tab.icon size={18} />
                  {{tab.label}}
                </button>
              ))}}
            </nav>
          </div>

          <div className="flex-1 p-6">
            <form onSubmit={{handleSubmit}} className="space-y-6">
              {{activeTab === 'profile' && (
                <>
                  <div className="grid grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
                      <input
                        type="text"
                        value={{formData.fullName}}
                        onChange={(e) => setFormData({{...formData, fullName: e.target.value}})}
                        className="w-full px-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
                      <input
                        type="email"
                        value={{formData.email}}
                        onChange={(e) => setFormData({{...formData, email: e.target.value}})}
                        className="w-full px-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Phone</label>
                    <input
                      type="tel"
                      value={{formData.phone}}
                      onChange={(e) => setFormData({{...formData, phone: e.target.value}})}
                      className="w-full px-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
                    />
                  </div>
                </>
              )}}

              {{activeTab === 'security' && (
                <>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Current Password</label>
                    <input
                      type="password"
                      value={{formData.currentPassword}}
                      onChange={(e) => setFormData({{...formData, currentPassword: e.target.value}})}
                      className="w-full px-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">New Password</label>
                    <input
                      type="password"
                      value={{formData.newPassword}}
                      onChange={(e) => setFormData({{...formData, newPassword: e.target.value}})}
                      className="w-full px-4 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black/10"
                    />
                  </div>
                </>
              )}}

              {{activeTab === 'notifications' && (
                <div className="space-y-4">
                  <label className="flex items-center gap-3">
                    <input
                      type="checkbox"
                      checked={{formData.notifications}}
                      onChange={(e) => setFormData({{...formData, notifications: e.target.checked}})}
                      className="w-5 h-5 rounded border-gray-300"
                    />
                    <span className="text-sm">Push notifications</span>
                  </label>
                  <label className="flex items-center gap-3">
                    <input
                      type="checkbox"
                      checked={{formData.emailNotifications}}
                      onChange={(e) => setFormData({{...formData, emailNotifications: e.target.checked}})}
                      className="w-5 h-5 rounded border-gray-300"
                    />
                    <span className="text-sm">Email notifications</span>
                  </label>
                </>
              )}}

              <div className="pt-4 border-t border-gray-100">
                <button
                  type="submit"
                  className="px-6 py-2 bg-black text-white rounded-xl font-semibold hover:bg-gray-800 transition-all"
                >
                  Save Changes
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}};

export default SettingsPage;
'''

def main():
    base_path = "/Users/nivas/Documents/React apps/v/project-v/VID/workspaces"
    frontend_base_path = "/Users/nivas/Documents/React apps/v/project-v/VID/admin-panels/Frontend/core-system/src"
    
    print("Starting VID Workspace Generation...")
    print("=" * 50)
    
    for workspace, config in WORKSPACES.items():
        print(f"\nProcessing workspace: {workspace}")
        workspace_path = f"{base_path}/{workspace}"
        backend_path = f"{workspace_path}/backend"
        frontend_path = f"{frontend_base_path}/workspaces/{workspace}"
        
        os.makedirs(backend_path, exist_ok=True)
        os.makedirs(frontend_path, exist_ok=True)
        
        # Generate backend files
        print("  - Generating mongodb_connection.py...")
        with open(f"{backend_path}/mongodb_connection.py", "w") as f:
            f.write(generate_mongodb_connection(workspace))
        
        print("  - Generating models.py...")
        with open(f"{backend_path}/models.py", "w") as f:
            f.write(generate_models(workspace, config["models"]))
        
        print("  - Generating services.py...")
        with open(f"{backend_path}/services.py", "w") as f:
            f.write(generate_services(workspace, config["models"]))
        
        print("  - Generating routes.py...")
        with open(f"{backend_path}/routes.py", "w") as f:
            f.write(generate_routes(workspace, config["models"]))
        
        # Generate frontend files
        print("  - Generating Dashboard.tsx...")
        with open(f"{frontend_path}/Dashboard.tsx", "w") as f:
            f.write(generate_frontend_dashboard(workspace, config["pages"]))
        
        print("  - Generating Settings.tsx...")
        with open(f"{frontend_path}/Settings.tsx", "w") as f:
            f.write(generate_frontend_settings(workspace))
        
        print("  - Generating page components...")
        for page in config["pages"]:
            if page not in ["Dashboard", "Settings", "Logout"]:
                page_filename = page.lower().replace(/ /g, "-")
                with open(f"{frontend_path}/{pageFilename}.tsx".replace("PageFilename", page.replace(" ", "")), "w") as f:
                    f.write(generate_frontend_component(page, workspace))
        
        print(f"  ✓ Completed {workspace}")
    
    print("\n" + "=" * 50)
    print("Generation complete!")

if __name__ == "__main__":
    main()
