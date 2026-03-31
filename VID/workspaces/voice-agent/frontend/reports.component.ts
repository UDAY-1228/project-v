import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadReports();
  }

  loadReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', report_name: 'Weekly Usage Report', report_type: 'usage', date_range: 'Mar 24 - Mar 30, 2026', generated_by: 'System', status: 'completed', summary: { total_interactions: 2340, success_rate: 94.2 } },
        { id: '2', report_name: 'Performance Analysis', report_type: 'performance', date_range: 'Mar 17 - Mar 23, 2026', generated_by: 'Admin', status: 'completed', summary: { avg_response_time: 245, uptime: 99.8 } },
        { id: '3', report_name: 'Error Analysis', report_type: 'errors', date_range: 'Mar 24 - Mar 30, 2026', generated_by: 'System', status: 'completed', summary: { total_errors: 45, critical: 3 } },
        { id: '4', report_name: 'Monthly Usage Report', report_type: 'usage', date_range: 'Mar 1 - Mar 31, 2026', generated_by: 'System', status: 'pending', summary: null },
        { id: '5', report_name: 'User Behavior Analysis', report_type: 'usage', date_range: 'Feb 1 - Feb 28, 2026', generated_by: 'Admin', status: 'completed', summary: { total_users: 890, active_users: 567 } }
      ];
      this.isLoading = false;
    }, 600);
  }

  getStatusColor(status: string): string {
    return status === 'completed' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400';
  }

  getTypeIcon(type: string): string {
    return 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z';
  }
}
