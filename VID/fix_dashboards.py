import os
import json

workspaces_features = {
    "principal": [
        {"label": "Digital Notice Board", "icon": "announcement", "path": "/principal/notice-board"},
        {"label": "Activities", "icon": "event", "path": "/principal/activities"},
        {"label": "Principal Dashboard", "icon": "dashboard", "path": "/principal/dashboard"},
        {"label": "Academics", "icon": "school", "path": "/principal/academics"},
        {"label": "Data Management", "icon": "storage", "path": "/principal/data"},
        {"label": "Configurations", "icon": "settings", "path": "/principal/config"}
    ],
    "academic_coordinator": [
        {"label": "Digital Notice Board", "icon": "announcement", "path": "/academic-coordinator/notice-board"},
        {"label": "Activities", "icon": "event", "path": "/academic-coordinator/activities"},
        {"label": "Course Registrations", "icon": "how_to_reg", "path": "/academic-coordinator/registrations"},
        {"label": "Student Promotions", "icon": "trending_up", "path": "/academic-coordinator/promotions"},
        {"label": "All Students", "icon": "groups", "path": "/academic-coordinator/students"},
        {"label": "Question Banks", "icon": "quiz", "path": "/academic-coordinator/questions"},
        {"label": "Courses", "icon": "menu_book", "path": "/academic_coordinator/courses"},
        {"label": "Attendance", "icon": "check_circle", "path": "/academic_coordinator/attendance"},
        {"label": "Classrooms", "icon": "meeting_room", "path": "/academic_coordinator/classrooms"},
        {"label": "Reports", "icon": "analytics", "path": "/academic_coordinator/reports"},
        {"label": "Faculty Timetable", "icon": "event_note", "path": "/academic_coordinator/timetable"}
    ],
    "admission_officer": [
        {"label": "Prospects", "icon": "person_search", "path": "/admission-officer/prospects"},
        {"label": "Applications", "icon": "assignment", "path": "/admission-officer/applications"},
        {"label": "Admissions", "icon": "how_to_reg", "path": "/admission-officer/admissions"}
    ],
    "admissions_counselor": [
        {"label": "Prospects", "icon": "person_search", "path": "/admissions-counselor/prospects"},
        {"label": "Applications", "icon": "assignment", "path": "/admissions-counselor/applications"},
        {"label": "Admissions", "icon": "how_to_reg", "path": "/admissions-counselor/admissions"},
        {"label": "Configurations", "icon": "settings", "path": "/admissions-counselor/config"}
    ],
    "common": [
        {"label": "Home", "icon": "home", "path": "/common/home"},
        {"label": "Student Central", "icon": "school", "path": "/common/student-central"},
        {"label": "My Requests", "icon": "rate_review", "path": "/common/requests"},
        {"label": "Payments", "icon": "payments", "path": "/common/payments"},
        {"label": "Exams", "icon": "assessment", "path": "/common/exams"},
        {"label": "HRMS", "icon": "badge", "path": "/common/hrms"},
        {"label": "Configurations", "icon": "settings", "path": "/common/config"}
    ],
    "team_owner": [
        {"label": "Institutions", "icon": "business", "path": "/team-owner/institutions"},
        {"label": "Organization Settings", "icon": "admin_panel_settings", "path": "/team-owner/settings"},
        {"label": "User Management", "icon": "manage_accounts", "path": "/team-owner/users"},
        {"label": "Apps Data Management", "icon": "apps", "path": "/team-owner/apps"},
        {"label": "Course Coordinator", "icon": "coordinator", "path": "/team-owner/coordinator"},
        {"label": "Digital Notice Board", "icon": "announcement", "path": "/team-owner/notice-board"},
        {"label": "All Courses", "icon": "menu_book", "path": "/team-owner/courses"}
    ],
    "transport_coordinator": [
        {"label": "Digital Notice Board", "icon": "announcement", "path": "/transport-coordinator/notice-board"},
        {"label": "Transport Analytics", "icon": "bar_chart", "path": "/transport-coordinator/analytics"},
        {"label": "Transport Registrations", "icon": "app_registration", "path": "/transport-coordinator/registrations"},
        {"label": "Buses", "icon": "directions_bus", "path": "/transport-coordinator/buses"},
        {"label": "Boarding Points", "icon": "place", "path": "/transport-coordinator/boarding"},
        {"label": "Routes", "icon": "map", "path": "/transport-coordinator/routes"},
        {"label": "Route Bus Assignment", "icon": "assignment", "path": "/transport-coordinator/assignment"},
        {"label": "Configuration", "icon": "settings", "path": "/transport-coordinator/config"}
    ],
    "employee": [
        {"label": "Home", "icon": "home", "path": "/employee/home"},
        {"label": "Leaves", "icon": "holiday_village", "path": "/employee/leaves"},
        {"label": "Attendance", "icon": "check_circle", "path": "/employee/attendance"},
        {"label": "Salary", "icon": "account_balance_wallet", "path": "/employee/salary"},
        {"label": "Expenses", "icon": "receipt_long", "path": "/employee/expenses"},
        {"label": "Shift Requests", "icon": "schedule", "path": "/employee/shifts"},
        {"label": "Compensatory Leave", "icon": "event_available", "path": "/employee/comp-leave"}
    ],
    "hostel_admin": [
        {"label": "Dashboard", "icon": "dashboard", "path": "/hostel-admin/dashboard"},
        {"label": "Hostelers", "icon": "hotel", "path": "/hostel-admin/hostelers"},
        {"label": "Attendance", "icon": "check_circle", "path": "/hostel-admin/attendance"},
        {"label": "Gate Pass Requests", "icon": "key", "path": "/hostel-admin/gatepass"},
        {"label": "Reports", "icon": "analytics", "path": "/hostel-admin/reports"},
        {"label": "Configuration", "icon": "settings", "path": "/hostel-admin/config"}
    ],
    "payment_administrator": [
        {"label": "Dashboard", "icon": "dashboard", "path": "/payment-administrator/dashboard"},
        {"label": "Student Permissions", "icon": "security", "path": "/payment-administrator/permissions"},
        {"label": "Academic Fees", "icon": "school", "path": "/payment-administrator/academic-fees"},
        {"label": "Exam Fees", "icon": "assessment", "path": "/payment-administrator/exam-fees"},
        {"label": "Restrictions", "icon": "block", "path": "/payment-administrator/restrictions"},
        {"label": "Open Payments", "icon": "credit_card", "path": "/payment-administrator/open-payments"},
        {"label": "Reports", "icon": "analytics", "path": "/payment-administrator/reports"},
        {"label": "Configuration", "icon": "settings", "path": "/payment-administrator/config"},
        {"label": "Concessions", "icon": "money_off", "path": "/payment-administrator/concessions"},
        {"label": "Online Transactions", "icon": "online_prediction", "path": "/payment-administrator/online"},
        {"label": "Challans", "icon": "receipt", "path": "/payment-administrator/challans"},
        {"label": "Statements", "icon": "account_balance", "path": "/payment-administrator/statements"},
        {"label": "Scholarships", "icon": "card_membership", "path": "/payment-administrator/scholarships"},
        {"label": "Credit Memos", "icon": "note_add", "path": "/payment-administrator/credits"},
        {"label": "Fee Card", "icon": "credit_card", "path": "/payment-administrator/feecard"}
    ],
    "faculty": [
        {"label": "Notice Board", "icon": "announcement", "path": "/faculty/notice-board"},
        {"label": "Activities", "icon": "event", "path": "/faculty/activities"},
        {"label": "Discussion", "icon": "forum", "path": "/faculty/discussion"},
        {"label": "Calendar", "icon": "calendar_month", "path": "/faculty/calendar"},
        {"label": "My Courses", "icon": "class", "path": "/faculty/courses"},
        {"label": "Timetable", "icon": "schedule", "path": "/faculty/timetable"},
        {"label": "LMS Classroom", "icon": "laptop", "path": "/faculty/lms"},
        {"label": "Assessments", "icon": "quiz", "path": "/faculty/assessments"},
        {"label": "Assignments", "icon": "assignment", "path": "/faculty/assignments"},
        {"label": "Attendance", "icon": "task_alt", "path": "/faculty/attendance"},
        {"label": "Students", "icon": "groups", "path": "/faculty/students"},
        {"label": "My Mentees", "icon": "psychology", "path": "/faculty/mentees"},
        {"label": "Research", "icon": "science", "path": "/faculty/research"},
        {"label": "Profile", "icon": "person", "path": "/faculty/profile"},
        {"label": "Reports", "icon": "analytics", "path": "/faculty/reports"}
    ],
    "student": [
        {"label": "Notice Board", "icon": "announcement", "path": "/student/notice-board"},
        {"label": "My Attendance", "icon": "check_circle", "path": "/student/attendance"},
        {"label": "Events", "icon": "event", "path": "/student/events"},
        {"label": "LMS", "icon": "auto_stories", "path": "/student/lms"},
        {"label": "Exams", "icon": "assignment", "path": "/student/exams"},
        {"label": "Assessments", "icon": "quiz", "path": "/student/assessments"},
        {"label": "Question Bank", "icon": "menu_book", "path": "/student/questions"},
        {"label": "Fee Payments", "icon": "payments", "path": "/student/payments"},
        {"label": "My Profile", "icon": "person", "path": "/student/profile"},
        {"label": "Calendar", "icon": "calendar_month", "path": "/student/calendar"}
    ]
}

base_dir = "/Users/nivas/Documents/React apps/VID/workspaces"

dashboard_template = """import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Dashboard: React.FC = () => {
    const sidebarItems = %SIDEBAR_ITEMS%;

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize">%WORKSPACE_NAME% Dashboard</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Welcome to the VID Portal</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Notifications" value="12" icon="announcement" color="blue" />
                    <Card title="Completed Tasks" value="85%" icon="task_alt" color="green" />
                    <Card title="Pending Review" value="5" icon="pending" color="yellow" />
                    <Card title="System Health" value="Stable" icon="health_and_safety" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Overview & Features
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {sidebarItems.map((item, idx) => (
                            <a 
                                key={idx} 
                                href={item.path}
                                className="group flex items-center gap-6 p-8 bg-slate-50/50 rounded-3xl border border-slate-100 hover:border-indigo-400 hover:bg-white hover:shadow-xl transition-all duration-300"
                            >
                                <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-indigo-500 group-hover:bg-indigo-500 group-hover:text-white transition-all">
                                    <span className="material-icons text-2xl group-hover:scale-110 transition-transform">{item.icon}</span>
                                </div>
                                <div>
                                    <p className="font-extrabold text-slate-800 tracking-tight group-hover:text-indigo-600 transition-colors">{item.label}</p>
                                    <p className="text-[11px] font-bold text-slate-400 uppercase tracking-widest mt-1">Access Module</p>
                                </div>
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Dashboard;
"""

for ws, items in workspaces_features.items():
    ws_path = os.path.join(base_dir, ws)
    os.makedirs(os.path.join(ws_path, "frontend/pages"), exist_ok=True)
    
    formatted_items = json.dumps(items, indent=4)
    ws_name_display = ws.replace("_", " ")
    
    content = dashboard_template.replace("%SIDEBAR_ITEMS%", formatted_items).replace("%WORKSPACE_NAME%", ws_name_display)
    
    with open(os.path.join(ws_path, "frontend/pages/Dashboard.tsx"), "w") as f:
        f.write(content)

print("Successfully updated all dashboards to VID branding.")
