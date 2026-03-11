import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
    {
        path: '',
        redirectTo: 'tools/home',
        pathMatch: 'full'
    },
    {
        path: 'auth/login',
        loadChildren: () => import('./auth/login/login.module').then(m => m.LoginPageModule)
    },
    {
        path: 'auth/forgot-password',
        loadChildren: () => import('./auth/forgot-password/forgotpassword.module').then(m => m.ForgotPasswordPageModule)
    },
    {
        path: 'auth/reset-password',
        loadChildren: () => import('./auth/reset-password/resetpassword.module').then(m => m.ResetPasswordPageModule)
    },
    {
        path: 'auth/change-password',
        loadChildren: () => import('./auth/change-password/changepassword.module').then(m => m.ChangePasswordPageModule)
    },
    {
        path: 'auth/logout',
        loadChildren: () => import('./auth/logout/logout.module').then(m => m.LogoutPageModule)
    },
    {
        path: 'auth/active-sessions',
        loadChildren: () => import('./auth/active-sessions/activesessions.module').then(m => m.ActiveSessionsPageModule)
    },
    {
        path: 'profile/student',
        loadChildren: () => import('./profile/student/studentprofile.module').then(m => m.StudentProfilePageModule)
    },
    {
        path: 'profile/parent',
        loadChildren: () => import('./profile/parent/parentprofile.module').then(m => m.ParentProfilePageModule)
    },
    {
        path: 'profile/teacher',
        loadChildren: () => import('./profile/teacher/teacherprofile.module').then(m => m.TeacherProfilePageModule)
    },
    {
        path: 'profile/admin',
        loadChildren: () => import('./profile/admin/adminprofile.module').then(m => m.AdminProfilePageModule)
    },
    {
        path: 'profile/developer',
        loadChildren: () => import('./profile/developer/developerprofile.module').then(m => m.DeveloperProfilePageModule)
    },
    {
        path: 'profile/virtual-id',
        loadChildren: () => import('./profile/virtual-id/virtualid.module').then(m => m.VirtualIDPageModule)
    },
    {
        path: 'profile/edit',
        loadChildren: () => import('./profile/edit/profileedit.module').then(m => m.ProfileEditPageModule)
    },
    {
        path: 'roles/list',
        loadChildren: () => import('./roles/list/rolelist.module').then(m => m.RoleListPageModule)
    },
    {
        path: 'roles/assign',
        loadChildren: () => import('./roles/assign/assignrole.module').then(m => m.AssignRolePageModule)
    },
    {
        path: 'roles/permission-matrix',
        loadChildren: () => import('./roles/permission-matrix/permissionmatrix.module').then(m => m.PermissionMatrixPageModule)
    },
    {
        path: 'roles/history',
        loadChildren: () => import('./roles/history/rolehistory.module').then(m => m.RoleHistoryPageModule)
    },
    {
        path: 'privacy/settings',
        loadChildren: () => import('./privacy/settings/privacysettings.module').then(m => m.PrivacySettingsPageModule)
    },
    {
        path: 'privacy/biometric-consent',
        loadChildren: () => import('./privacy/biometric-consent/biometricconsent.module').then(m => m.BiometricConsentPageModule)
    },
    {
        path: 'privacy/download-request',
        loadChildren: () => import('./privacy/download-request/datadownloadrequest.module').then(m => m.DataDownloadRequestPageModule)
    },
    {
        path: 'academic/attendance/dashboard',
        loadChildren: () => import('./academic/attendance/dashboard/attendancedashboard.module').then(m => m.AttendanceDashboardPageModule)
    },
    {
        path: 'academic/attendance/class',
        loadChildren: () => import('./academic/attendance/class/classattendance.module').then(m => m.ClassAttendancePageModule)
    },
    {
        path: 'academic/attendance/detail',
        loadChildren: () => import('./academic/attendance/detail/attendancedetail.module').then(m => m.AttendanceDetailPageModule)
    },
    {
        path: 'academic/attendance/enroll',
        loadChildren: () => import('./academic/attendance/enroll/faceenrollment.module').then(m => m.FaceEnrollmentPageModule)
    },
    {
        path: 'academic/attendance/flagged',
        loadChildren: () => import('./academic/attendance/flagged/flaggedattendance.module').then(m => m.FlaggedAttendancePageModule)
    },
    {
        path: 'academic/attendance/overrides',
        loadChildren: () => import('./academic/attendance/overrides/overriderequests.module').then(m => m.OverrideRequestsPageModule)
    },
    {
        path: 'academic/attendance/policy',
        loadChildren: () => import('./academic/attendance/policy/attendancepolicy.module').then(m => m.AttendancePolicyPageModule)
    },
    {
        path: 'academic/attendance/holidays',
        loadChildren: () => import('./academic/attendance/holidays/holidaysetup.module').then(m => m.HolidaySetupPageModule)
    },
    {
        path: 'academic/attendance/alerts',
        loadChildren: () => import('./academic/attendance/alerts/attendancealerts.module').then(m => m.AttendanceAlertsPageModule)
    },
    {
        path: 'academic/attendance/logs',
        loadChildren: () => import('./academic/attendance/logs/attendancelogs.module').then(m => m.AttendanceLogsPageModule)
    },
    {
        path: 'academic/timetable/student',
        loadChildren: () => import('./academic/timetable/student/studenttimetable.module').then(m => m.StudentTimetablePageModule)
    },
    {
        path: 'academic/timetable/teacher',
        loadChildren: () => import('./academic/timetable/teacher/teachertimetable.module').then(m => m.TeacherTimetablePageModule)
    },
    {
        path: 'academic/timetable/class',
        loadChildren: () => import('./academic/timetable/class/classtimetable.module').then(m => m.ClassTimetablePageModule)
    },
    {
        path: 'academic/timetable/generator',
        loadChildren: () => import('./academic/timetable/generator/timetablegenerator.module').then(m => m.TimetableGeneratorPageModule)
    },
    {
        path: 'academic/timetable/conflicts',
        loadChildren: () => import('./academic/timetable/conflicts/conflictresolver.module').then(m => m.ConflictResolverPageModule)
    },
    {
        path: 'academic/timetable/history',
        loadChildren: () => import('./academic/timetable/history/timetablehistory.module').then(m => m.TimetableHistoryPageModule)
    },
    {
        path: 'academic/calendar/institution',
        loadChildren: () => import('./academic/calendar/institution/institutioncalendar.module').then(m => m.InstitutionCalendarPageModule)
    },
    {
        path: 'academic/calendar/personal',
        loadChildren: () => import('./academic/calendar/personal/mycalendar.module').then(m => m.MyCalendarPageModule)
    },
    {
        path: 'academic/calendar/event-details',
        loadChildren: () => import('./academic/calendar/event-details/eventdetails.module').then(m => m.EventDetailsPageModule)
    },
    {
        path: 'academic/calendar/manage',
        loadChildren: () => import('./academic/calendar/manage/eventmanagement.module').then(m => m.EventManagementPageModule)
    },
    {
        path: 'finance/fees/setup',
        loadChildren: () => import('./finance/fees/setup/feeplansetup.module').then(m => m.FeePlanSetupPageModule)
    },
    {
        path: 'finance/fees/invoices',
        loadChildren: () => import('./finance/fees/invoices/invoicelist.module').then(m => m.InvoiceListPageModule)
    },
    {
        path: 'finance/fees/waivers',
        loadChildren: () => import('./finance/fees/waivers/feewaiver.module').then(m => m.FeeWaiverPageModule)
    },
    {
        path: 'finance/fees/due',
        loadChildren: () => import('./finance/fees/due/feeduelist.module').then(m => m.FeeDueListPageModule)
    },
    {
        path: 'finance/fees/payment-home',
        loadChildren: () => import('./finance/fees/payment-home/paymenthome.module').then(m => m.PaymentHomePageModule)
    },
    {
        path: 'finance/fees/methods',
        loadChildren: () => import('./finance/fees/methods/paymentmethods.module').then(m => m.PaymentMethodsPageModule)
    },
    {
        path: 'finance/fees/confirmation',
        loadChildren: () => import('./finance/fees/confirmation/paymentconfirmation.module').then(m => m.PaymentConfirmationPageModule)
    },
    {
        path: 'finance/fees/receipts',
        loadChildren: () => import('./finance/fees/receipts/receiptdownload.module').then(m => m.ReceiptDownloadPageModule)
    },
    {
        path: 'finance/fees/history',
        loadChildren: () => import('./finance/fees/history/transactionhistory.module').then(m => m.TransactionHistoryPageModule)
    },
    {
        path: 'finance/fees/admin-online',
        loadChildren: () => import('./finance/fees/admin-online/admintransactions.module').then(m => m.AdminTransactionsPageModule)
    },
    {
        path: 'finance/fees/manual-entry',
        loadChildren: () => import('./finance/fees/manual-entry/manualpayment.module').then(m => m.ManualPaymentPageModule)
    },
    {
        path: 'finance/fees/failed',
        loadChildren: () => import('./finance/fees/failed/failedtransactions.module').then(m => m.FailedTransactionsPageModule)
    },
    {
        path: 'finance/fees/refunds',
        loadChildren: () => import('./finance/fees/refunds/refundmanagement.module').then(m => m.RefundManagementPageModule)
    },
    {
        path: 'lms/courses',
        loadChildren: () => import('./lms/courses/mycourses.module').then(m => m.MyCoursesPageModule)
    },
    {
        path: 'lms/course-detail',
        loadChildren: () => import('./lms/course-detail/coursedetail.module').then(m => m.CourseDetailPageModule)
    },
    {
        path: 'lms/lessons',
        loadChildren: () => import('./lms/lessons/lessonstopics.module').then(m => m.LessonsTopicsPageModule)
    },
    {
        path: 'lms/resources',
        loadChildren: () => import('./lms/resources/resourceshandouts.module').then(m => m.ResourcesHandoutsPageModule)
    },
    {
        path: 'lms/assignments-student',
        loadChildren: () => import('./lms/assignments-student/studentassignments.module').then(m => m.StudentAssignmentsPageModule)
    },
    {
        path: 'lms/assignments-teacher',
        loadChildren: () => import('./lms/assignments-teacher/teacherassignments.module').then(m => m.TeacherAssignmentsPageModule)
    },
    {
        path: 'lms/assignment-detail',
        loadChildren: () => import('./lms/assignment-detail/assignmentdetail.module').then(m => m.AssignmentDetailPageModule)
    },
    {
        path: 'lms/submit',
        loadChildren: () => import('./lms/submit/submitassignment.module').then(m => m.SubmitAssignmentPageModule)
    },
    {
        path: 'lms/grade',
        loadChildren: () => import('./lms/grade/gradefeedback.module').then(m => m.GradeFeedbackPageModule)
    },
    {
        path: 'homework/list',
        loadChildren: () => import('./homework/list/homeworklist.module').then(m => m.HomeworkListPageModule)
    },
    {
        path: 'homework/ai-helper',
        loadChildren: () => import('./homework/ai-helper/aihomeworkhelper.module').then(m => m.AIHomeworkHelperPageModule)
    },
    {
        path: 'homework/ai-explanation',
        loadChildren: () => import('./homework/ai-explanation/aiexplanation.module').then(m => m.AIExplanationPageModule)
    },
    {
        path: 'homework/progress',
        loadChildren: () => import('./homework/progress/homeworkprogress.module').then(m => m.HomeworkProgressPageModule)
    },
    {
        path: 'chatbot/ask',
        loadChildren: () => import('./chatbot/ask/askassistant.module').then(m => m.AskAssistantPageModule)
    },
    {
        path: 'chatbot/history',
        loadChildren: () => import('./chatbot/history/chathistory.module').then(m => m.ChatHistoryPageModule)
    },
    {
        path: 'chatbot/support',
        loadChildren: () => import('./chatbot/support/humansupport.module').then(m => m.HumanSupportPageModule)
    },
    {
        path: 'academic/exams/calendar',
        loadChildren: () => import('./academic/exams/calendar/examcalendar.module').then(m => m.ExamCalendarPageModule)
    },
    {
        path: 'academic/exams/timetable',
        loadChildren: () => import('./academic/exams/timetable/examtimetable.module').then(m => m.ExamTimetablePageModule)
    },
    {
        path: 'academic/exams/setup',
        loadChildren: () => import('./academic/exams/setup/examsetup.module').then(m => m.ExamSetupPageModule)
    },
    {
        path: 'academic/exams/hall-ticket',
        loadChildren: () => import('./academic/exams/hall-ticket/hallticket.module').then(m => m.HallTicketPageModule)
    },
    {
        path: 'academic/results/marks-entry',
        loadChildren: () => import('./academic/results/marks-entry/marksentry.module').then(m => m.MarksEntryPageModule)
    },
    {
        path: 'academic/results/verification',
        loadChildren: () => import('./academic/results/verification/resultverification.module').then(m => m.ResultVerificationPageModule)
    },
    {
        path: 'academic/results/publish',
        loadChildren: () => import('./academic/results/publish/publishresults.module').then(m => m.PublishResultsPageModule)
    },
    {
        path: 'academic/results/card',
        loadChildren: () => import('./academic/results/card/studentresultcard.module').then(m => m.StudentResultCardPageModule)
    },
    {
        path: 'practice/list',
        loadChildren: () => import('./practice/list/practicetestslist.module').then(m => m.PracticeTestsListPageModule)
    },
    {
        path: 'practice/ai-test',
        loadChildren: () => import('./practice/ai-test/startaitest.module').then(m => m.StartAITestPageModule)
    },
    {
        path: 'practice/analysis',
        loadChildren: () => import('./practice/analysis/testanalysis.module').then(m => m.TestAnalysisPageModule)
    },
    {
        path: 'practice/request',
        loadChildren: () => import('./practice/request/teachertestrequest.module').then(m => m.TeacherTestRequestPageModule)
    },
    {
        path: 'analytics/student',
        loadChildren: () => import('./analytics/student/studentanalytics.module').then(m => m.StudentAnalyticsPageModule)
    },
    {
        path: 'analytics/class',
        loadChildren: () => import('./analytics/class/classanalytics.module').then(m => m.ClassAnalyticsPageModule)
    },
    {
        path: 'analytics/department',
        loadChildren: () => import('./analytics/department/deptanalytics.module').then(m => m.DeptAnalyticsPageModule)
    },
    {
        path: 'analytics/institution',
        loadChildren: () => import('./analytics/institution/instanalytics.module').then(m => m.InstAnalyticsPageModule)
    },
    {
        path: 'analytics/at-risk',
        loadChildren: () => import('./analytics/at-risk/atriskstudents.module').then(m => m.AtRiskStudentsPageModule)
    },
    {
        path: 'noticeboard/feed',
        loadChildren: () => import('./noticeboard/feed/noticefeed.module').then(m => m.NoticeFeedPageModule)
    },
    {
        path: 'noticeboard/announcements',
        loadChildren: () => import('./noticeboard/announcements/announcements.module').then(m => m.AnnouncementsPageModule)
    },
    {
        path: 'noticeboard/details',
        loadChildren: () => import('./noticeboard/details/noticedetails.module').then(m => m.NoticeDetailsPageModule)
    },
    {
        path: 'noticeboard/create',
        loadChildren: () => import('./noticeboard/create/createnotice.module').then(m => m.CreateNoticePageModule)
    },
    {
        path: 'messaging/inbox',
        loadChildren: () => import('./messaging/inbox/messagesinbox.module').then(m => m.MessagesInboxPageModule)
    },
    {
        path: 'messaging/outbox',
        loadChildren: () => import('./messaging/outbox/messagesoutbox.module').then(m => m.MessagesOutboxPageModule)
    },
    {
        path: 'messaging/class-channel',
        loadChildren: () => import('./messaging/class-channel/classchannel.module').then(m => m.ClassChannelPageModule)
    },
    {
        path: 'messaging/ptm-chat',
        loadChildren: () => import('./messaging/ptm-chat/parentteacherchat.module').then(m => m.ParentTeacherChatPageModule)
    },
    {
        path: 'messaging/ptm-scheduler',
        loadChildren: () => import('./messaging/ptm-scheduler/ptmscheduler.module').then(m => m.PTMSchedulerPageModule)
    },
    {
        path: 'messaging/ptm-booking',
        loadChildren: () => import('./messaging/ptm-booking/ptmslotbooking.module').then(m => m.PTMSlotBookingPageModule)
    },
    {
        path: 'messaging/ptm-notes',
        loadChildren: () => import('./messaging/ptm-notes/ptmsummary.module').then(m => m.PTMSummaryPageModule)
    },
    {
        path: 'clubs/directory',
        loadChildren: () => import('./clubs/directory/clubsdirectory.module').then(m => m.ClubsDirectoryPageModule)
    },
    {
        path: 'clubs/my-clubs',
        loadChildren: () => import('./clubs/my-clubs/myclubs.module').then(m => m.MyClubsPageModule)
    },
    {
        path: 'clubs/detail',
        loadChildren: () => import('./clubs/detail/clubdetail.module').then(m => m.ClubDetailPageModule)
    },
    {
        path: 'clubs/calendar',
        loadChildren: () => import('./clubs/calendar/clubcalendar.module').then(m => m.ClubCalendarPageModule)
    },
    {
        path: 'clubs/admin',
        loadChildren: () => import('./clubs/admin/clubadmin.module').then(m => m.ClubAdminPageModule)
    },
    {
        path: 'tools/home',
        loadChildren: () => import('./tools/home/toolshome.module').then(m => m.ToolsHomePageModule)
    },
    {
        path: 'feedback/submit',
        loadChildren: () => import('./feedback/submit/submitfeedback.module').then(m => m.SubmitFeedbackPageModule)
    },
    {
        path: 'feedback/list',
        loadChildren: () => import('./feedback/list/feedbacklist.module').then(m => m.FeedbackListPageModule)
    },
    {
        path: 'feedback/analytics',
        loadChildren: () => import('./feedback/analytics/feedbackanalytics.module').then(m => m.FeedbackAnalyticsPageModule)
    },
    {
        path: 'helpdesk/create',
        loadChildren: () => import('./helpdesk/create/createticket.module').then(m => m.CreateTicketPageModule)
    },
    {
        path: 'helpdesk/status',
        loadChildren: () => import('./helpdesk/status/ticketstatus.module').then(m => m.TicketStatusPageModule)
    },
    {
        path: 'helpdesk/faq',
        loadChildren: () => import('./helpdesk/faq/faq.module').then(m => m.FAQPageModule)
    },
    {
        path: 'helpdesk/support',
        loadChildren: () => import('./helpdesk/support/contactsupport.module').then(m => m.ContactSupportPageModule)
    },
    {
        path: 'notifications/list',
        loadChildren: () => import('./notifications/list/notificationlist.module').then(m => m.NotificationListPageModule)
    },
    {
        path: 'notifications/settings',
        loadChildren: () => import('./notifications/settings/notificationsettings.module').then(m => m.NotificationSettingsPageModule)
    },
    {
        path: 'notifications/templates',
        loadChildren: () => import('./notifications/templates/templatemgmt.module').then(m => m.TemplateMgmtPageModule)
    },
    {
        path: 'audit/user-log',
        loadChildren: () => import('./audit/user-log/useractivitylog.module').then(m => m.UserActivityLogPageModule)
    },
    {
        path: 'audit/system-log',
        loadChildren: () => import('./audit/system-log/systemauditlog.module').then(m => m.SystemAuditLogPageModule)
    },
    {
        path: 'admin/institutions',
        loadChildren: () => import('./admin/institutions/institutionlist.module').then(m => m.InstitutionListPageModule)
    },
    {
        path: 'admin/institution-detail',
        loadChildren: () => import('./admin/institution-detail/institutiondetail.module').then(m => m.InstitutionDetailPageModule)
    },
    {
        path: 'admin/license',
        loadChildren: () => import('./admin/license/licenselimits.module').then(m => m.LicenseLimitsPageModule)
    },
    {
        path: 'admin/backup',
        loadChildren: () => import('./admin/backup/databackupexport.module').then(m => m.DataBackupExportPageModule)
    },
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
    ],
    exports: [RouterModule]
})
export class AppRoutingModule { }
