import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-principal-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_students: 0,
    total_staff: 0,
    total_departments: 0,
    total_courses: 0,
    pending_approvals: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_students: 2500,
        total_staff: 320,
        total_departments: 12,
        total_courses: 48,
        pending_approvals: 5
      };

      this.activities = [
        { id: '1', action: 'Policy Approved', actor: 'Board', module: 'Policies', description: 'New attendance policy approved', timestamp: new Date() },
        { id: '2', action: 'Staff Review', actor: 'HR', module: 'Staff Stats', description: 'Q4 performance review completed', timestamp: new Date() },
        { id: '3', action: 'Report Generated', actor: 'System', module: 'Reports', description: 'Annual institutional report ready', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
