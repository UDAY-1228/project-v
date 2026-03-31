import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-timetable-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class TimetableReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchReports();
  }

  fetchReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', name: 'Weekly Timetable', type: 'schedule', generated: new Date() },
        { id: '2', name: 'Room Utilization', type: 'utilization', generated: new Date() },
      ];
      this.isLoading = false;
    }, 600);
  }

  generateReport(type: string) { console.log('Generating:', type); }
}
