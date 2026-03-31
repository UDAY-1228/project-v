import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface DashboardData {
  studentName: string;
  studentId: string;
  department: string;
  semester: number;
  currentCgpa: number | null;
  attendancePercentage: number;
  totalNotifications: number;
  unreadNotifications: number;
  upcomingExams: number;
  pendingFees: number;
  enrolledCourses: number;
  completedCourses: number;
}

interface AttendanceSummary {
  totalClasses: number;
  present: number;
  absent: number;
  late: number;
  excused: number;
  percentage: number;
}

interface Course {
  courseId: string;
  courseCode: string;
  courseName: string;
  credits: number;
  instructorName: string;
  attendancePercentage?: number;
}

interface Notification {
  notificationId: string;
  title: string;
  message: string;
  type: string;
  isRead: boolean;
  sentAt: string;
}

interface Exam {
  examId: string;
  examName: string;
  courseName: string;
  date: string;
  startTime: string;
  endTime: string;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  studentName = '';
  studentId = '';
  department = '';
  semester = 1;
  currentCgpa: number | null = null;
  attendancePercentage = 0;
  upcomingExams = 0;
  pendingFees = 0;
  enrolledCourses = 0;
  completedCourses = 0;
  
  enrolledCoursesList: Course[] = [];
  recentNotifications: Notification[] = [];
  examList: Exam[] = [];
  attendanceData: AttendanceSummary = {
    totalClasses: 0,
    present: 0,
    absent: 0,
    late: 0,
    excused: 0,
    percentage: 0
  };

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.studentId = this.getStudentId();
    this.loadDashboardData();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.studentId
    });
  }

  loadDashboardData(): void {
    this.http.get<DashboardData>(`${this.apiBase}/dashboard`, { headers: this.getHeaders() })
      .subscribe({
        next: (data) => {
          this.studentName = data.studentName;
          this.studentId = data.studentId;
          this.department = data.department;
          this.semester = data.semester;
          this.currentCgpa = data.currentCgpa;
          this.attendancePercentage = data.attendancePercentage;
          this.upcomingExams = data.upcomingExams;
          this.pendingFees = data.pendingFees;
          this.enrolledCourses = data.enrolledCourses;
          this.completedCourses = data.completedCourses;
        },
        error: (err) => console.error('Failed to load dashboard:', err)
      });

    this.loadEnrolledCourses();
    this.loadNotifications();
    this.loadUpcomingExams();
    this.loadAttendanceSummary();
  }

  loadEnrolledCourses(): void {
    this.http.get<Course[]>(`${this.apiBase}/courses/enrolled`, { headers: this.getHeaders() })
      .subscribe({
        next: (courses) => this.enrolledCoursesList = courses,
        error: (err) => console.error('Failed to load courses:', err)
      });
  }

  loadNotifications(): void {
    this.http.get<Notification[]>(`${this.apiBase}/notifications?limit=5`, { headers: this.getHeaders() })
      .subscribe({
        next: (notifications) => this.recentNotifications = notifications,
        error: (err) => console.error('Failed to load notifications:', err)
      });
  }

  loadUpcomingExams(): void {
    this.http.get<Exam[]>(`${this.apiBase}/exams/upcoming?limit=3`, { headers: this.getHeaders() })
      .subscribe({
        next: (exams) => this.examList = exams,
        error: (err) => console.error('Failed to load exams:', err)
      });
  }

  loadAttendanceSummary(): void {
    this.http.get<AttendanceSummary>(`${this.apiBase}/attendance/summary`, { headers: this.getHeaders() })
      .subscribe({
        next: (summary) => this.attendanceData = summary,
        error: (err) => console.error('Failed to load attendance:', err)
      });
  }

  refreshDashboard(): void {
    this.loadDashboardData();
  }

  getNotificationIcon(type: string): string {
    const icons: Record<string, string> = {
      'general': '📢',
      'academic': '📚',
      'fee': '💰',
      'event': '🎉',
      'attendance': '📋',
      'exam': '📝',
      'result': '🎓'
    };
    return icons[type] || '📢';
  }

  formatTime(dateStr: string): string {
    const date = new Date(dateStr);
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const hours = Math.floor(diff / (1000 * 60 * 60));
    if (hours < 1) return 'Just now';
    if (hours < 24) return `${hours}h ago`;
    const days = Math.floor(hours / 24);
    if (days < 7) return `${days}d ago`;
    return date.toLocaleDateString();
  }

  viewNotification(notification: Notification): void {
    if (!notification.isRead) {
      this.http.put(`${this.apiBase}/notifications/${notification.notificationId}/read`, {})
        .subscribe(() => {
          notification.isRead = true;
        });
    }
  }

  getExamDay(dateStr: string): string {
    const date = new Date(dateStr);
    return date.getDate().toString();
  }

  getExamMonth(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleString('default', { month: 'short' });
  }
}
