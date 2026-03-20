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
import EmployeeDashboard from '../workspaces/employee/frontend/pages/Dashboard';
import HostelAdminDashboard from '../workspaces/hostel_admin/frontend/pages/Dashboard';
import PaymentAdministratorDashboard from '../workspaces/payment_administrator/frontend/pages/Dashboard';
import FacultyDashboard from '../workspaces/faculty/frontend/pages/Dashboard';
import StudentDashboard from '../workspaces/student/frontend/pages/Dashboard';

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
        <Route path="/academic-coordinator/dashboard" element={<AcademicDashboard />} />
        <Route path="/admission-officer/dashboard" element={<AdmissionOfficerDashboard />} />
        <Route path="/admissions-counselor/dashboard" element={<AdmissionsCounselorDashboard />} />
        <Route path="/common/dashboard" element={<CommonDashboard />} />
        <Route path="/team-owner/dashboard" element={<TeamOwnerDashboard />} />
        <Route path="/transport-coordinator/dashboard" element={<TransportCoordinatorDashboard />} />
        <Route path="/employee/dashboard" element={<EmployeeDashboard />} />
        <Route path="/hostel-admin/dashboard" element={<HostelAdminDashboard />} />
        <Route path="/payment-administrator/dashboard" element={<PaymentAdministratorDashboard />} />
        <Route path="/faculty/dashboard" element={<FacultyDashboard />} />
        <Route path="/student/dashboard" element={<StudentDashboard />} />
        
        {/* Fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
};

export default App;
