import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-team-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class TeamReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchReports();
  }

  fetchReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', name: 'Member Activity', type: 'activity', generated: new Date() },
        { id: '2', name: 'Access Audit', type: 'audit', generated: new Date() },
        { id: '3', name: 'Workspace Summary', type: 'summary', generated: new Date() },
      ];
      this.isLoading = false;
    }, 600);
  }

  generateReport(type: string) { console.log('Generating:', type); }
}
