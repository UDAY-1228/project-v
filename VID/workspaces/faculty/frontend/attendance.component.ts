import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  classes: any[] = [];
  selectedClass: any = null;
  students: any[] = [];
  attendanceDate: string = new Date().toISOString().split('T')[0];
  isLoading = false;
  showMarkAttendance = false;
  viewMode: 'list' | 'summary' = 'list';

  attendanceSummary: any[] = [];

  ngOnInit(): void {
    this.fetchClasses();
  }

  fetchClasses() {
    setTimeout(() => {
      this.classes = [
        { id: '1', class_name: 'CS301 - Data Structures', section: 'A', total_students: 45 },
        { id: '2', class_name: 'CS302 - Database Systems', section: 'A', total_students: 40 },
        { id: '3', class_name: 'CS303 - Algorithms', section: 'B', total_students: 38 }
      ];
    }, 500);
  }

  selectClass(classItem: any) {
    this.selectedClass = classItem;
    this.fetchStudents(classItem.id);
  }

  fetchStudents(classId: string) {
    this.isLoading = true;
    setTimeout(() => {
      this.students = [
        { id: 's1', student_id: 'STU001', first_name: 'Amit', last_name: 'Kumar', roll_number: 'CS301001', status: 'present' },
        { id: 's2', student_id: 'STU002', first_name: 'Priya', last_name: 'Sharma', roll_number: 'CS301002', status: 'present' },
        { id: 's3', student_id: 'STU003', first_name: 'Rahul', last_name: 'Verma', roll_number: 'CS301003', status: 'absent' },
        { id: 's4', student_id: 'STU004', first_name: 'Sneha', last_name: 'Patel', roll_number: 'CS301004', status: 'present' },
        { id: 's5', student_id: 'STU005', first_name: 'Vikram', last_name: 'Singh', roll_number: 'CS301005', status: 'late' },
        { id: 's6', student_id: 'STU006', first_name: 'Anita', last_name: 'Reddy', roll_number: 'CS301006', status: 'present' },
        { id: 's7', student_id: 'STU007', first_name: 'Rajesh', last_name: 'Gupta', roll_number: 'CS301007', status: 'present' },
        { id: 's8', student_id: 'STU008', first_name: 'Meera', last_name: 'Joshi', roll_number: 'CS301008', status: 'excused' }
      ];
      this.isLoading = false;
    }, 600);
  }

  openMarkAttendance() {
    this.showMarkAttendance = true;
  }

  closeMarkAttendance() {
    this.showMarkAttendance = false;
  }

  markAllPresent() {
    this.students.forEach(s => s.status = 'present');
  }

  markAllAbsent() {
    this.students.forEach(s => s.status = 'absent');
  }

  setStatus(student: any, status: string) {
    student.status = status;
  }

  saveAttendance() {
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      this.showMarkAttendance = false;
      alert('Attendance saved successfully!');
    }, 800);
  }

  toggleView(mode: 'list' | 'summary') {
    this.viewMode = mode;
    if (mode === 'summary') {
      this.fetchAttendanceSummary();
    }
  }

  fetchAttendanceSummary() {
    this.attendanceSummary = this.students.map(s => ({
      ...s,
      total_classes: 24,
      classes_attended: Math.floor(Math.random() * 10) + 15,
      percentage: 0
    })).map(s => ({
      ...s,
      percentage: Math.round((s.classes_attended / s.total_classes) * 100)
    }));
  }
}
