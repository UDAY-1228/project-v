import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-applications',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './applications.component.html',
  styleUrls: ['./applications.component.css']
})
export class ApplicationsComponent implements OnInit {
  applications: any[] = [];

  ngOnInit(): void {
    this.loadApplications();
  }

  loadApplications() {
    this.applications = [
      { application_number: 'APP-2026030101', applicant_name: 'Priya Sharma', email: 'priya@example.com', course_applied: 'Computer Science', status: 'pending', submitted_at: new Date() },
      { application_number: 'APP-2026030102', applicant_name: 'Rahul Verma', email: 'rahul@example.com', course_applied: 'Electronics', status: 'approved', submitted_at: new Date() },
      { application_number: 'APP-2026030103', applicant_name: 'Sneha Patel', email: 'sneha@example.com', course_applied: 'Mechanical', status: 'under_review', submitted_at: new Date() },
      { application_number: 'APP-2026030104', applicant_name: 'Amit Kumar', email: 'amit@example.com', course_applied: 'Civil', status: 'rejected', submitted_at: new Date() },
      { application_number: 'APP-2026030105', applicant_name: 'Neha Singh', email: 'neha@example.com', course_applied: 'Computer Science', status: 'pending', submitted_at: new Date() }
    ];
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
