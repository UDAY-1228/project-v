import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-academic-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_courses: 0,
    total_subjects: 0,
    total_assessments: 0,
    active_timetables: 0,
    pending_reports: 0,
    unread_notices: 0
  };

  activities: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    // Mock data fetching to match premium UI feel
    setTimeout(() => {
      this.stats = {
        total_courses: 12,
        total_subjects: 45,
        total_assessments: 8,
        active_timetables: 4,
        pending_reports: 2,
        unread_notices: 3
      };

      this.activities = [
        { id: '1', action: 'Course Updated', actor: 'Dr. Smith', module: 'Courses', description: 'Updated syllabus for CS101', timestamp: new Date() },
        { id: '2', action: 'New Notice', actor: 'Admin', module: 'Notice Board', description: 'Exam schedule posted', timestamp: new Date() },
        { id: '3', action: 'Timetable Generated', actor: 'System', module: 'Timetable', description: 'Semester 1 timetable finalized', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
