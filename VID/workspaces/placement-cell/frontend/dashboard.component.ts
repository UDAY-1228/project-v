import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-placement-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_companies: 0,
    active_drives: 0,
    total_applications: 0,
    placed_students: 0,
    pending_applications: 0,
    upcoming_drives: 0
  };

  upcomingDrives: any[] = [];
  recentApplications: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_companies: 45,
        active_drives: 12,
        total_applications: 892,
        placed_students: 156,
        pending_applications: 234,
        upcoming_drives: 8
      };

      this.upcomingDrives = [
        { company: 'TCS', job_title: 'Software Engineer', date: new Date('2026-04-15'), location: 'Campus' },
        { company: 'Infosys', job_title: 'System Engineer', date: new Date('2026-04-18'), location: 'Virtual' },
        { company: 'Wipro', job_title: 'Tech Analyst', date: new Date('2026-04-22'), location: 'Campus' }
      ];

      this.recentApplications = [
        { student_name: 'Priya Sharma', company: 'TCS', status: 'shortlisted', date: new Date() },
        { student_name: 'Rahul Kumar', company: 'Infosys', status: 'pending', date: new Date() },
        { student_name: 'Sneha Patel', company: 'Wipro', status: 'selected', date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
