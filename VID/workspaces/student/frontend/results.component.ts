import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Result {
  resultId: string;
  courseId: string;
  courseCode: string;
  courseName: string;
  examId?: string;
  examName?: string;
  marksObtained: number;
  totalMarks: number;
  percentage: number;
  grade: string;
  remarks?: string;
  publishedAt: string;
  isFinal: boolean;
}

@Component({
  selector: 'app-results',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  results: Result[] = [];
  cgpa: number | null = null;
  finalizedCount = 0;

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadResults();
    this.loadCgpa();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadResults(): void {
    this.http.get<Result[]>(`${this.apiBase}/results`, { headers: this.getHeaders() })
      .subscribe({
        next: (results) => {
          this.results = results;
          this.finalizedCount = results.filter(r => r.isFinal).length;
        },
        error: (err) => console.error('Failed to load results:', err)
      });
  }

  loadCgpa(): void {
    this.http.get<{ cgpa: number | null }>(`${this.apiBase}/results/cgpa`, { headers: this.getHeaders() })
      .subscribe({
        next: (data) => this.cgpa = data.cgpa,
        error: (err) => console.error('Failed to load CGPA:', err)
      });
  }

  formatDate(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  getGradeClass(grade: string): string {
    const gradeUpper = grade.toUpperCase();
    if (['A+', 'A', 'A-'].includes(gradeUpper)) return 'excellent';
    if (['B+', 'B', 'B-'].includes(gradeUpper)) return 'good';
    if (['C+', 'C', 'C-'].includes(gradeUpper)) return 'average';
    return 'poor';
  }
}
