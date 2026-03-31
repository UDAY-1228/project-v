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
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.reports = [
        { id: '1', name: 'Annual Faculty Audit', type: 'department-wise', status: 'completed', date: '2024-03-20' },
        { id: '2', name: 'CS Performance Matrix', type: 'academic', status: 'pending', date: '2024-04-10' },
        { id: '3', name: 'Attendance Summary Q1', type: 'attendance', status: 'completed', date: '2024-03-15' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
