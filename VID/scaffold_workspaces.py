import os
import json
import re

BASE_DIR = "/Users/nivas/Documents/React apps/v/project-v/VID"

WORKSPACES = {
    "faculty": {
        "features": ["Digital Notice Board", "Activities", "My Courses", "Class Timetable", "My Mentees", "Question Banks", "My Profile", "Research Scholar", "LMS"],
        "pages": {
            "Activities": "event",
            "MyCourses": "menu_book",
            "ClassTimetable": "calendar_month",
            "MyMentees": "groups",
            "QuestionBanks": "quiz",
            "MyProfile": "person",
            "ResearchScholar": "science",
            "Lms": "laptop_chromebook",
        }
    },
    "admission_officer": {
        "features": ["Digital Notice Board", "Prospects", "Applications", "Admissions", "Configuration"],
        "pages": {
            "Prospects": "person_search",
            "Applications": "assignment",
            "Admissions": "how_to_reg",
            "Configuration": "settings",
        }
    },
    "common": {
        "features": ["Digital Notice Board", "Home", "Student Central", "My Requests", "Payments", "Examination", "HRMS", "Configuration", "User Management System"],
        "pages": {
            "Home": "home",
            "StudentCentral": "hub",
            "MyRequests": "receipt_long",
            "Payments": "payments",
            "Examination": "grading",
            "Hrms": "badge",
            "Configuration": "settings",
            "UserManagementSystem": "manage_accounts",
        }
    },
    "team_owner": {
        "features": ["Digital Notice Board", "Institutions", "Organization Settings", "User Management", "Apps", "Data Management"],
        "pages": {
            "Institutions": "business",
            "OrganizationSettings": "settings_suggest",
            "UserManagement": "manage_accounts",
            "Apps": "apps",
            "DataManagement": "storage",
        }
    },
    "course_coordinator": {
        "features": ["Digital Notice Board", "All Courses"],
        "pages": {
            "AllCourses": "library_books",
        }
    },
    "employee": {
        "features": ["Digital Notice Board", "Home", "Leaves", "Attendance", "Salary", "Expenses", "Shift Requests", "Compensatory Leave"],
        "pages": {
            "Home": "home",
            "Leaves": "time_to_leave",
            "Attendance": "how_to_reg",
            "Salary": "account_balance_wallet",
            "Expenses": "receipt",
            "ShiftRequests": "schedule",
            "CompensatoryLeave": "event_available",
        }
    },
    "hostel_admin": {
        "features": ["Digital Notice Board", "Dashboard", "Hostels", "Attendance", "Gate Pass", "Requests", "Reports", "Configuration"],
        "pages": {
            "Hostels": "apartment",
            "Attendance": "how_to_reg",
            "GatePass": "directions_run",
            "Requests": "question_answer",
            "Reports": "analytics",
            "Configuration": "settings",
        }
    },
    "payment_administrator": {
        "features": ["Digital Notice Board", "Dashboard", "Academic Fees", "Student Permissions", "Exam Fee Restrictions", "Examination Fees", "Open Payments", "Configuration", "Reports", "Concessions", "Online Transactions", "Challans", "Statements", "Scholarships", "Credit Memos", "Student Fee Card", "Transaction Card"],
        "pages": {
            "AcademicFees": "school",
            "StudentPermissions": "verified_user",
            "ExamFeeRestrictions": "gavel",
            "ExaminationFees": "grading",
            "OpenPayments": "account_balance",
            "Configuration": "settings",
            "Reports": "analytics",
            "Concessions": "discount",
            "OnlineTransactions": "payment",
            "Challans": "receipt",
            "Statements": "description",
            "Scholarships": "military_tech",
            "CreditMemos": "credit_card",
            "StudentFeeCard": "account_box",
            "TransactionCard": "credit_score",
        }
    },
    "student": {
        "features": ["Digital Notice Board", "Dashboard", "Attendance", "Chatbot", "Teacher Communications", "Fees", "Examinations", "Co-curricular Activities", "Learning Management", "Course Tracking", "Profile", "Payment History"],
        "pages": {
            "Attendance": "how_to_reg",
            "Chatbot": "smart_toy",
            "TeacherCommunications": "forum",
            "Fees": "payments",
            "Examinations": "grading",
            "CoCurricularActivities": "rowing",
            "LearningManagement": "laptop_chromebook",
            "CourseTracking": "trending_up",
            "Profile": "person",
            "PaymentHistory": "history",
        }
    },
    "examination": {
        "features": ["Digital Notice Board", "Results", "Previous Exams", "Tests", "Previous Year Papers", "Averages", "Class Toppers", "Reports"],
        "pages": {
            "Results": "score",
            "PreviousExams": "history",
            "Tests": "quiz",
            "PreviousYearPapers": "library_books",
            "Averages": "functions",
            "ClassToppers": "emoji_events",
            "Reports": "analytics",
        }
    },
    "sports_officer": {
        "features": ["Digital Notice Board", "Dashboard", "Sports Events", "Team Management", "Player Registrations", "Practice Schedules", "Tournament Management", "Performance Tracking", "Reports"],
        "pages": {
            "SportsEvents": "emoji_events",
            "TeamManagement": "groups",
            "PlayerRegistrations": "how_to_reg",
            "PracticeSchedules": "schedule",
            "TournamentManagement": "emoji_events",
            "PerformanceTracking": "trending_up",
            "Reports": "analytics",
        }
    },
    "sports_and_co_curricular": {
        "features": ["Digital Notice Board", "Activities List", "Event Calendar", "Student Participation", "Achievements", "Certificates", "Clubs Management", "Announcements"],
        "pages": {
            "ActivitiesList": "list_alt",
            "EventCalendar": "event",
            "StudentParticipation": "groups",
            "Achievements": "emoji_events",
            "Certificates": "workspace_premium",
            "ClubsManagement": "category",
            "Announcements": "campaign",
        }
    }
}

TEMPLATE_COMPONENT = """import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const {component_name}: React.FC = () => {{
    const sidebarItems = [
{sidebar_items}
    ];

    return (
        <Layout sidebarItems={{sidebarItems}}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize">{human_readable_name}</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage and oversee operational activities</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Total Records" value="1,240" icon="groups" color="indigo" />
                    <Card title="Active Status" value="94.2%" icon="check_circle" color="green" />
                    <Card title="Pending Review" value="34" icon="pending" color="yellow" />
                    <Card title="System Alerts" value="2" icon="error_outline" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        {human_readable_name} Data Interface
                    </h3>
                    <div className="flex items-center justify-center p-20 bg-slate-50 border-2 border-dashed border-slate-200 rounded-[2.5rem]">
                        <p className="text-slate-400 font-bold uppercase tracking-widest text-xs">Module Implementation Area</p>
                    </div>
                </div>
            </div>
        </Layout>
    );
}};

export default {component_name};
"""

TEMPLATE_NOTICE_BOARD = """import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {{
    const sidebarItems = [
{sidebar_items}
    ];

    return <SharedNoticeBoard sidebarItems={{sidebarItems}} />;
}};

export default NoticeBoard;
"""

TEMPLATE_ROUTES_PY = """from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from core.backend.auth.security import get_current_user, TokenData
from ..services.logic import get_data, create_item

router = APIRouter(tags=["{workspace_title}"])

{endpoints}
"""

TEMPLATE_LOGIC_PY = """import os
import json
from typing import List, Dict, Any
from core.backend.database.connection import db

DATABASE_JSON = os.path.join(os.path.dirname(__file__), "..", "..", "database", "database.json")

async def get_data(collection_name: str, institution_id: str):
    try:
        cursor = db[collection_name].find({{"institution_id": institution_id}})
        data = await cursor.to_list(length=100)
        if data:
            return data
    except Exception:
        pass

    try:
        with open(DATABASE_JSON, 'r') as f:
            data = json.load(f)
            return data.get(collection_name, [])
    except Exception as e:
        return []

async def create_item(collection_name: str, item_data: Dict[str, Any]):
    try:
        result = await db[collection_name].insert_one(item_data)
        return str(result.inserted_id)
    except Exception:
        return "mock_id_123"
"""

TEMPLATE_APP_TSX_ROUTE = """        <Route path="/{url_path}/{page_path}" element={{<{component_name} />}} />"""
TEMPLATE_APP_TSX_IMPORT = """import {component_name} from '../workspaces/{workspace_id}/frontend/pages/{file_name}';"""

def generate_sidebar_items(workspace_id, pages):
    url_path = workspace_id.replace('_', '-')
    items = [f'        {{ "label": "Digital Notice Board", "icon": "announcement", "path": "/{url_path}/notice-board" }}']
    
    # Add Dashboard if it's implicitly part of human workflows or if pages aren't just dashboard
    items.append(f'        {{ "label": "Dashboard", "icon": "dashboard", "path": "/{url_path}/dashboard" }}')
    
    for page_name, icon in pages.items():
        if page_name != "Dashboard":
            label = re.sub(r'(?<!^)(?=[A-Z])', ' ', page_name)
            path_name = re.sub(r'(?<!^)(?=[A-Z])', '-', page_name).lower()
            items.append(f'        {{ "label": "{label}", "icon": "{icon}", "path": "/{url_path}/{path_name}" }}')
            
    return ",\n".join(items)

def run():
    app_tsx_imports = set()
    app_tsx_routes = []

    for ws_id, data in WORKSPACES.items():
        url_path = ws_id.replace('_', '-')
        ws_title = ws_id.replace('_', ' ').title()
        
        ws_dir = os.path.join(BASE_DIR, "workspaces", ws_id)
        os.makedirs(os.path.join(ws_dir, "frontend", "pages"), exist_ok=True)
        os.makedirs(os.path.join(ws_dir, "backend", "api"), exist_ok=True)
        os.makedirs(os.path.join(ws_dir, "backend", "services"), exist_ok=True)
        os.makedirs(os.path.join(ws_dir, "database"), exist_ok=True)
        
        sidebar_items = generate_sidebar_items(ws_id, data["pages"])
        
        # Write Dashboard
        dash_code = TEMPLATE_COMPONENT.format(
            component_name="Dashboard",
            sidebar_items=sidebar_items,
            human_readable_name=f"{ws_title} Dashboard"
        )
        with open(os.path.join(ws_dir, "frontend", "pages", "Dashboard.tsx"), "w") as f:
            f.write(dash_code)
            
        # Dash Imports/Routes
        comp_prefix = ws_id.replace('_', ' ').title().replace(' ', '')
        app_tsx_imports.add(TEMPLATE_APP_TSX_IMPORT.format(component_name=f"{comp_prefix}Dashboard", workspace_id=ws_id, file_name="Dashboard"))
        app_tsx_routes.append(TEMPLATE_APP_TSX_ROUTE.format(url_path=url_path, page_path="dashboard", component_name=f"{comp_prefix}Dashboard"))
        
        # Write Notice Board
        nb_code = TEMPLATE_NOTICE_BOARD.format(sidebar_items=sidebar_items)
        with open(os.path.join(ws_dir, "frontend", "pages", "NoticeBoard.tsx"), "w") as f:
            f.write(nb_code)
        
        app_tsx_imports.add(TEMPLATE_APP_TSX_IMPORT.format(component_name=f"{comp_prefix}NoticeBoard", workspace_id=ws_id, file_name="NoticeBoard"))
        app_tsx_routes.append(TEMPLATE_APP_TSX_ROUTE.format(url_path=url_path, page_path="notice-board", component_name=f"{comp_prefix}NoticeBoard"))

        
        endpoints = []
        for page_name, icon in data["pages"].items():
            if page_name == "Dashboard" or page_name == "NoticeBoard":
                continue
                
            label = re.sub(r'(?<!^)(?=[A-Z])', ' ', page_name)
            path_name = re.sub(r'(?<!^)(?=[A-Z])', '-', page_name).lower()
            
            # Write Component
            page_code = TEMPLATE_COMPONENT.format(
                component_name=page_name,
                sidebar_items=sidebar_items,
                human_readable_name=label
            )
            with open(os.path.join(ws_dir, "frontend", "pages", f"{page_name}.tsx"), "w") as f:
                f.write(page_code)
                
            # React Routing
            page_comp_name = f"{comp_prefix}{page_name}"
            app_tsx_imports.add(TEMPLATE_APP_TSX_IMPORT.format(component_name=page_comp_name, workspace_id=ws_id, file_name=page_name))
            app_tsx_routes.append(TEMPLATE_APP_TSX_ROUTE.format(url_path=url_path, page_path=path_name, component_name=page_comp_name))
            
            # Endpoints
            safe_page_name = path_name.replace('-', '_')
            endpoints.append(f"@router.get('/{path_name}')\nasync def get_{safe_page_name}(current_user: TokenData = Depends(get_current_user)):\n    return await get_data('{safe_page_name}', current_user.institution_id)\n")

        # Write Logic
        with open(os.path.join(ws_dir, "backend", "services", "logic.py"), "w") as f:
            f.write(TEMPLATE_LOGIC_PY)
            
        # Write Routes
        with open(os.path.join(ws_dir, "backend", "api", "routes.py"), "w") as f:
            f.write(TEMPLATE_ROUTES_PY.format(workspace_title=ws_title, endpoints="\n".join(endpoints)))

        # Empty Database Json
        with open(os.path.join(ws_dir, "database", "database.json"), "w") as f:
            f.write("{}")

    # Now let's update App.tsx completely. 
    # Because there are so many routes, we will just regenerate the App.tsx
    # but strictly around standard paths to retain login and superadmin.
    
    app_tsx_content_1 = """import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from '../core/frontend/pages/Login';
import SuperAdminDashboard from '../super_admin/frontend/pages/Dashboard';
import CreateInstitution from '../super_admin/frontend/pages/CreateInstitution';
import AdminDashboard from '../admin/frontend/pages/Dashboard';
import CreateUser from '../admin/frontend/pages/CreateUser';

// Generated Workspace Imports
"""
    app_tsx_content_2 = (chr(10)).join(sorted(list(app_tsx_imports))) + """

import PrincipalDashboard from '../workspaces/principal/frontend/pages/Dashboard';
import PrincipalNoticeBoard from '../workspaces/principal/frontend/pages/NoticeBoard';
import AcademicDashboard from '../workspaces/academic_coordinator/frontend/pages/Dashboard';
import AcademicNoticeBoard from '../workspaces/academic_coordinator/frontend/pages/NoticeBoard';
import AcademicActivities from '../workspaces/academic_coordinator/frontend/pages/Activities';
import AcademicPrincipalDashboard from '../workspaces/academic_coordinator/frontend/pages/PrincipalDashboard';
import Academics from '../workspaces/academic_coordinator/frontend/pages/Academics';
import AcademicSetup from '../workspaces/academic_coordinator/frontend/pages/AcademicSetup';
import AcademicCourses from '../workspaces/academic_coordinator/frontend/pages/Courses';
import MasterCourses from '../workspaces/academic_coordinator/frontend/pages/MasterCourses';
import AcademicAssessment from '../workspaces/academic_coordinator/frontend/pages/Assessment';
import DataManagement from '../workspaces/academic_coordinator/frontend/pages/DataManagement';
import AcademicConfigurations from '../workspaces/academic_coordinator/frontend/pages/Configurations';

import TransportCoordinatorDashboard from '../workspaces/transport_coordinator/frontend/pages/Dashboard';
import TransportCoordinatorNoticeBoard from '../workspaces/transport_coordinator/frontend/pages/NoticeBoard';
import TransportCoordinatorAnalytics from '../workspaces/transport_coordinator/frontend/pages/Analytics';
import TransportCoordinatorRegistrations from '../workspaces/transport_coordinator/frontend/pages/Registrations';
import TransportCoordinatorBuses from '../workspaces/transport_coordinator/frontend/pages/Buses';
import TransportCoordinatorBoardingPoints from '../workspaces/transport_coordinator/frontend/pages/BoardingPoints';
import TransportCoordinatorRoutes from '../workspaces/transport_coordinator/frontend/pages/Routes';
import RouteBusAssignment from '../workspaces/transport_coordinator/frontend/pages/RouteBusAssignment';
import TransportCoordinatorConfiguration from '../workspaces/transport_coordinator/frontend/pages/Configuration';
import TransportRoute from '../workspaces/transport_coordinator/frontend/pages/TransportRoute';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        
        {/* Super Admin Routes */}
        <Route path="/super-admin/dashboard" element={<SuperAdminDashboard />} />
        <Route path="/super-admin/institutions" element={<CreateInstitution />} />
        
        {/* Institutional Admin Routes */}
        <Route path="/admin/dashboard" element={<AdminDashboard />} /> 
        <Route path="/admin/create-user" element={<CreateUser />} />
        <Route path="/admin/users" element={<AdminDashboard />} />
        
        {/* Legacy Pre-existing specific routes */}
        <Route path="/principal/dashboard" element={<PrincipalDashboard />} />
        <Route path="/principal/notice-board" element={<PrincipalNoticeBoard />} />
        
        <Route path="/academic-coordinator/dashboard" element={<AcademicDashboard />} />
        <Route path="/academic-coordinator/notice-board" element={<AcademicNoticeBoard />} />
        <Route path="/academic-coordinator/activities" element={<AcademicActivities />} />
        <Route path="/academic-coordinator/principal-dashboard" element={<AcademicPrincipalDashboard />} />
        <Route path="/academic-coordinator/academics" element={<Academics />} />
        <Route path="/academic-coordinator/setup" element={<AcademicSetup />} />
        <Route path="/academic-coordinator/courses" element={<AcademicCourses />} />
        <Route path="/academic-coordinator/master-courses" element={<MasterCourses />} />
        <Route path="/academic-coordinator/assessment" element={<AcademicAssessment />} />
        <Route path="/academic-coordinator/data-management" element={<DataManagement />} />
        <Route path="/academic-coordinator/config" element={<AcademicConfigurations />} />
        
        <Route path="/transport-coordinator/dashboard" element={<TransportCoordinatorDashboard />} />
        <Route path="/transport-coordinator/notice-board" element={<TransportCoordinatorNoticeBoard />} />
        <Route path="/transport-coordinator/analytics" element={<TransportCoordinatorAnalytics />} />
        <Route path="/transport-coordinator/registrations" element={<TransportCoordinatorRegistrations />} />
        <Route path="/transport-coordinator/buses" element={<TransportCoordinatorBuses />} />
        <Route path="/transport-coordinator/boarding" element={<TransportCoordinatorBoardingPoints />} />
        <Route path="/transport-coordinator/routes" element={<TransportCoordinatorRoutes />} />
        <Route path="/transport-coordinator/assignment" element={<RouteBusAssignment />} />
        <Route path="/transport-coordinator/config" element={<TransportCoordinatorConfiguration />} />
        <Route path="/transport-coordinator/transport-route" element={<TransportRoute />} />

        {/* Generated Routes */}
"""
    app_tsx_content_3 = (chr(10)).join(app_tsx_routes) + """
        
        {/* Fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
};

export default App;
"""
    app_tsx_content = app_tsx_content_1 + app_tsx_content_2 + app_tsx_content_3

    with open(os.path.join(BASE_DIR, "src", "App.tsx"), "w") as f:
        f.write(app_tsx_content)

    print("Generation complete!")

if __name__ == "__main__":
    run()
