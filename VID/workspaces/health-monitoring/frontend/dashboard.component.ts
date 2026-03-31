import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-health-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_patients: 0,
    total_records: 0,
    pending_alerts: 0,
    critical_alerts: 0,
    reports_generated: 0,
    active_campaigns: 0
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
        total_patients: 245,
        total_records: 128,
        pending_alerts: 5,
        critical_alerts: 1,
        reports_generated: 12,
        active_campaigns: 2
      };

      this.activities = [
        { id: '1', action: 'Checkup Completed', actor: 'Dr. Sharma', module: 'Medical', description: 'Annual health checkup for Class 10 students', timestamp: new Date() },
        { id: '2', action: 'Alert Raised', actor: 'Nurse Kumar', module: 'Alerts', description: 'Critical BMI detected for student S12345', timestamp: new Date() },
        { id: '3', action: 'Report Generated', actor: 'System', module: 'Reports', description: 'Monthly health summary report ready', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
