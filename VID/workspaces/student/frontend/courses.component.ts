import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

interface Course {
  courseId: string;
  courseCode: string;
  courseName: string;
  credits: number;
  department: string;
  semester: number;
  instructorName: string;
  instructorEmail?: string;
  description?: string;
  schedule?: string;
  room?: string;
}

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent implements OnInit {
  courses: Course[] = [];
  selectedSemester: number | null = null;
  availableSemesters: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
  selectedCourse: Course | null = null;
  loading = false;

  private apiBase = '/api/student';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadCourses();
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
    this.loading = true;
    const url = this.selectedSemester
      ? `${this.apiBase}/courses?semester=${this.selectedSemester}`
      : `${this.apiBase}/courses`;

    this.http.get<Course[]>(url, { headers: this.getHeaders() })
      .subscribe({
        next: (courses) => {
          this.courses = courses;
          this.updateAvailableSemesters();
          this.loading = false;
        },
        error: (err) => {
          console.error('Failed to load courses:', err);
          this.loading = false;
        }
      });
  }

  filterBySemester(): void {
    this.loadCourses();
  }

  updateAvailableSemesters(): void {
    const semesters = new Set(this.courses.map(c => c.semester));
    this.availableSemesters = Array.from(semesters).sort((a, b) => a - b);
    if (this.availableSemesters.length === 0) {
      this.availableSemesters = [1, 2, 3, 4, 5, 6, 7, 8];
    }
  }

  viewCourseDetails(course: Course): void {
    this.selectedCourse = course;
  }

  closeModal(): void {
    this.selectedCourse = null;
  }

  viewAttendance(courseId: string): void {
    this.router.navigate(['/attendance'], { queryParams: { courseId } });
  }
}
