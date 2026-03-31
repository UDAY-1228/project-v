import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  loading = true;
  stats = {
    totalEmployees: 0,
    activeEmployees: 0,
    presentToday: 0,
    onLeave: 0,
    pendingPayroll: 0,
    openPositions: 0,
    newApplications: 0,
    recentHires: 0
  };

  activities: Array<{
    type: string;
    icon: string;
    text: string;
    time: string;
  }> = [];

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadDashboard();
  }

  loadDashboard() {
    this.loading = true;
    this.http.get<any>(`${this.apiUrl}/dashboard/stats`).subscribe({
      next: (data) => {
        this.stats = {
          totalEmployees: data.total_employees || 0,
          activeEmployees: data.active_employees || 0,
          presentToday: data.present_today || 0,
          onLeave: data.on_leave || 0,
          pendingPayroll: data.pending_payroll || 0,
          openPositions: data.open_positions || 0,
          newApplications: data.new_applications || 0,
          recentHires: data.recent_hires || 0
        };
        this.loadRecentActivity();
        this.loading = false;
      },
      error: (err) => {
        console.error('Failed to load dashboard:', err);
        this.loading = false;
      }
    });
  }

  loadRecentActivity() {
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=5`).subscribe({
      next: (employees) => {
        this.activities = employees.slice(0, 5).map((emp: any) => ({
          type: 'employee',
          icon: '👤',
          text: `${emp.first_name} ${emp.last_name} - ${emp.designation}`,
          time: this.formatDate(emp.created_at)
        }));
      },
      error: () => {
        this.activities = [];
      }
    });
  }

  refreshDashboard() {
    this.loadDashboard();
  }

  private formatDate(dateStr: string | undefined): string {
    if (!dateStr) return 'Recently';
    const date = new Date(dateStr);
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const hours = Math.floor(diff / (1000 * 60 * 60));
    if (hours < 1) return 'Just now';
    if (hours < 24) return `${hours}h ago`;
    const days = Math.floor(hours / 24);
    if (days < 7) return `${days}d ago`;
    return date.toLocaleDateString();
  }
}
