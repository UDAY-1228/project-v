import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-parent-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_students: 0,
    average_attendance: 0,
    pending_fees: 0,
    upcoming_events: 0,
    unread_notifications: 0,
    recent_activities: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_students: 2,
        average_attendance: 92,
        pending_fees: 1,
        upcoming_events: 2,
        unread_notifications: 5,
        recent_activities: 8
      };

      this.activities = [
        { id: '1', studentName: 'John', description: 'Scored 95% in Mathematics exam', timestamp: new Date() },
        { id: '2', studentName: 'John', description: 'Attendance marked present today', timestamp: new Date() },
        { id: '3', studentName: 'Sarah', description: 'New assignment posted in Science', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
