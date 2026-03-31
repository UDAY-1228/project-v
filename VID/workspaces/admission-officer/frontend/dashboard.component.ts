import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-admission-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_applications: 0,
    pending_applications: 0,
    approved_applications: 0,
    rejected_applications: 0,
    total_admissions: 0,
    verified_documents: 0
  };

  applications: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_applications: 156,
        pending_applications: 42,
        approved_applications: 98,
        rejected_applications: 16,
        total_admissions: 89,
        verified_documents: 134
      };

      this.applications = [
        { id: '1', applicant_name: 'Priya Sharma', course_applied: 'Computer Science', status: 'pending', submitted_at: new Date() },
        { id: '2', applicant_name: 'Rahul Verma', course_applied: 'Electronics', status: 'approved', submitted_at: new Date() },
        { id: '3', applicant_name: 'Sneha Patel', course_applied: 'Mechanical', status: 'pending', submitted_at: new Date() },
        { id: '4', applicant_name: 'Amit Kumar', course_applied: 'Civil', status: 'under_review', submitted_at: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }

  getStatusClass(status: string): string {
    const statusClasses: Record<string, string> = {
      'pending': 'bg-amber-500/20 text-amber-400',
      'approved': 'bg-emerald-500/20 text-emerald-400',
      'rejected': 'bg-red-500/20 text-red-400',
      'under_review': 'bg-blue-500/20 text-blue-400'
    };
    return statusClasses[status] || 'bg-zinc-500/20 text-zinc-400';
  }
}
