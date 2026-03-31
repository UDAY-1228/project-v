import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-transport-reports',
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
      { id: '1', report_name: 'Monthly Fleet Usage', report_type: 'fleet', created_at: new Date() },
      { id: '2', report_name: 'Route Analysis', report_type: 'routes', created_at: new Date() },
      { id: '3', report_name: 'Fuel Consumption', report_type: 'fuel', created_at: new Date() }
    ];
  }
}
