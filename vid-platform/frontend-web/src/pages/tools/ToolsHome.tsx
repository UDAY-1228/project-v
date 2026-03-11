import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { fetchConfig } from '../../services/api';

const ToolsHome: React.FC = () => {
    const [backendStatus, setBackendStatus] = useState<'connected' | 'offline' | 'loading'>('loading');

    useEffect(() => {
        const checkConnection = async () => {
            const config = await fetchConfig();
            setBackendStatus(config ? 'connected' : 'offline');
        };
        checkConnection();
    }, []);

    const modules = [
        {
            name: 'Auth', pages: [
                { title: 'Login', path: '/auth/login' },
                { title: 'ForgotPassword', path: '/auth/forgotpassword' },
                { title: 'ResetPassword', path: '/auth/resetpassword' },
                { title: 'ChangePassword', path: '/auth/changepassword' },
                { title: 'Logout', path: '/auth/logout' },
                { title: 'ActiveSessions', path: '/auth/activesessions' },
            ]
        },
        {
            name: 'Profiles', pages: [
                { title: 'StudentProfile', path: '/profiles/studentprofile' },
                { title: 'ParentProfile', path: '/profiles/parentprofile' },
                { title: 'TeacherProfile', path: '/profiles/teacherprofile' },
                { title: 'AdminProfile', path: '/profiles/adminprofile' },
                { title: 'DeveloperProfile', path: '/profiles/developerprofile' },
                { title: 'VirtualID', path: '/profiles/virtualid' },
                { title: 'ProfileEdit', path: '/profiles/profileedit' },
            ]
        },
        {
            name: 'Roles', pages: [
                { title: 'RoleList', path: '/roles/rolelist' },
                { title: 'AssignRole', path: '/roles/assignrole' },
                { title: 'PermissionMatrix', path: '/roles/permissionmatrix' },
                { title: 'RoleChangeHistory', path: '/roles/rolechangehistory' },
            ]
        },
        {
            name: 'Privacy', pages: [
                { title: 'PrivacySettings', path: '/privacy/privacysettings' },
                { title: 'BiometricConsent', path: '/privacy/biometricconsent' },
                { title: 'DataDownloadRequest', path: '/privacy/datadownloadrequest' },
            ]
        },
        {
            name: 'Attendance', pages: [
                { title: 'StudentAttendanceDashboard', path: '/attendance/studentattendancedashboard' },
                { title: 'ClassAttendanceDashboard', path: '/attendance/classattendancedashboard' },
                { title: 'AttendanceDetail', path: '/attendance/attendancedetail' },
                { title: 'FaceEnrollment', path: '/attendance/faceenrollment' },
                { title: 'FlaggedAttendance', path: '/attendance/flaggedattendance' },
                { title: 'OverrideRequests', path: '/attendance/overriderequests' },
            ]
        },
        {
            name: 'Cctv', pages: [
                { title: 'CCTVLiveView', path: '/cctv/cctvliveview' },
                { title: 'KioskList', path: '/cctv/kiosklist' },
                { title: 'KioskSettings', path: '/cctv/kiosksettings' },
            ]
        },
        {
            name: 'Attendance', pages: [
                { title: 'AttendancePolicy', path: '/attendance/attendancepolicy' },
                { title: 'HolidaySetup', path: '/attendance/holidaysetup' },
                { title: 'AttendanceAlertSettings', path: '/attendance/attendancealertsettings' },
                { title: 'AttendanceNotificationLog', path: '/attendance/attendancenotificationlog' },
            ]
        },
        {
            name: 'Timetable', pages: [
                { title: 'MyTimetableStudent', path: '/timetable/mytimetablestudent' },
                { title: 'MyTimetableTeacher', path: '/timetable/mytimetableteacher' },
                { title: 'ClassTimetable', path: '/timetable/classtimetable' },
                { title: 'TimetableGenerator', path: '/timetable/timetablegenerator' },
                { title: 'ConflictResolver', path: '/timetable/conflictresolver' },
                { title: 'TimetableChangeHistory', path: '/timetable/timetablechangehistory' },
            ]
        },
        {
            name: 'Calendar', pages: [
                { title: 'InstitutionCalendar', path: '/calendar/institutioncalendar' },
                { title: 'MyCalendar', path: '/calendar/mycalendar' },
                { title: 'EventDetails', path: '/calendar/eventdetails' },
                { title: 'EventManagement', path: '/calendar/eventmanagement' },
            ]
        },
        {
            name: 'Fees', pages: [
                { title: 'FeePlanSetup', path: '/fees/feeplansetup' },
                { title: 'InvoiceList', path: '/fees/invoicelist' },
                { title: 'WaiverScholarship', path: '/fees/waiverscholarship' },
                { title: 'FeeDueList', path: '/fees/feeduelist' },
                { title: 'PaymentHome', path: '/fees/paymenthome' },
                { title: 'PaymentMethods', path: '/fees/paymentmethods' },
                { title: 'PaymentConfirmation', path: '/fees/paymentconfirmation' },
                { title: 'ReceiptDownload', path: '/fees/receiptdownload' },
                { title: 'StudentTransactionHistory', path: '/fees/studenttransactionhistory' },
                { title: 'AdminOnlineTransactions', path: '/fees/adminonlinetransactions' },
                { title: 'ManualPaymentEntry', path: '/fees/manualpaymententry' },
                { title: 'FailedTransactions', path: '/fees/failedtransactions' },
                { title: 'RefundManagement', path: '/fees/refundmanagement' },
            ]
        },
        {
            name: 'Lms', pages: [
                { title: 'MyCourses', path: '/lms/mycourses' },
                { title: 'CourseDetail', path: '/lms/coursedetail' },
                { title: 'LessonsTopics', path: '/lms/lessonstopics' },
                { title: 'ResourcesHandouts', path: '/lms/resourceshandouts' },
                { title: 'StudentAssignmentList', path: '/lms/studentassignmentlist' },
                { title: 'TeacherAssignmentList', path: '/lms/teacherassignmentlist' },
                { title: 'AssignmentDetail', path: '/lms/assignmentdetail' },
                { title: 'SubmitAssignment', path: '/lms/submitassignment' },
                { title: 'GradeFeedback', path: '/lms/gradefeedback' },
            ]
        },
        {
            name: 'Homework', pages: [
                { title: 'HomeworkList', path: '/homework/homeworklist' },
                { title: 'AIHomeworkHelper', path: '/homework/aihomeworkhelper' },
                { title: 'AIExplanationView', path: '/homework/aiexplanationview' },
                { title: 'HomeworkProgress', path: '/homework/homeworkprogress' },
            ]
        },
        {
            name: 'Chatbot', pages: [
                { title: 'AskAssistant', path: '/chatbot/askassistant' },
                { title: 'ChatHistory', path: '/chatbot/chathistory' },
                { title: 'HumanSupport', path: '/chatbot/humansupport' },
            ]
        },
        {
            name: 'Exams', pages: [
                { title: 'ExamCalendar', path: '/exams/examcalendar' },
                { title: 'ExamTimetable', path: '/exams/examtimetable' },
                { title: 'ExamSetup', path: '/exams/examsetup' },
                { title: 'HallTicket', path: '/exams/hallticket' },
            ]
        },
        {
            name: 'Results', pages: [
                { title: 'MarksEntry', path: '/results/marksentry' },
                { title: 'ResultVerification', path: '/results/resultverification' },
                { title: 'PublishResults', path: '/results/publishresults' },
                { title: 'StudentResultCard', path: '/results/studentresultcard' },
            ]
        },
        {
            name: 'Practice', pages: [
                { title: 'PracticeTestsList', path: '/practice/practicetestslist' },
                { title: 'StartAITest', path: '/practice/startaitest' },
                { title: 'TestResultAnalysis', path: '/practice/testresultanalysis' },
                { title: 'TeacherTestRequest', path: '/practice/teachertestrequest' },
            ]
        },
        {
            name: 'Analytics', pages: [
                { title: 'StudentAnalytics', path: '/analytics/studentanalytics' },
                { title: 'ClassAnalytics', path: '/analytics/classanalytics' },
                { title: 'DepartmentAnalytics', path: '/analytics/departmentanalytics' },
                { title: 'InstitutionAnalytics', path: '/analytics/institutionanalytics' },
                { title: 'AtRiskStudents', path: '/analytics/atriskstudents' },
            ]
        },
        {
            name: 'Noticeboard', pages: [
                { title: 'Feed', path: '/noticeboard/feed' },
                { title: 'Announcements', path: '/noticeboard/announcements' },
                { title: 'NoticeDetails', path: '/noticeboard/noticedetails' },
                { title: 'CreateNotice', path: '/noticeboard/createnotice' },
            ]
        },
        {
            name: 'Messaging', pages: [
                { title: 'MessagesInbox', path: '/messaging/messagesinbox' },
                { title: 'MessagesOutbox', path: '/messaging/messagesoutbox' },
                { title: 'ClassChannel', path: '/messaging/classchannel' },
                { title: 'ParentTeacherChat', path: '/messaging/parentteacherchat' },
                { title: 'PTMScheduler', path: '/messaging/ptmscheduler' },
                { title: 'PTMSlotBooking', path: '/messaging/ptmslotbooking' },
                { title: 'PTMSummary', path: '/messaging/ptmsummary' },
            ]
        },
        {
            name: 'Clubs', pages: [
                { title: 'ClubsDirectory', path: '/clubs/clubsdirectory' },
                { title: 'MyClubs', path: '/clubs/myclubs' },
                { title: 'ClubDetail', path: '/clubs/clubdetail' },
                { title: 'CoCurricularCalendar', path: '/clubs/cocurricularcalendar' },
                { title: 'ClubAdmin', path: '/clubs/clubadmin' },
            ]
        },
        {
            name: 'Tools', pages: [
                { title: 'ToolsHome', path: '/tools/toolshome' },
            ]
        },
        {
            name: 'Feedback', pages: [
                { title: 'SubmitFeedback', path: '/feedback/submitfeedback' },
                { title: 'FeedbackList', path: '/feedback/feedbacklist' },
                { title: 'FeedbackAnalytics', path: '/feedback/feedbackanalytics' },
            ]
        },
        {
            name: 'Helpdesk', pages: [
                { title: 'CreateTicket', path: '/helpdesk/createticket' },
                { title: 'TicketStatus', path: '/helpdesk/ticketstatus' },
                { title: 'FAQ', path: '/helpdesk/faq' },
                { title: 'ContactSupport', path: '/helpdesk/contactsupport' },
            ]
        },
        {
            name: 'Notifications', pages: [
                { title: 'NotificationList', path: '/notifications/notificationlist' },
                { title: 'NotificationSettings', path: '/notifications/notificationsettings' },
                { title: 'TemplateManagement', path: '/notifications/templatemanagement' },
            ]
        },
        {
            name: 'Audit', pages: [
                { title: 'UserActivityLog', path: '/audit/useractivitylog' },
                { title: 'SystemAuditLog', path: '/audit/systemauditlog' },
            ]
        },
        {
            name: 'Institution', pages: [
                { title: 'InstitutionList', path: '/institution/institutionlist' },
                { title: 'InstitutionDetail', path: '/institution/institutiondetail' },
                { title: 'LicenseLimits', path: '/institution/licenselimits' },
                { title: 'DataBackupExport', path: '/institution/databackupexport' },
            ]
        }
    ];

    return (
        <DashboardLayout role="Admin">
            <div className="p-8">
                <header className="mb-12">
                    <h1 className="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight">
                        VID Tools Hub
                    </h1>
                    <p className="mt-2 text-lg text-gray-600 dark:text-gray-400">
                        Explore all 122 platform pages across all modules.
                    </p>
                </header>

                <div className="space-y-12">
                    {modules.map((module, idx) => (
                        <section key={idx} className="bg-white dark:bg-gray-800/50 rounded-3xl p-8 border border-gray-100 dark:border-gray-700/50 shadow-sm backdrop-blur-xl">
                            <h2 className="text-2xl font-bold text-indigo-600 dark:text-indigo-400 mb-6 flex items-center">
                                <span className="w-2 h-8 bg-indigo-600 dark:bg-indigo-400 rounded-full mr-4"></span>
                                {module.name}
                            </h2>
                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                                {module.pages.map((page, pIdx) => (
                                    <Link
                                        key={pIdx}
                                        to={page.path}
                                        className="group p-4 rounded-2xl bg-gray-50 dark:bg-gray-800/80 hover:bg-indigo-50 dark:hover:bg-indigo-900/40 border border-transparent hover:border-indigo-200 dark:hover:border-indigo-700 transition-all duration-300 transform hover:-translate-y-1"
                                    >
                                        <div className="flex items-center justify-between">
                                            <span className="text-sm font-semibold text-gray-700 dark:text-gray-200 group-hover:text-indigo-700 dark:group-hover:text-indigo-300">
                                                {page.title}
                                            </span>
                                            <svg className="w-5 h-5 text-gray-400 group-hover:text-indigo-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                                            </svg>
                                        </div>
                                    </Link>
                                ))}
                            </div>
                        </section>
                    ))}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default ToolsHome;
