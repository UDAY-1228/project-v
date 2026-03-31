import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-timetable-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class TimetableDashboardComponent implements OnInit {
  stats = {
    total_timetables: 0,
    active_timetables: 0,
    total_classes: 0,
    total_rooms: 0,
    total_faculty: 0,
    pending_allocations: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_timetables: 15,
        active_timetables: 12,
        total_classes: 45,
        total_rooms: 30,
        total_faculty: 80,
        pending_allocations: 5
      };
      this.activities = [
        { id: '1', action: 'Timetable Published', actor: 'Dr. Kumar', module: 'Schedule', description: 'Semester 5 timetable published', timestamp: new Date() },
        { id: '2', action: 'Room Allocated', actor: 'Admin', module: 'Room Allocation', description: 'Lab 3 allocated to CS department', timestamp: new Date() },
        { id: '3', action: 'Class Added', actor: 'System', module: 'Class Allocation', description: 'New section created for B.Sc', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
