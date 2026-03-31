import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-examination-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class ExaminationDashboardComponent implements OnInit {
  stats = {
    total_exams: 0,
    upcoming_exams: 0,
    completed_exams: 0,
    total_students: 0,
    hall_capacity: 0,
    pending_results: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_exams: 24,
        upcoming_exams: 8,
        completed_exams: 16,
        total_students: 1250,
        hall_capacity: 1800,
        pending_results: 5
      };

      this.activities = [
        { id: '1', action: 'Exam Scheduled', actor: 'Dr. Sharma', module: 'Exam Schedule', description: 'Mid-semester exams scheduled for October', timestamp: new Date() },
        { id: '2', action: 'Results Published', actor: 'Exam Cell', module: 'Results', description: 'Semester 1 results uploaded', timestamp: new Date() },
        { id: '3', action: 'Hall Tickets Issued', actor: 'Admin', module: 'Hall Tickets', description: '500 hall tickets generated', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
