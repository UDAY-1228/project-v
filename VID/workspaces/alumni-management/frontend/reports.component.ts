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
        { id: '1', reportName: 'Alumni Growth Report', reportType: 'Analytics', status: 'completed', generatedAt: new Date('2026-03-01') },
        { id: '2', reportName: 'Donation Summary', reportType: 'Financial', status: 'completed', generatedAt: new Date('2026-02-28') },
        { id: '3', reportName: 'Engagement Metrics', reportType: 'Analytics', status: 'pending', generatedAt: null },
        { id: '4', reportName: 'Event Attendance', reportType: 'Events', status: 'completed', generatedAt: new Date('2026-02-15') },
        { id: '5', reportName: 'Donor Analysis', reportType: 'Financial', status: 'pending', generatedAt: null }
      ];
      this.isLoading = false;
    }, 500);
  }
}
