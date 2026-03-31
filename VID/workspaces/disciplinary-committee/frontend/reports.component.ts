import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dc-reports',
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
        { id: '1', name: 'Monthly Case Summary', type: 'monthly', date: new Date() },
        { id: '2', name: 'Annual Disciplinary Report', type: 'annual', date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
