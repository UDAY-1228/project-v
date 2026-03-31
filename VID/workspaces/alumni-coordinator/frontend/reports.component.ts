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
        { id: '1', reportName: 'Alumni Directory 2026', reportType: 'Directory', status: 'completed', generatedAt: new Date('2026-03-01') },
        { id: '2', reportName: 'Donation Summary Q1', reportType: 'Financial', status: 'completed', generatedAt: new Date('2026-02-28') },
        { id: '3', reportName: 'Event Attendance Report', reportType: 'Events', status: 'completed', generatedAt: new Date('2026-02-15') },
        { id: '4', reportName: 'Employment Statistics', reportType: 'Analytics', status: 'pending', generatedAt: null },
        { id: '5', reportName: 'Batch-wise Analysis', reportType: 'Analytics', status: 'pending', generatedAt: null }
      ];
      this.isLoading = false;
    }, 500);
  }
}
