import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-reports',
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
        { id: '1', name: 'Event Attendance Report', type: 'attendance', date: new Date(), status: 'completed' },
        { id: '2', name: 'Revenue Analysis Q1', type: 'revenue', date: new Date(), status: 'pending' },
        { id: '3', name: 'Registration Summary', type: 'registration', date: new Date(), status: 'completed' },
      ];
      this.isLoading = false;
    }, 800);
  }
}
