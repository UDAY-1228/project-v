import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_tasks: 0,
    completed_tasks: 0,
    pending_leaves: 0,
    attendance_rate: 0,
    upcoming_events: 0,
    total_hours_worked: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_tasks: 15,
        completed_tasks: 8,
        pending_leaves: 2,
        attendance_rate: 95.5,
        upcoming_events: 3,
        total_hours_worked: 160
      };

      this.activities = [
        { id: '1', action: 'Task Completed', actor: 'John Doe', module: 'Tasks', description: 'Monthly report submitted', timestamp: new Date() },
        { id: '2', action: 'Leave Approved', actor: 'Manager', module: 'Leave', description: 'Vacation request approved', timestamp: new Date() },
        { id: '3', action: 'Attendance', actor: 'System', module: 'Attendance', description: 'Checked in at 9:00 AM', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
