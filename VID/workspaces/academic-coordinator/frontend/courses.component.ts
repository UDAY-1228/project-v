import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent implements OnInit {
  courses: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.courses = [
        { id: '1', name: 'Computer Science & Engineering', code: 'CSE-001', dept: 'CS', duration: 4, type: 'UG' },
        { id: '2', name: 'Electronics & Communication', code: 'ECE-002', dept: 'ECE', duration: 4, type: 'UG' },
        { id: '3', name: 'Information Systems', code: 'IS-105', dept: 'CS', duration: 2, type: 'PG' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
