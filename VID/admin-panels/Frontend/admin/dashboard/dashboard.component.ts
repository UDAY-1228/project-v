import { Component } from '@angular/core';

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  institutionOverview = { total_users: 154, active_workspaces: 8 };
  trendingAnalytics = [
    { label: 'Active Users', value: 85 },
    { label: 'Workspace Usage', value: 92 }
  ];
  recentOperations = [
    { type: 'USER_CREATED', user: 'admin1', timestamp: '2024-03-31T08:00:00Z' },
    { type: 'WORKSPACE_ASSIGNED', user: 'fac_12', timestamp: '2024-03-31T07:45:00Z' }
  ];
  logout() {
    console.log('Logging out of Admin Panel...');
  }
}
