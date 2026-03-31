import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-health-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  reports: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.reports = [
      { id: '1', report_name: 'Monthly Health Summary', report_type: 'summary', created_at: new Date() },
      { id: '2', report_name: 'Annual Checkup Data', report_type: 'annual', created_at: new Date() },
      { id: '3', report_name: 'Vaccination Status', report_type: 'vaccination', created_at: new Date() }
    ];
  }
}
