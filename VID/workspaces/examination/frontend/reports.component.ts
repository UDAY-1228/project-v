import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-examination-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ExaminationReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchReports();
  }

  fetchReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', report_name: 'Mid-Term Analysis', report_type: 'analysis', generated_by: 'System', created_at: new Date() },
        { id: '2', report_name: 'Result Summary', report_type: 'summary', generated_by: 'Admin', created_at: new Date() },
      ];
      this.isLoading = false;
    }, 600);
  }

  generateReport(type: string) { console.log('Generating:', type); }
}
