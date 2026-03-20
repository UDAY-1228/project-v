import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from '../core/frontend/pages/Login';
import SuperAdminDashboard from '../super_admin/frontend/pages/Dashboard';
import CreateInstitution from '../super_admin/frontend/pages/CreateInstitution';
import AdminDashboard from '../admin/frontend/pages/Dashboard';
import CreateUser from '../admin/frontend/pages/CreateUser';

// Workspace Dashboards
import PrincipalDashboard from '../workspaces/principal/frontend/pages/Dashboard';
import AcademicDashboard from '../workspaces/academic_coordinator/frontend/pages/Dashboard';
import AdmissionOfficerDashboard from '../workspaces/admission_officer/frontend/pages/Dashboard';
import AdmissionsCounselorDashboard from '../workspaces/admissions_counselor/frontend/pages/Dashboard';
import CommonDashboard from '../workspaces/common/frontend/pages/Dashboard';
import TeamOwnerDashboard from '../workspaces/team_owner/frontend/pages/Dashboard';
import TransportCoordinatorDashboard from '../workspaces/transport_coordinator/frontend/pages/Dashboard';
import NoticeBoard from '../workspaces/transport_coordinator/frontend/pages/NoticeBoard';
import Analytics from '../workspaces/transport_coordinator/frontend/pages/Analytics';
import Registrations from '../workspaces/transport_coordinator/frontend/pages/Registrations';
import Buses from '../workspaces/transport_coordinator/frontend/pages/Buses';
import BoardingPoints from '../workspaces/transport_coordinator/frontend/pages/BoardingPoints';
import TransportRoutes from '../workspaces/transport_coordinator/frontend/pages/Routes';
import RouteBusAssignment from '../workspaces/transport_coordinator/frontend/pages/RouteBusAssignment';
import Configuration from '../workspaces/transport_coordinator/frontend/pages/Configuration';
import TransportRoute from '../workspaces/transport_coordinator/frontend/pages/TransportRoute';

// Academic Coordinator Pages
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

import EmployeeDashboard from '../workspaces/employee/frontend/pages/Dashboard';
import HostelAdminDashboard from '../workspaces/hostel_admin/frontend/pages/Dashboard';
import PaymentAdministratorDashboard from '../workspaces/payment_administrator/frontend/pages/Dashboard';
import FacultyDashboard from '../workspaces/faculty/frontend/pages/Dashboard';
import StudentDashboard from '../workspaces/student/frontend/pages/Dashboard';

import PrincipalNoticeBoard from '../workspaces/principal/frontend/pages/NoticeBoard';
import AdmissionOfficerNoticeBoard from '../workspaces/admission_officer/frontend/pages/NoticeBoard';
import AdmissionsCounselorNoticeBoard from '../workspaces/admissions_counselor/frontend/pages/NoticeBoard';
import CommonNoticeBoard from '../workspaces/common/frontend/pages/NoticeBoard';
import TeamOwnerNoticeBoard from '../workspaces/team_owner/frontend/pages/NoticeBoard';
import EmployeeNoticeBoard from '../workspaces/employee/frontend/pages/NoticeBoard';
import HostelAdminNoticeBoard from '../workspaces/hostel_admin/frontend/pages/NoticeBoard';
import PaymentAdministratorNoticeBoard from '../workspaces/payment_administrator/frontend/pages/NoticeBoard';
import FacultyNoticeBoard from '../workspaces/faculty/frontend/pages/NoticeBoard';
import StudentNoticeBoard from '../workspaces/student/frontend/pages/NoticeBoard';

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
        <Route path="/admin/users" element={<AdminDashboard />} /> {/* Simple list placeholder */}
        
        {/* Workspace Routes */}
        <Route path="/principal/dashboard" element={<PrincipalDashboard />} />
        <Route path="/principal/notice-board" element={<PrincipalNoticeBoard />} />
        
        {/* Academic Coordinator Routes */}
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

        <Route path="/admission-officer/dashboard" element={<AdmissionOfficerDashboard />} />
        <Route path="/admission-officer/notice-board" element={<AdmissionOfficerNoticeBoard />} />
        <Route path="/admissions-counselor/dashboard" element={<AdmissionsCounselorDashboard />} />
        <Route path="/admissions-counselor/notice-board" element={<AdmissionsCounselorNoticeBoard />} />
        <Route path="/common/dashboard" element={<CommonDashboard />} />
        <Route path="/common/notice-board" element={<CommonNoticeBoard />} />
        <Route path="/team-owner/dashboard" element={<TeamOwnerDashboard />} />
        <Route path="/team-owner/notice-board" element={<TeamOwnerNoticeBoard />} />
        <Route path="/transport-coordinator/dashboard" element={<TransportCoordinatorDashboard />} />
        <Route path="/transport-coordinator/notice-board" element={<NoticeBoard />} />
        <Route path="/transport-coordinator/analytics" element={<Analytics />} />
        <Route path="/transport-coordinator/registrations" element={<Registrations />} />
        <Route path="/transport-coordinator/buses" element={<Buses />} />
        <Route path="/transport-coordinator/boarding" element={<BoardingPoints />} />
        <Route path="/transport-coordinator/routes" element={<TransportRoutes />} />
        <Route path="/transport-coordinator/assignment" element={<RouteBusAssignment />} />
        <Route path="/transport-coordinator/config" element={<Configuration />} />
        <Route path="/transport-coordinator/transport-route" element={<TransportRoute />} />
        <Route path="/employee/dashboard" element={<EmployeeDashboard />} />
        <Route path="/employee/notice-board" element={<EmployeeNoticeBoard />} />
        <Route path="/hostel-admin/dashboard" element={<HostelAdminDashboard />} />
        <Route path="/hostel-admin/notice-board" element={<HostelAdminNoticeBoard />} />
        <Route path="/payment-administrator/dashboard" element={<PaymentAdministratorDashboard />} />
        <Route path="/payment-administrator/notice-board" element={<PaymentAdministratorNoticeBoard />} />
        <Route path="/faculty/dashboard" element={<FacultyDashboard />} />
        <Route path="/faculty/notice-board" element={<FacultyNoticeBoard />} />
        <Route path="/student/dashboard" element={<StudentDashboard />} />
        <Route path="/student/notice-board" element={<StudentNoticeBoard />} />
        
        {/* Fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
};

export default App;
