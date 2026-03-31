import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-student-progress',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './student-progress.component.html',
  styleUrls: ['./student-progress.component.css']
})
export class StudentProgressComponent implements OnInit {
  subjects = [
    { name: 'Mathematics', percentage: 95 },
    { name: 'Science', percentage: 90 },
    { name: 'English', percentage: 88 },
    { name: 'Social Studies', percentage: 92 },
    { name: 'Computer Science', percentage: 98 }
  ];

  exams = [
    { name: 'Unit Test 1', date: new Date('2026-02-15'), marks: 95 },
    { name: 'Mid Term', date: new Date('2026-02-28'), marks: 90 },
    { name: 'Unit Test 2', date: new Date('2026-03-10'), marks: 92 }
  ];

  ngOnInit(): void {}
}
