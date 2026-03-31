import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-student-transport',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './student-transport.component.html',
  styleUrls: ['./student-transport.component.css']
})
export class StudentTransportComponent implements OnInit {
  students: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.students = [
      { id: '1', student_id: 'STU001', student_name: 'Rahul Sharma', route_name: 'Route A', pickup_point: 'Main Gate', drop_point: 'Campus', is_active: true },
      { id: '2', student_id: 'STU002', student_name: 'Priya Patel', route_name: 'Route B', pickup_point: 'City Center', drop_point: 'Campus', is_active: true },
      { id: '3', student_id: 'STU003', student_name: 'Amit Kumar', route_name: 'Route A', pickup_point: 'Main Gate', drop_point: 'Campus', is_active: false }
    ];
  }
}
