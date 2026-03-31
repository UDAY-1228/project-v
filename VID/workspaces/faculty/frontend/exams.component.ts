import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-exams',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './exams.component.html',
  styleUrls: ['./exams.component.css']
})
export class ExamsComponent implements OnInit {
  exams: any[] = [];
  filteredExams: any[] = [];
  selectedType: string = 'all';
  searchQuery: string = '';
  isLoading = true;
  showCreateModal = false;
  showResultsModal = false;
  selectedExam: any = null;
  results: any[] = [];

  newExam = {
    exam_name: '',
    exam_type: 'mid_semester',
    subject_name: 'Data Structures',
    total_marks: 100,
    passing_marks: 40,
    exam_date: '',
    duration_minutes: 60,
    start_time: '09:00',
    venue: ''
  };

  examTypes = [
    { value: 'quiz', label: 'Quiz' },
    { value: 'class_test', label: 'Class Test' },
    { value: 'mid_semester', label: 'Mid-Semester' },
    { value: 'end_semester', label: 'End-Semester' },
    { value: 'practical', label: 'Practical' },
    { value: 'assignment', label: 'Assignment' }
  ];

  ngOnInit(): void {
    this.fetchExams();
  }

  fetchExams() {
    setTimeout(() => {
      this.exams = [
        { id: '1', exam_name: 'Mid-Semester Examination', exam_type: 'mid_semester', subject_name: 'Data Structures', total_marks: 100, passing_marks: 40, exam_date: '2026-04-20', duration_minutes: 180, start_time: '09:00', venue: 'Main Hall', total_students: 45, evaluated_count: 0, status: 'scheduled' },
        { id: '2', exam_name: 'Quiz 3 - Trees and Graphs', exam_type: 'quiz', subject_name: 'Data Structures', total_marks: 30, passing_marks: 12, exam_date: '2026-04-10', duration_minutes: 45, start_time: '14:00', venue: 'C-201', total_students: 45, evaluated_count: 45, average_score: 24.5, status: 'completed' },
        { id: '3', exam_name: 'Database Design Test', exam_type: 'class_test', subject_name: 'Database Systems', total_marks: 50, passing_marks: 20, exam_date: '2026-04-15', duration_minutes: 60, start_time: '11:00', venue: 'C-202', total_students: 40, evaluated_count: 0, status: 'scheduled' },
        { id: '4', exam_name: 'Practical Exam - SQL Queries', exam_type: 'practical', subject_name: 'Database Systems', total_marks: 50, passing_marks: 25, exam_date: '2026-03-25', duration_minutes: 90, start_time: '10:00', venue: 'Lab 1', total_students: 40, evaluated_count: 40, average_score: 38.2, status: 'completed' }
      ];
      this.applyFilters();
      this.isLoading = false;
    }, 800);
  }

  applyFilters() {
    let filtered = [...this.exams];
    if (this.selectedType !== 'all') {
      filtered = filtered.filter(e => e.exam_type === this.selectedType);
    }
    if (this.searchQuery) {
      const query = this.searchQuery.toLowerCase();
      filtered = filtered.filter(e => e.exam_name.toLowerCase().includes(query) || e.subject_name.toLowerCase().includes(query));
    }
    this.filteredExams = filtered;
  }

  openCreateModal() {
    this.showCreateModal = true;
  }

  closeCreateModal() {
    this.showCreateModal = false;
  }

  createExam() {
    const newData = {
      ...this.newExam,
      id: Date.now().toString(),
      total_students: 0,
      evaluated_count: 0,
      status: 'scheduled'
    };
    this.exams.unshift(newData);
    this.applyFilters();
    this.closeCreateModal();
  }

  viewResults(exam: any) {
    this.selectedExam = exam;
    this.results = [
      { student_id: 'STU001', student_name: 'Amit Kumar', roll_number: 'CS301001', marks_obtained: 85, percentage: 85, grade: 'A' },
      { student_id: 'STU002', student_name: 'Priya Sharma', roll_number: 'CS301002', marks_obtained: 78, percentage: 78, grade: 'A' },
      { student_id: 'STU003', student_name: 'Rahul Verma', roll_number: 'CS301003', marks_obtained: 62, percentage: 62, grade: 'B' },
      { student_id: 'STU004', student_name: 'Sneha Patel', roll_number: 'CS301004', marks_obtained: 92, percentage: 92, grade: 'O' }
    ];
    this.showResultsModal = true;
  }

  closeResultsModal() {
    this.showResultsModal = false;
  }

  getStatusColor(status: string) {
    switch(status) {
      case 'scheduled': return 'bg-amber-500/10 text-amber-400';
      case 'completed': return 'bg-emerald-500/10 text-emerald-400';
      default: return 'bg-zinc-500/10 text-zinc-400';
    }
  }

  getGradeColor(grade: string) {
    if (grade === 'O' || grade === 'A+' || grade === 'A') return 'text-emerald-400';
    if (grade === 'B+' || grade === 'B') return 'text-blue-400';
    return 'text-amber-400';
  }
}
