import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-faculty-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_classes: 0,
    total_students: 0,
    total_assignments: 0,
    pending_assignments: 0,
    upcoming_exams: 0,
    average_attendance: 0
  };

  activities: any[] = [];
  upcomingClasses: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_classes: 6,
        total_students: 180,
        total_assignments: 12,
        pending_assignments: 3,
        upcoming_exams: 2,
        average_attendance: 84.5
      };

      this.activities = [
        { id: '1', action: 'Attendance Marked', actor: 'Dr. Sharma', module: 'Attendance', description: 'Marked attendance for CS301 - Section A', timestamp: new Date() },
        { id: '2', action: 'Assignment Posted', actor: 'Dr. Sharma', module: 'Assignments', description: 'Posted "Database Design Project" for CS302', timestamp: new Date(Date.now() - 3600000) },
        { id: '3', action: 'Exam Scheduled', actor: 'Dr. Sharma', module: 'Exams', description: 'Scheduled Mid-Semester exam for CS301', timestamp: new Date(Date.now() - 7200000) },
        { id: '4', action: 'Results Published', actor: 'Dr. Sharma', module: 'Exams', description: 'Published Quiz 2 results for CS302', timestamp: new Date(Date.now() - 86400000) }
      ];

      this.upcomingClasses = [
        { name: 'CS301 - Data Structures', time: '09:00 AM', room: 'C-201', students: 45 },
        { name: 'CS302 - Database Systems', time: '11:00 AM', room: 'C-202', students: 40 },
        { name: 'CS303 - Algorithms', time: '02:00 PM', room: 'C-203', students: 35 }
      ];

      this.isLoading = false;
    }, 800);
  }

  refreshData() {
    this.isLoading = true;
    this.fetchDashboardData();
  }
}
