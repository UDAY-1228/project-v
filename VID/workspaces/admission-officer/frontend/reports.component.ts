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

  ngOnInit(): void {
    this.reports = [
      { name: 'Admission Summary', type: 'Monthly', generated_at: new Date() },
      { name: 'Course-wise Applications', type: 'Analysis', generated_at: new Date() },
      { name: 'Fee Collection Report', type: 'Financial', generated_at: new Date() },
      { name: 'Document Verification Status', type: 'Compliance', generated_at: new Date() },
      { name: 'Gender Distribution', type: 'Demographics', generated_at: new Date() },
      { name: 'Rejected Applications', type: 'Analysis', generated_at: new Date() }
    ];
  }
}
