import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dc-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_complaints: 0,
    pending_complaints: 0,
    resolved_cases: 0,
    active_cases: 0,
    escalated_cases: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.stats = { total_complaints: 45, pending_complaints: 8, resolved_cases: 32, active_cases: 12, escalated_cases: 3 };
      this.activities = [
        { id: '1', action: 'Case Resolved', actor: 'Committee', module: 'Cases', description: 'Academic misconduct case closed', timestamp: new Date() },
        { id: '2', action: 'New Complaint', actor: 'Student', module: 'Complaints', description: 'Filed against peer harassment', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
