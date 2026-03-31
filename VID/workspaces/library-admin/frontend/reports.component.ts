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
      { name: 'Monthly Circulation', type: 'Circulation', generated_at: new Date() },
      { name: 'Overdue Report', type: 'Fines', generated_at: new Date() },
      { name: 'Popular Books', type: 'Statistics', generated_at: new Date() },
      { name: 'Member Activity', type: 'Members', generated_at: new Date() },
      { name: 'Collection Summary', type: 'Inventory', generated_at: new Date() },
      { name: 'Fine Collection', type: 'Financial', generated_at: new Date() }
    ];
  }
}
