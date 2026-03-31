import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-students',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.css']
})
export class StudentsComponent implements OnInit {
  students: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.students = [
      { id: '1', student_id: 'STU001', student_name: 'Rahul Sharma', room_number: 'A101', department: 'Computer Science', year: 2, status: 'active' },
      { id: '2', student_id: 'STU002', student_name: 'Priya Patel', room_number: 'A102', department: 'Electronics', year: 1, status: 'active' },
      { id: '3', student_id: 'STU003', student_name: 'Amit Kumar', room_number: null, department: 'Mechanical', year: 3, status: 'inactive' }
    ];
  }
}
