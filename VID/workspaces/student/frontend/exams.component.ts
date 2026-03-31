import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Exam {
  examId: string;
  examName: string;
  courseId: string;
  courseCode: string;
  courseName: string;
  examType: string;
  date: string;
  startTime: string;
  endTime: string;
  durationMinutes: number;
  venue: string;
  totalMarks: number;
  status: string;
  instructions?: string;
}

@Component({
  selector: 'app-exams',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './exams.component.html',
  styleUrls: ['./exams.component.css']
})
export class ExamsComponent implements OnInit {
  exams: Exam[] = [];
  selectedStatus: string | null = null;
  selectedExam: Exam | null = null;

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadExams();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadExams(): void {
    let url = `${this.apiBase}/exams`;
    if (this.selectedStatus) {
      url += `?status=${this.selectedStatus}`;
    }

    this.http.get<Exam[]>(url, { headers: this.getHeaders() })
      .subscribe({
        next: (exams) => this.exams = exams,
        error: (err) => console.error('Failed to load exams:', err)
      });
  }

  filterByStatus(): void {
    this.loadExams();
  }

  formatDate(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  viewExamDetails(exam: Exam): void {
    this.selectedExam = exam;
  }

  registerForExam(exam: Exam): void {
    this.http.post(`${this.apiBase}/exams/${exam.examId}/register`, {}, { headers: this.getHeaders() })
      .subscribe({
        next: () => {
          alert('Successfully registered for exam!');
          this.closeModal();
        },
        error: (err) => {
          console.error('Failed to register:', err);
          alert('Registration failed. You may already be registered.');
        }
      });
  }

  closeModal(): void {
    this.selectedExam = null;
  }
}
