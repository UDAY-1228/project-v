import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-student-admissions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './student-admissions.component.html',
  styleUrls: ['./student-admissions.component.css']
})
export class StudentAdmissionsComponent implements OnInit {
  stats = { total_admissions: 89, monthly_admissions: 15, fees_paid: 72, pending: 17 };
  students: any[] = [];

  ngOnInit(): void {
    this.students = [
      { admission_number: 'ADM-2026030101', student_name: 'Priya Sharma', course: 'Computer Science', batch: '2026', status: 'active' },
      { admission_number: 'ADM-2026030102', student_name: 'Rahul Verma', course: 'Electronics', batch: '2026', status: 'active' },
      { admission_number: 'ADM-2026030103', student_name: 'Sneha Patel', course: 'Mechanical', batch: '2026', status: 'active' },
      { admission_number: 'ADM-2026030104', student_name: 'Amit Kumar', course: 'Civil', batch: '2026', status: 'active' }
    ];
  }
}
