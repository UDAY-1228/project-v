import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from '../core/frontend/pages/Home';
import Login from '../core/frontend/pages/Login';
import SuperAdminDashboard from '../super_admin/frontend/pages/Dashboard';
import CreateInstitution from '../super_admin/frontend/pages/CreateInstitution';
import AdminDashboard from '../admin/frontend/pages/Dashboard';
import CreateUser from '../admin/frontend/pages/CreateUser';

// Generated Workspace Imports
import AdmissionOfficerAdmissions from '../workspaces/admission_officer/frontend/pages/Admissions';
import AdmissionOfficerApplications from '../workspaces/admission_officer/frontend/pages/Applications';
import AdmissionOfficerConfiguration from '../workspaces/admission_officer/frontend/pages/Configuration';
import AdmissionOfficerDashboard from '../workspaces/admission_officer/frontend/pages/Dashboard';
import AdmissionOfficerNoticeBoard from '../workspaces/admission_officer/frontend/pages/NoticeBoard';
import AdmissionOfficerProspects from '../workspaces/admission_officer/frontend/pages/Prospects';
import CommonConfiguration from '../workspaces/common/frontend/pages/Configuration';
import CommonDashboard from '../workspaces/common/frontend/pages/Dashboard';
import CommonExamination from '../workspaces/common/frontend/pages/Examination';
import CommonHome from '../workspaces/common/frontend/pages/Home';
import CommonHrms from '../workspaces/common/frontend/pages/Hrms';
import CommonMyRequests from '../workspaces/common/frontend/pages/MyRequests';
import CommonNoticeBoard from '../workspaces/common/frontend/pages/NoticeBoard';
import CommonPayments from '../workspaces/common/frontend/pages/Payments';
import CommonStudentCentral from '../workspaces/common/frontend/pages/StudentCentral';
import CommonUserManagementSystem from '../workspaces/common/frontend/pages/UserManagementSystem';
import CourseCoordinatorAllCourses from '../workspaces/course_coordinator/frontend/pages/AllCourses';
import CourseCoordinatorDashboard from '../workspaces/course_coordinator/frontend/pages/Dashboard';
import CourseCoordinatorNoticeBoard from '../workspaces/course_coordinator/frontend/pages/NoticeBoard';
import EmployeeAttendance from '../workspaces/employee/frontend/pages/Attendance';
import EmployeeCompensatoryLeave from '../workspaces/employee/frontend/pages/CompensatoryLeave';
import EmployeeDashboard from '../workspaces/employee/frontend/pages/Dashboard';
import EmployeeExpenses from '../workspaces/employee/frontend/pages/Expenses';
import EmployeeHome from '../workspaces/employee/frontend/pages/Home';
import EmployeeLeaves from '../workspaces/employee/frontend/pages/Leaves';
import EmployeeNoticeBoard from '../workspaces/employee/frontend/pages/NoticeBoard';
import EmployeeSalary from '../workspaces/employee/frontend/pages/Salary';
import EmployeeShiftRequests from '../workspaces/employee/frontend/pages/ShiftRequests';
import ExaminationAverages from '../workspaces/examination/frontend/pages/Averages';
import ExaminationClassToppers from '../workspaces/examination/frontend/pages/ClassToppers';
import ExaminationDashboard from '../workspaces/examination/frontend/pages/Dashboard';
import ExaminationNoticeBoard from '../workspaces/examination/frontend/pages/NoticeBoard';
import ExaminationPreviousExams from '../workspaces/examination/frontend/pages/PreviousExams';
import ExaminationPreviousYearPapers from '../workspaces/examination/frontend/pages/PreviousYearPapers';
import ExaminationReports from '../workspaces/examination/frontend/pages/Reports';
import ExaminationResults from '../workspaces/examination/frontend/pages/Results';
import ExaminationTests from '../workspaces/examination/frontend/pages/Tests';
import FacultyActivities from '../workspaces/faculty/frontend/pages/Activities';
import FacultyClassTimetable from '../workspaces/faculty/frontend/pages/ClassTimetable';
import FacultyDashboard from '../workspaces/faculty/frontend/pages/Dashboard';
import FacultyLms from '../workspaces/faculty/frontend/pages/Lms';
import FacultyMyCourses from '../workspaces/faculty/frontend/pages/MyCourses';
import FacultyMyMentees from '../workspaces/faculty/frontend/pages/MyMentees';
import FacultyMyProfile from '../workspaces/faculty/frontend/pages/MyProfile';
import FacultyNoticeBoard from '../workspaces/faculty/frontend/pages/NoticeBoard';
import FacultyQuestionBanks from '../workspaces/faculty/frontend/pages/QuestionBanks';
import FacultyResearchScholar from '../workspaces/faculty/frontend/pages/ResearchScholar';
import HostelAdminAttendance from '../workspaces/hostel_admin/frontend/pages/Attendance';
import HostelAdminConfiguration from '../workspaces/hostel_admin/frontend/pages/Configuration';
import HostelAdminDashboard from '../workspaces/hostel_admin/frontend/pages/Dashboard';
import HostelAdminGatePass from '../workspaces/hostel_admin/frontend/pages/GatePass';
import HostelAdminHostels from '../workspaces/hostel_admin/frontend/pages/Hostels';
import HostelAdminNoticeBoard from '../workspaces/hostel_admin/frontend/pages/NoticeBoard';
import HostelAdminReports from '../workspaces/hostel_admin/frontend/pages/Reports';
import HostelAdminRequests from '../workspaces/hostel_admin/frontend/pages/Requests';
import PaymentAdministratorAcademicFees from '../workspaces/payment_administrator/frontend/pages/AcademicFees';
import PaymentAdministratorChallans from '../workspaces/payment_administrator/frontend/pages/Challans';
import PaymentAdministratorConcessions from '../workspaces/payment_administrator/frontend/pages/Concessions';
import PaymentAdministratorConfiguration from '../workspaces/payment_administrator/frontend/pages/Configuration';
import PaymentAdministratorCreditMemos from '../workspaces/payment_administrator/frontend/pages/CreditMemos';
import PaymentAdministratorDashboard from '../workspaces/payment_administrator/frontend/pages/Dashboard';
import PaymentAdministratorExamFeeRestrictions from '../workspaces/payment_administrator/frontend/pages/ExamFeeRestrictions';
import PaymentAdministratorExaminationFees from '../workspaces/payment_administrator/frontend/pages/ExaminationFees';
import PaymentAdministratorNoticeBoard from '../workspaces/payment_administrator/frontend/pages/NoticeBoard';
import PaymentAdministratorOnlineTransactions from '../workspaces/payment_administrator/frontend/pages/OnlineTransactions';
import PaymentAdministratorOpenPayments from '../workspaces/payment_administrator/frontend/pages/OpenPayments';
import PaymentAdministratorReports from '../workspaces/payment_administrator/frontend/pages/Reports';
import PaymentAdministratorScholarships from '../workspaces/payment_administrator/frontend/pages/Scholarships';
import PaymentAdministratorStatements from '../workspaces/payment_administrator/frontend/pages/Statements';
import PaymentAdministratorStudentFeeCard from '../workspaces/payment_administrator/frontend/pages/StudentFeeCard';
import PaymentAdministratorStudentPermissions from '../workspaces/payment_administrator/frontend/pages/StudentPermissions';
import PaymentAdministratorTransactionCard from '../workspaces/payment_administrator/frontend/pages/TransactionCard';
import SportsOfficerAchievements from '../workspaces/sports_officer/frontend/pages/Achievements';
import SportsOfficerActivitiesList from '../workspaces/sports_officer/frontend/pages/ActivitiesList';
import SportsOfficerAnnouncements from '../workspaces/sports_officer/frontend/pages/Announcements';
import SportsOfficerCertificates from '../workspaces/sports_officer/frontend/pages/Certificates';
import SportsOfficerClubsManagement from '../workspaces/sports_officer/frontend/pages/ClubsManagement';
import SportsOfficerEventCalendar from '../workspaces/sports_officer/frontend/pages/EventCalendar';
import SportsOfficerStudentParticipation from '../workspaces/sports_officer/frontend/pages/StudentParticipation';
import SportsOfficerDashboard from '../workspaces/sports_officer/frontend/pages/Dashboard';
import SportsOfficerNoticeBoard from '../workspaces/sports_officer/frontend/pages/NoticeBoard';
import SportsOfficerPerformanceTracking from '../workspaces/sports_officer/frontend/pages/PerformanceTracking';
import SportsOfficerPlayerRegistrations from '../workspaces/sports_officer/frontend/pages/PlayerRegistrations';
import SportsOfficerPracticeSchedules from '../workspaces/sports_officer/frontend/pages/PracticeSchedules';
import SportsOfficerReports from '../workspaces/sports_officer/frontend/pages/Reports';
import SportsOfficerSportsEvents from '../workspaces/sports_officer/frontend/pages/SportsEvents';
import SportsOfficerTeamManagement from '../workspaces/sports_officer/frontend/pages/TeamManagement';
import SportsOfficerTournamentManagement from '../workspaces/sports_officer/frontend/pages/TournamentManagement';
import StudentAttendance from '../workspaces/student/frontend/pages/Attendance';
import StudentChatbot from '../workspaces/student/frontend/pages/Chatbot';
import StudentCoCurricularActivities from '../workspaces/student/frontend/pages/CoCurricularActivities';
import StudentCourseTracking from '../workspaces/student/frontend/pages/CourseTracking';
import StudentDashboard from '../workspaces/student/frontend/pages/Dashboard';
import StudentExaminations from '../workspaces/student/frontend/pages/Examinations';
import StudentFees from '../workspaces/student/frontend/pages/Fees';
import StudentLearningManagement from '../workspaces/student/frontend/pages/LearningManagement';
import StudentNoticeBoard from '../workspaces/student/frontend/pages/NoticeBoard';
import StudentPaymentHistory from '../workspaces/student/frontend/pages/PaymentHistory';
import StudentProfile from '../workspaces/student/frontend/pages/Profile';
import StudentTeacherCommunications from '../workspaces/student/frontend/pages/TeacherCommunications';
import TeamOwnerApps from '../workspaces/team_owner/frontend/pages/Apps';
import TeamOwnerDashboard from '../workspaces/team_owner/frontend/pages/Dashboard';
import TeamOwnerDataManagement from '../workspaces/team_owner/frontend/pages/DataManagement';
import TeamOwnerInstitutions from '../workspaces/team_owner/frontend/pages/Institutions';
import TeamOwnerNoticeBoard from '../workspaces/team_owner/frontend/pages/NoticeBoard';
import TeamOwnerOrganizationSettings from '../workspaces/team_owner/frontend/pages/OrganizationSettings';
import TeamOwnerUserManagement from '../workspaces/team_owner/frontend/pages/UserManagement';


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
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        
        {/* Super Admin Routes */}
        <Route path="/super-admin/dashboard" element={<SuperAdminDashboard />} />
        <Route path="/super-admin/institutions" element={<CreateInstitution />} />
        
        {/* Institutional Admin Routes */}
        <Route path="/admin/dashboard" element={<AdminDashboard />} /> 
        <Route path="/admin/create-user" element={<CreateUser />} />
        <Route path="/admin/users" element={<AdminDashboard />} />
        
        {/* Legacy Pre-existing specific routes */}
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
        <Route path="/faculty/dashboard" element={<FacultyDashboard />} />
        <Route path="/faculty/notice-board" element={<FacultyNoticeBoard />} />
        <Route path="/faculty/activities" element={<FacultyActivities />} />
        <Route path="/faculty/my-courses" element={<FacultyMyCourses />} />
        <Route path="/faculty/class-timetable" element={<FacultyClassTimetable />} />
        <Route path="/faculty/my-mentees" element={<FacultyMyMentees />} />
        <Route path="/faculty/question-banks" element={<FacultyQuestionBanks />} />
        <Route path="/faculty/my-profile" element={<FacultyMyProfile />} />
        <Route path="/faculty/research-scholar" element={<FacultyResearchScholar />} />
        <Route path="/faculty/lms" element={<FacultyLms />} />
        <Route path="/admission-officer/dashboard" element={<AdmissionOfficerDashboard />} />
        <Route path="/admission-officer/notice-board" element={<AdmissionOfficerNoticeBoard />} />
        <Route path="/admission-officer/prospects" element={<AdmissionOfficerProspects />} />
        <Route path="/admission-officer/applications" element={<AdmissionOfficerApplications />} />
        <Route path="/admission-officer/admissions" element={<AdmissionOfficerAdmissions />} />
        <Route path="/admission-officer/configuration" element={<AdmissionOfficerConfiguration />} />
        <Route path="/common/dashboard" element={<CommonDashboard />} />
        <Route path="/common/notice-board" element={<CommonNoticeBoard />} />
        <Route path="/common/home" element={<CommonHome />} />
        <Route path="/common/student-central" element={<CommonStudentCentral />} />
        <Route path="/common/my-requests" element={<CommonMyRequests />} />
        <Route path="/common/payments" element={<CommonPayments />} />
        <Route path="/common/examination" element={<CommonExamination />} />
        <Route path="/common/hrms" element={<CommonHrms />} />
        <Route path="/common/configuration" element={<CommonConfiguration />} />
        <Route path="/common/user-management-system" element={<CommonUserManagementSystem />} />
        <Route path="/team-owner/dashboard" element={<TeamOwnerDashboard />} />
        <Route path="/team-owner/notice-board" element={<TeamOwnerNoticeBoard />} />
        <Route path="/team-owner/institutions" element={<TeamOwnerInstitutions />} />
        <Route path="/team-owner/organization-settings" element={<TeamOwnerOrganizationSettings />} />
        <Route path="/team-owner/user-management" element={<TeamOwnerUserManagement />} />
        <Route path="/team-owner/apps" element={<TeamOwnerApps />} />
        <Route path="/team-owner/data-management" element={<TeamOwnerDataManagement />} />
        <Route path="/course-coordinator/dashboard" element={<CourseCoordinatorDashboard />} />
        <Route path="/course-coordinator/notice-board" element={<CourseCoordinatorNoticeBoard />} />
        <Route path="/course-coordinator/all-courses" element={<CourseCoordinatorAllCourses />} />
        <Route path="/employee/dashboard" element={<EmployeeDashboard />} />
        <Route path="/employee/notice-board" element={<EmployeeNoticeBoard />} />
        <Route path="/employee/home" element={<EmployeeHome />} />
        <Route path="/employee/leaves" element={<EmployeeLeaves />} />
        <Route path="/employee/attendance" element={<EmployeeAttendance />} />
        <Route path="/employee/salary" element={<EmployeeSalary />} />
        <Route path="/employee/expenses" element={<EmployeeExpenses />} />
        <Route path="/employee/shift-requests" element={<EmployeeShiftRequests />} />
        <Route path="/employee/compensatory-leave" element={<EmployeeCompensatoryLeave />} />
        <Route path="/hostel-admin/dashboard" element={<HostelAdminDashboard />} />
        <Route path="/hostel-admin/notice-board" element={<HostelAdminNoticeBoard />} />
        <Route path="/hostel-admin/hostels" element={<HostelAdminHostels />} />
        <Route path="/hostel-admin/attendance" element={<HostelAdminAttendance />} />
        <Route path="/hostel-admin/gate-pass" element={<HostelAdminGatePass />} />
        <Route path="/hostel-admin/requests" element={<HostelAdminRequests />} />
        <Route path="/hostel-admin/reports" element={<HostelAdminReports />} />
        <Route path="/hostel-admin/configuration" element={<HostelAdminConfiguration />} />
        <Route path="/payment-administrator/dashboard" element={<PaymentAdministratorDashboard />} />
        <Route path="/payment-administrator/notice-board" element={<PaymentAdministratorNoticeBoard />} />
        <Route path="/payment-administrator/academic-fees" element={<PaymentAdministratorAcademicFees />} />
        <Route path="/payment-administrator/student-permissions" element={<PaymentAdministratorStudentPermissions />} />
        <Route path="/payment-administrator/exam-fee-restrictions" element={<PaymentAdministratorExamFeeRestrictions />} />
        <Route path="/payment-administrator/examination-fees" element={<PaymentAdministratorExaminationFees />} />
        <Route path="/payment-administrator/open-payments" element={<PaymentAdministratorOpenPayments />} />
        <Route path="/payment-administrator/configuration" element={<PaymentAdministratorConfiguration />} />
        <Route path="/payment-administrator/reports" element={<PaymentAdministratorReports />} />
        <Route path="/payment-administrator/concessions" element={<PaymentAdministratorConcessions />} />
        <Route path="/payment-administrator/online-transactions" element={<PaymentAdministratorOnlineTransactions />} />
        <Route path="/payment-administrator/challans" element={<PaymentAdministratorChallans />} />
        <Route path="/payment-administrator/statements" element={<PaymentAdministratorStatements />} />
        <Route path="/payment-administrator/scholarships" element={<PaymentAdministratorScholarships />} />
        <Route path="/payment-administrator/credit-memos" element={<PaymentAdministratorCreditMemos />} />
        <Route path="/payment-administrator/student-fee-card" element={<PaymentAdministratorStudentFeeCard />} />
        <Route path="/payment-administrator/transaction-card" element={<PaymentAdministratorTransactionCard />} />
        <Route path="/student/dashboard" element={<StudentDashboard />} />
        <Route path="/student/notice-board" element={<StudentNoticeBoard />} />
        <Route path="/student/attendance" element={<StudentAttendance />} />
        <Route path="/student/chatbot" element={<StudentChatbot />} />
        <Route path="/student/teacher-communications" element={<StudentTeacherCommunications />} />
        <Route path="/student/fees" element={<StudentFees />} />
        <Route path="/student/examinations" element={<StudentExaminations />} />
        <Route path="/student/co-curricular-activities" element={<StudentCoCurricularActivities />} />
        <Route path="/student/learning-management" element={<StudentLearningManagement />} />
        <Route path="/student/course-tracking" element={<StudentCourseTracking />} />
        <Route path="/student/profile" element={<StudentProfile />} />
        <Route path="/student/payment-history" element={<StudentPaymentHistory />} />
        <Route path="/examination/dashboard" element={<ExaminationDashboard />} />
        <Route path="/examination/notice-board" element={<ExaminationNoticeBoard />} />
        <Route path="/examination/results" element={<ExaminationResults />} />
        <Route path="/examination/previous-exams" element={<ExaminationPreviousExams />} />
        <Route path="/examination/tests" element={<ExaminationTests />} />
        <Route path="/examination/previous-year-papers" element={<ExaminationPreviousYearPapers />} />
        <Route path="/examination/averages" element={<ExaminationAverages />} />
        <Route path="/examination/class-toppers" element={<ExaminationClassToppers />} />
        <Route path="/examination/reports" element={<ExaminationReports />} />
        <Route path="/sports-officer/dashboard" element={<SportsOfficerDashboard />} />
        <Route path="/sports-officer/notice-board" element={<SportsOfficerNoticeBoard />} />
        <Route path="/sports-officer/sports-events" element={<SportsOfficerSportsEvents />} />
        <Route path="/sports-officer/team-management" element={<SportsOfficerTeamManagement />} />
        <Route path="/sports-officer/player-registrations" element={<SportsOfficerPlayerRegistrations />} />
        <Route path="/sports-officer/practice-schedules" element={<SportsOfficerPracticeSchedules />} />
        <Route path="/sports-officer/tournament-management" element={<SportsOfficerTournamentManagement />} />
        <Route path="/sports-officer/performance-tracking" element={<SportsOfficerPerformanceTracking />} />
        <Route path="/sports-officer/reports" element={<SportsOfficerReports />} />
        <Route path="/sports-officer/activities-list" element={<SportsOfficerActivitiesList />} />
        <Route path="/sports-officer/event-calendar" element={<SportsOfficerEventCalendar />} />
        <Route path="/sports-officer/student-participation" element={<SportsOfficerStudentParticipation />} />
        <Route path="/sports-officer/achievements" element={<SportsOfficerAchievements />} />
        <Route path="/sports-officer/certificates" element={<SportsOfficerCertificates />} />
        <Route path="/sports-officer/clubs-management" element={<SportsOfficerClubsManagement />} />
        <Route path="/sports-officer/announcements" element={<SportsOfficerAnnouncements />} />
        
        {/* Fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
};

export default App;
