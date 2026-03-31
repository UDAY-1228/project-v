import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-hostel-reports',
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
      { id: '1', report_name: 'Monthly Occupancy Report', report_type: 'occupancy', created_at: new Date() },
      { id: '2', report_name: 'Fee Collection Summary', report_type: 'fees', created_at: new Date() },
      { id: '3', report_name: 'Complaint Analysis', report_type: 'complaints', created_at: new Date() }
    ];
  }
}
