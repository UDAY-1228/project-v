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
    verified_alumni: 0,
    total_donations: 0,
    pending_donations: 0,
    total_events: 0,
    active_reports: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_alumni: 500,
        verified_alumni: 350,
        total_donations: 25,
        pending_donations: 5,
        total_events: 15,
        active_reports: 3
      };

      this.activities = [
        { id: '1', action: 'New Donation', actor: 'Alumni', description: '$500 received from Michael Chen', timestamp: new Date() },
        { id: '2', action: 'Alumni Verified', actor: 'Admin', description: 'Sarah Johnson verified', timestamp: new Date() },
        { id: '3', action: 'Campaign Launched', actor: 'Admin', description: 'Scholarship Fund 2026 started', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
