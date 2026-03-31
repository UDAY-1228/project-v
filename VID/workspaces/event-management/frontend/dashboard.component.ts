import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_events: 0,
    upcoming_events: 0,
    total_registrations: 0,
    completed_events: 0,
    total_revenue: 0,
    average_attendance: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_events: 18,
        upcoming_events: 4,
        total_registrations: 1250,
        completed_events: 12,
        total_revenue: 45000,
        average_attendance: 85
      };

      this.activities = [
        { id: '1', action: 'Event Published', actor: 'Admin', module: 'Events', description: 'Annual Tech Conference published', timestamp: new Date() },
        { id: '2', action: 'Registration', actor: 'System', module: 'Registrations', description: 'New participant registered', timestamp: new Date() },
        { id: '3', action: 'Event Completed', actor: 'Organizer', module: 'Events', description: 'Workshop successfully completed', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
