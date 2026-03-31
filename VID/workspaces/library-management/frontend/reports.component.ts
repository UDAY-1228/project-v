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
      { name: 'Catalog Inventory', type: 'Inventory', generated_at: new Date() },
      { name: 'Circulation Summary', type: 'Circulation', generated_at: new Date() },
      { name: 'Member Statistics', type: 'Members', generated_at: new Date() },
      { name: 'Popular Books', type: 'Analytics', generated_at: new Date() },
      { name: 'Overdue Report', type: 'Fines', generated_at: new Date() },
      { name: 'Acquisition Report', type: 'Inventory', generated_at: new Date() }
    ];
  }
}
