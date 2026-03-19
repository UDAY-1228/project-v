import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';
import { roleGuard } from './core/guards/role.guard';

export const routes: Routes = [
  // Public routes
  {
    path: 'login',
    loadComponent: () => import('./auth/login/login.component').then(m => m.LoginComponent),
    title: 'EIMS — Login'
  },
  {
    path: 'forgot-password',
    loadComponent: () => import('./auth/forgot-password/forgot-password.component').then(m => m.ForgotPasswordComponent),
    title: 'Forgot Password'
  },

  // Auth Layout (Shell)
  {
    path: '',
    loadComponent: () => import('./core/shell/shell.component').then(m => m.ShellComponent),
    canActivate: [authGuard],
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },

      // ── Student routes ─────────────────────────────────────────
      {
        path: 'student',
        canActivate: [roleGuard],
        data: { roles: ['student'] },
        children: [
          { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
          { path: 'dashboard', loadComponent: () => import('./student/dashboard/student-dashboard.component').then(m => m.StudentDashboardComponent), title: 'Student Dashboard' },
          { path: 'timetable', loadComponent: () => import('./student/timetable/my-timetable.component').then(m => m.MyStudentTimetableComponent), title: 'My Timetable' },
          { path: 'attendance', loadComponent: () => import('./student/attendance/my-attendance.component').then(m => m.MyAttendanceComponent), title: 'My Attendance' },
          { path: 'lms', loadComponent: () => import('./student/lms/my-courses.component').then(m => m.MyCoursesComponent), title: 'My Courses' },
          { path: 'assignments', loadComponent: () => import('./student/lms/my-assignments.component').then(m => m.MyAssignmentsComponent), title: 'My Assignments' },
          { path: 'homework-helper', loadComponent: () => import('./student/lms/homework-helper.component').then(m => m.HomeworkHelperComponent), title: 'AI Homework Helper' },
          { path: 'exams', loadComponent: () => import('./student/exams/my-exams.component').then(m => m.MyExamsComponent), title: 'Exams' },
          { path: 'results', loadComponent: () => import('./student/exams/result-card.component').then(m => m.ResultCardComponent), title: 'Result Card' },
          { path: 'virtual-id', loadComponent: () => import('./student/virtual-id/my-virtual-id.component').then(m => m.MyVirtualIdComponent), title: 'My Virtual ID' },
          { path: 'notifications', loadComponent: () => import('./student/notifications/notifications.component').then(m => m.StudentNotificationsComponent), title: 'Notifications' },
          { path: 'fees', loadComponent: () => import('./student/fees/fee-payment.component').then(m => m.FeePaymentComponent), title: 'Fee Payment' },
        ],
      },


      // ── Shared dashboard redirect ──────────────────────────────
      { path: 'dashboard', loadComponent: () => import('./core/shell/role-redirect.component').then(m => m.RoleRedirectComponent) },
      { path: 'profile', loadComponent: () => import('./shared/profile/profile.component').then(m => m.ProfileComponent), title: 'My Profile' },
      { path: 'notifications', loadComponent: () => import('./shared/notifications/notifications-page.component').then(m => m.NotificationsPageComponent), title: 'Notifications' },
      { path: 'chat', loadComponent: () => import('./shared/chat/chat.component').then(m => m.ChatComponent), title: 'Chat' },
    ],
  },

  // Fallback
  { path: '**', redirectTo: 'dashboard' },
];
