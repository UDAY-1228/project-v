import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Report {
  id: string;
  name: string;
  type: string;
  createdAt: Date;
  status: string;
}

@Component({
  selector: 'app-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  reports: Report[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.reports = [
        { id: '1', name: 'Weekly Performance Report', type: 'performance', createdAt: new Date(), status: 'ready' },
        { id: '2', name: 'API Usage Summary', type: 'usage', createdAt: new Date(Date.now() - 86400000), status: 'ready' },
        { id: '3', name: 'Model Health Report', type: 'health', createdAt: new Date(Date.now() - 172800000), status: 'processing' },
        { id: '4', name: 'Monthly Analytics', type: 'analytics', createdAt: new Date(Date.now() - 604800000), status: 'ready' }
      ];
      this.isLoading = false;
    }, 800);
  }

  generateReport(): void {
    alert('Generate new report...');
  }

  downloadReport(report: Report): void {
    alert(`Downloading ${report.name}...`);
  }

  deleteReport(report: Report): void {
    this.reports = this.reports.filter(r => r.id !== report.id);
  }
}
