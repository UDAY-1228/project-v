import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-student-stats',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './student-stats.component.html',
  styleUrls: ['./student-stats.component.css']
})
export class StudentStatsComponent implements OnInit {
  courses: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.courses = [
        { name: 'B.Tech CSE', enrolled: 480, passed: 450, failed: 30, gpa: 8.2, placement: 92 },
        { name: 'B.Tech ECE', enrolled: 360, passed: 340, failed: 20, gpa: 7.8, placement: 88 },
        { name: 'B.Tech ME', enrolled: 300, passed: 280, failed: 20, gpa: 7.5, placement: 85 },
        { name: 'B.Tech CE', enrolled: 240, passed: 225, failed: 15, gpa: 7.9, placement: 87 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
