import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-pd-reports',
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
        { id: '1', name: 'Annual Performance Report', type: 'annual', date: new Date(), status: 'completed' },
        { id: '2', name: 'Staff Analytics Q4', type: 'quarterly', date: new Date(), status: 'pending' },
        { id: '3', name: 'Student Enrollment Summary', type: 'semester', date: new Date(), status: 'completed' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
