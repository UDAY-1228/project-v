import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-rd-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = { total_projects: 0, active_projects: 0, completed_projects: 0, total_publications: 0, total_grants: 0 };
  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.stats = { total_projects: 28, active_projects: 15, completed_projects: 13, total_publications: 145, total_grants: 22 };
      this.activities = [
        { action: 'Paper Published', actor: 'Dr. Kumar', module: 'Publications', description: 'IEEE Access impact factor 3.2', timestamp: new Date() },
        { action: 'Grant Approved', actor: 'Dr. Sharma', module: 'Grants', description: 'DST funding 50L', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
