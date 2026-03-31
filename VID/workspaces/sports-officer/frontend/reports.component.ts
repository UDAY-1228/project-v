import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sports-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadReports();
  }

  loadReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', name: 'Monthly Performance Report', type: 'performance', date: new Date(), status: 'completed' },
        { id: '2', name: 'Tournament Summary Q1', type: 'summary', date: new Date(), status: 'pending' },
        { id: '3', name: 'Team Statistics Report', type: 'statistics', date: new Date(), status: 'completed' },
      ];
      this.isLoading = false;
    }, 800);
  }
}
