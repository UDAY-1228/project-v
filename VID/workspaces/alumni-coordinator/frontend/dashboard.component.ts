import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-alumni-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_alumni: 0,
    total_events: 0,
    upcoming_events: 0,
    total_communications: 0,
    active_reports: 0,
    recent_activities: 0
  };

  activities: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_alumni: 245,
        total_events: 12,
        upcoming_events: 3,
        total_communications: 45,
        active_reports: 5,
        recent_activities: 18
      };

      this.activities = [
        { id: '1', action: 'New Alumni Added', actor: 'Coordinator', module: 'Alumni Records', description: 'Sarah Johnson (Class of 2020) registered', timestamp: new Date() },
        { id: '2', action: 'Event Completed', actor: 'System', module: 'Events', description: 'Annual Alumni Meet 2025 concluded', timestamp: new Date() },
        { id: '3', action: 'Newsletter Sent', actor: 'Coordinator', module: 'Communication', description: 'Monthly newsletter dispatched to 200+ alumni', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
