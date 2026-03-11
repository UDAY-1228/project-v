import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import Login from './pages/auth/Login';
import ForgotPassword from './pages/auth/ForgotPassword';
import ResetPassword from './pages/auth/ResetPassword';
import ChangePassword from './pages/auth/ChangePassword';
import Logout from './pages/auth/Logout';
import ActiveSessions from './pages/auth/ActiveSessions';
import StudentProfile from './pages/profiles/StudentProfile';
import ParentProfile from './pages/profiles/ParentProfile';
import TeacherProfile from './pages/profiles/TeacherProfile';
import AdminProfile from './pages/profiles/AdminProfile';
import DeveloperProfile from './pages/profiles/DeveloperProfile';
import VirtualID from './pages/profiles/VirtualID';
import ProfileEdit from './pages/profiles/ProfileEdit';
import RoleList from './pages/roles/RoleList';
import AssignRole from './pages/roles/AssignRole';
import PermissionMatrix from './pages/roles/PermissionMatrix';
import RoleChangeHistory from './pages/roles/RoleChangeHistory';
import PrivacySettings from './pages/privacy/PrivacySettings';
import BiometricConsent from './pages/privacy/BiometricConsent';
import DataDownloadRequest from './pages/privacy/DataDownloadRequest';
import StudentAttendanceDashboard from './pages/attendance/StudentAttendanceDashboard';
import ClassAttendanceDashboard from './pages/attendance/ClassAttendanceDashboard';
import AttendanceDetail from './pages/attendance/AttendanceDetail';
import FaceEnrollment from './pages/attendance/FaceEnrollment';
import FlaggedAttendance from './pages/attendance/FlaggedAttendance';
import OverrideRequests from './pages/attendance/OverrideRequests';
import CCTVLiveView from './pages/cctv/CCTVLiveView';
import KioskList from './pages/cctv/KioskList';
import KioskSettings from './pages/cctv/KioskSettings';
import AttendancePolicy from './pages/attendance/AttendancePolicy';
import HolidaySetup from './pages/attendance/HolidaySetup';
import AttendanceAlertSettings from './pages/attendance/AttendanceAlertSettings';
import AttendanceNotificationLog from './pages/attendance/AttendanceNotificationLog';
import MyTimetableStudent from './pages/timetable/MyTimetableStudent';
import MyTimetableTeacher from './pages/timetable/MyTimetableTeacher';
import ClassTimetable from './pages/timetable/ClassTimetable';
import TimetableGenerator from './pages/timetable/TimetableGenerator';
import ConflictResolver from './pages/timetable/ConflictResolver';
import TimetableChangeHistory from './pages/timetable/TimetableChangeHistory';
import InstitutionCalendar from './pages/calendar/InstitutionCalendar';
import MyCalendar from './pages/calendar/MyCalendar';
import EventDetails from './pages/calendar/EventDetails';
import EventManagement from './pages/calendar/EventManagement';
import FeePlanSetup from './pages/fees/FeePlanSetup';
import InvoiceList from './pages/fees/InvoiceList';
import WaiverScholarship from './pages/fees/WaiverScholarship';
import FeeDueList from './pages/fees/FeeDueList';
import PaymentHome from './pages/fees/PaymentHome';
import PaymentMethods from './pages/fees/PaymentMethods';
import PaymentConfirmation from './pages/fees/PaymentConfirmation';
import ReceiptDownload from './pages/fees/ReceiptDownload';
import StudentTransactionHistory from './pages/fees/StudentTransactionHistory';
import AdminOnlineTransactions from './pages/fees/AdminOnlineTransactions';
import ManualPaymentEntry from './pages/fees/ManualPaymentEntry';
import FailedTransactions from './pages/fees/FailedTransactions';
import RefundManagement from './pages/fees/RefundManagement';
import MyCourses from './pages/lms/MyCourses';
import CourseDetail from './pages/lms/CourseDetail';
import LessonsTopics from './pages/lms/LessonsTopics';
import ResourcesHandouts from './pages/lms/ResourcesHandouts';
import StudentAssignmentList from './pages/lms/StudentAssignmentList';
import TeacherAssignmentList from './pages/lms/TeacherAssignmentList';
import AssignmentDetail from './pages/lms/AssignmentDetail';
import SubmitAssignment from './pages/lms/SubmitAssignment';
import GradeFeedback from './pages/lms/GradeFeedback';
import HomeworkList from './pages/homework/HomeworkList';
import AIHomeworkHelper from './pages/homework/AIHomeworkHelper';
import AIExplanationView from './pages/homework/AIExplanationView';
import HomeworkProgress from './pages/homework/HomeworkProgress';
import AskAssistant from './pages/chatbot/AskAssistant';
import ChatHistory from './pages/chatbot/ChatHistory';
import HumanSupport from './pages/chatbot/HumanSupport';
import ExamCalendar from './pages/exams/ExamCalendar';
import ExamTimetable from './pages/exams/ExamTimetable';
import ExamSetup from './pages/exams/ExamSetup';
import HallTicket from './pages/exams/HallTicket';
import MarksEntry from './pages/results/MarksEntry';
import ResultVerification from './pages/results/ResultVerification';
import PublishResults from './pages/results/PublishResults';
import StudentResultCard from './pages/results/StudentResultCard';
import PracticeTestsList from './pages/practice/PracticeTestsList';
import StartAITest from './pages/practice/StartAITest';
import TestResultAnalysis from './pages/practice/TestResultAnalysis';
import TeacherTestRequest from './pages/practice/TeacherTestRequest';
import StudentAnalytics from './pages/analytics/StudentAnalytics';
import ClassAnalytics from './pages/analytics/ClassAnalytics';
import DepartmentAnalytics from './pages/analytics/DepartmentAnalytics';
import InstitutionAnalytics from './pages/analytics/InstitutionAnalytics';
import AtRiskStudents from './pages/analytics/AtRiskStudents';
import Feed from './pages/noticeboard/Feed';
import Announcements from './pages/noticeboard/Announcements';
import NoticeDetails from './pages/noticeboard/NoticeDetails';
import CreateNotice from './pages/noticeboard/CreateNotice';
import MessagesInbox from './pages/messaging/MessagesInbox';
import MessagesOutbox from './pages/messaging/MessagesOutbox';
import ClassChannel from './pages/messaging/ClassChannel';
import ParentTeacherChat from './pages/messaging/ParentTeacherChat';
import PTMScheduler from './pages/messaging/PTMScheduler';
import PTMSlotBooking from './pages/messaging/PTMSlotBooking';
import PTMSummary from './pages/messaging/PTMSummary';
import ClubsDirectory from './pages/clubs/ClubsDirectory';
import MyClubs from './pages/clubs/MyClubs';
import ClubDetail from './pages/clubs/ClubDetail';
import CoCurricularCalendar from './pages/clubs/CoCurricularCalendar';
import ClubAdmin from './pages/clubs/ClubAdmin';
import ToolsHome from './pages/tools/ToolsHome';
import SubmitFeedback from './pages/feedback/SubmitFeedback';
import FeedbackList from './pages/feedback/FeedbackList';
import FeedbackAnalytics from './pages/feedback/FeedbackAnalytics';
import CreateTicket from './pages/helpdesk/CreateTicket';
import TicketStatus from './pages/helpdesk/TicketStatus';
import FAQ from './pages/helpdesk/FAQ';
import ContactSupport from './pages/helpdesk/ContactSupport';
import NotificationList from './pages/notifications/NotificationList';
import NotificationSettings from './pages/notifications/NotificationSettings';
import TemplateManagement from './pages/notifications/TemplateManagement';
import UserActivityLog from './pages/audit/UserActivityLog';
import SystemAuditLog from './pages/audit/SystemAuditLog';
import InstitutionList from './pages/institution/InstitutionList';
import InstitutionDetail from './pages/institution/InstitutionDetail';
import LicenseLimits from './pages/institution/LicenseLimits';
import DataBackupExport from './pages/institution/DataBackupExport';

const App: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Navigate to="/tools/toolshome" replace />} />
                <Route path="/auth/login" element={<Login />} />
                <Route path="/auth/forgotpassword" element={<ForgotPassword />} />
                <Route path="/auth/resetpassword" element={<ResetPassword />} />
                <Route path="/auth/changepassword" element={<ChangePassword />} />
                <Route path="/auth/logout" element={<Logout />} />
                <Route path="/auth/activesessions" element={<ActiveSessions />} />
                <Route path="/profiles/studentprofile" element={<StudentProfile />} />
                <Route path="/profiles/parentprofile" element={<ParentProfile />} />
                <Route path="/profiles/teacherprofile" element={<TeacherProfile />} />
                <Route path="/profiles/adminprofile" element={<AdminProfile />} />
                <Route path="/profiles/developerprofile" element={<DeveloperProfile />} />
                <Route path="/profiles/virtualid" element={<VirtualID />} />
                <Route path="/profiles/profileedit" element={<ProfileEdit />} />
                <Route path="/roles/rolelist" element={<RoleList />} />
                <Route path="/roles/assignrole" element={<AssignRole />} />
                <Route path="/roles/permissionmatrix" element={<PermissionMatrix />} />
                <Route path="/roles/rolechangehistory" element={<RoleChangeHistory />} />
                <Route path="/privacy/privacysettings" element={<PrivacySettings />} />
                <Route path="/privacy/biometricconsent" element={<BiometricConsent />} />
                <Route path="/privacy/datadownloadrequest" element={<DataDownloadRequest />} />
                <Route path="/attendance/studentattendancedashboard" element={<StudentAttendanceDashboard />} />
                <Route path="/attendance/classattendancedashboard" element={<ClassAttendanceDashboard />} />
                <Route path="/attendance/attendancedetail" element={<AttendanceDetail />} />
                <Route path="/attendance/faceenrollment" element={<FaceEnrollment />} />
                <Route path="/attendance/flaggedattendance" element={<FlaggedAttendance />} />
                <Route path="/attendance/overriderequests" element={<OverrideRequests />} />
                <Route path="/cctv/cctvliveview" element={<CCTVLiveView />} />
                <Route path="/cctv/kiosklist" element={<KioskList />} />
                <Route path="/cctv/kiosksettings" element={<KioskSettings />} />
                <Route path="/attendance/attendancepolicy" element={<AttendancePolicy />} />
                <Route path="/attendance/holidaysetup" element={<HolidaySetup />} />
                <Route path="/attendance/attendancealertsettings" element={<AttendanceAlertSettings />} />
                <Route path="/attendance/attendancenotificationlog" element={<AttendanceNotificationLog />} />
                <Route path="/timetable/mytimetablestudent" element={<MyTimetableStudent />} />
                <Route path="/timetable/mytimetableteacher" element={<MyTimetableTeacher />} />
                <Route path="/timetable/classtimetable" element={<ClassTimetable />} />
                <Route path="/timetable/timetablegenerator" element={<TimetableGenerator />} />
                <Route path="/timetable/conflictresolver" element={<ConflictResolver />} />
                <Route path="/timetable/timetablechangehistory" element={<TimetableChangeHistory />} />
                <Route path="/calendar/institutioncalendar" element={<InstitutionCalendar />} />
                <Route path="/calendar/mycalendar" element={<MyCalendar />} />
                <Route path="/calendar/eventdetails" element={<EventDetails />} />
                <Route path="/calendar/eventmanagement" element={<EventManagement />} />
                <Route path="/fees/feeplansetup" element={<FeePlanSetup />} />
                <Route path="/fees/invoicelist" element={<InvoiceList />} />
                <Route path="/fees/waiverscholarship" element={<WaiverScholarship />} />
                <Route path="/fees/feeduelist" element={<FeeDueList />} />
                <Route path="/fees/paymenthome" element={<PaymentHome />} />
                <Route path="/fees/paymentmethods" element={<PaymentMethods />} />
                <Route path="/fees/paymentconfirmation" element={<PaymentConfirmation />} />
                <Route path="/fees/receiptdownload" element={<ReceiptDownload />} />
                <Route path="/fees/studenttransactionhistory" element={<StudentTransactionHistory />} />
                <Route path="/fees/adminonlinetransactions" element={<AdminOnlineTransactions />} />
                <Route path="/fees/manualpaymententry" element={<ManualPaymentEntry />} />
                <Route path="/fees/failedtransactions" element={<FailedTransactions />} />
                <Route path="/fees/refundmanagement" element={<RefundManagement />} />
                <Route path="/lms/mycourses" element={<MyCourses />} />
                <Route path="/lms/coursedetail" element={<CourseDetail />} />
                <Route path="/lms/lessonstopics" element={<LessonsTopics />} />
                <Route path="/lms/resourceshandouts" element={<ResourcesHandouts />} />
                <Route path="/lms/studentassignmentlist" element={<StudentAssignmentList />} />
                <Route path="/lms/teacherassignmentlist" element={<TeacherAssignmentList />} />
                <Route path="/lms/assignmentdetail" element={<AssignmentDetail />} />
                <Route path="/lms/submitassignment" element={<SubmitAssignment />} />
                <Route path="/lms/gradefeedback" element={<GradeFeedback />} />
                <Route path="/homework/homeworklist" element={<HomeworkList />} />
                <Route path="/homework/aihomeworkhelper" element={<AIHomeworkHelper />} />
                <Route path="/homework/aiexplanationview" element={<AIExplanationView />} />
                <Route path="/homework/homeworkprogress" element={<HomeworkProgress />} />
                <Route path="/chatbot/askassistant" element={<AskAssistant />} />
                <Route path="/chatbot/chathistory" element={<ChatHistory />} />
                <Route path="/chatbot/humansupport" element={<HumanSupport />} />
                <Route path="/exams/examcalendar" element={<ExamCalendar />} />
                <Route path="/exams/examtimetable" element={<ExamTimetable />} />
                <Route path="/exams/examsetup" element={<ExamSetup />} />
                <Route path="/exams/hallticket" element={<HallTicket />} />
                <Route path="/results/marksentry" element={<MarksEntry />} />
                <Route path="/results/resultverification" element={<ResultVerification />} />
                <Route path="/results/publishresults" element={<PublishResults />} />
                <Route path="/results/studentresultcard" element={<StudentResultCard />} />
                <Route path="/practice/practicetestslist" element={<PracticeTestsList />} />
                <Route path="/practice/startaitest" element={<StartAITest />} />
                <Route path="/practice/testresultanalysis" element={<TestResultAnalysis />} />
                <Route path="/practice/teachertestrequest" element={<TeacherTestRequest />} />
                <Route path="/analytics/studentanalytics" element={<StudentAnalytics />} />
                <Route path="/analytics/classanalytics" element={<ClassAnalytics />} />
                <Route path="/analytics/departmentanalytics" element={<DepartmentAnalytics />} />
                <Route path="/analytics/institutionanalytics" element={<InstitutionAnalytics />} />
                <Route path="/analytics/atriskstudents" element={<AtRiskStudents />} />
                <Route path="/noticeboard/feed" element={<Feed />} />
                <Route path="/noticeboard/announcements" element={<Announcements />} />
                <Route path="/noticeboard/noticedetails" element={<NoticeDetails />} />
                <Route path="/noticeboard/createnotice" element={<CreateNotice />} />
                <Route path="/messaging/messagesinbox" element={<MessagesInbox />} />
                <Route path="/messaging/messagesoutbox" element={<MessagesOutbox />} />
                <Route path="/messaging/classchannel" element={<ClassChannel />} />
                <Route path="/messaging/parentteacherchat" element={<ParentTeacherChat />} />
                <Route path="/messaging/ptmscheduler" element={<PTMScheduler />} />
                <Route path="/messaging/ptmslotbooking" element={<PTMSlotBooking />} />
                <Route path="/messaging/ptmsummary" element={<PTMSummary />} />
                <Route path="/clubs/clubsdirectory" element={<ClubsDirectory />} />
                <Route path="/clubs/myclubs" element={<MyClubs />} />
                <Route path="/clubs/clubdetail" element={<ClubDetail />} />
                <Route path="/clubs/cocurricularcalendar" element={<CoCurricularCalendar />} />
                <Route path="/clubs/clubadmin" element={<ClubAdmin />} />
                <Route path="/tools/toolshome" element={<ToolsHome />} />
                <Route path="/feedback/submitfeedback" element={<SubmitFeedback />} />
                <Route path="/feedback/feedbacklist" element={<FeedbackList />} />
                <Route path="/feedback/feedbackanalytics" element={<FeedbackAnalytics />} />
                <Route path="/helpdesk/createticket" element={<CreateTicket />} />
                <Route path="/helpdesk/ticketstatus" element={<TicketStatus />} />
                <Route path="/helpdesk/faq" element={<FAQ />} />
                <Route path="/helpdesk/contactsupport" element={<ContactSupport />} />
                <Route path="/notifications/notificationlist" element={<NotificationList />} />
                <Route path="/notifications/notificationsettings" element={<NotificationSettings />} />
                <Route path="/notifications/templatemanagement" element={<TemplateManagement />} />
                <Route path="/audit/useractivitylog" element={<UserActivityLog />} />
                <Route path="/audit/systemauditlog" element={<SystemAuditLog />} />
                <Route path="/institution/institutionlist" element={<InstitutionList />} />
                <Route path="/institution/institutiondetail" element={<InstitutionDetail />} />
                <Route path="/institution/licenselimits" element={<LicenseLimits />} />
                <Route path="/institution/databackupexport" element={<DataBackupExport />} />
            </Routes>
        </Router>
    );
};

export default App;
