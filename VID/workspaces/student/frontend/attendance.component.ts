import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

interface Course {
  courseId: string;
  courseCode: string;
  courseName: string;
}

interface AttendanceRecord {
  attendanceId: string;
  courseId: string;
  courseCode: string;
  date: string;
  status: string;
  remarks?: string;
}

interface AttendanceSummary {
  totalClasses: number;
  present: number;
  absent: number;
  late: number;
  excused: number;
  percentage: number;
}

@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  courses: Course[] = [];
  attendanceRecords: AttendanceRecord[] = [];
  selectedCourseId: string | null = null;
  startDate: string = '';
  endDate: string = '';
  
  summary: AttendanceSummary = {
    totalClasses: 0,
    present: 0,
    absent: 0,
    late: 0,
    excused: 0,
    percentage: 0
  };

  private apiBase = '/api/student';

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      if (params['courseId']) {
        this.selectedCourseId = params['courseId'];
      }
    });
    this.loadCourses();
    this.loadAttendance();
    this.loadSummary();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadCourses(): void {
    this.http.get<Course[]>(`${this.apiBase}/courses`, { headers: this.getHeaders() })
      .subscribe({
        next: (courses) => this.courses = courses,
        error: (err) => console.error('Failed to load courses:', err)
      });
  }

  loadAttendance(): void {
    let url = `${this.apiBase}/attendance`;
    const params: string[] = [];
    
    if (this.selectedCourseId) {
      params.push(`courseId=${this.selectedCourseId}`);
    }
    if (this.startDate) {
      params.push(`startDate=${this.startDate}`);
    }
    if (this.endDate) {
      params.push(`endDate=${this.endDate}`);
    }
    
    if (params.length > 0) {
      url += '?' + params.join('&');
    }

    this.http.get<AttendanceRecord[]>(url, { headers: this.getHeaders() })
      .subscribe({
        next: (records) => this.attendanceRecords = records,
        error: (err) => console.error('Failed to load attendance:', err)
      });
  }

  loadSummary(): void {
    let url = `${this.apiBase}/attendance/summary`;
    if (this.selectedCourseId) {
      url += `?courseId=${this.selectedCourseId}`;
    }

    this.http.get<AttendanceSummary>(url, { headers: this.getHeaders() })
      .subscribe({
        next: (summary) => this.summary = summary,
        error: (err) => console.error('Failed to load summary:', err)
      });
  }

  filterByCourse(): void {
    this.loadAttendance();
    this.loadSummary();
  }

  filterByDate(): void {
    this.loadAttendance();
  }

  formatDate(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }
}
