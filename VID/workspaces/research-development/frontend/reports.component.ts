import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-rd-reports',
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
        { id: '1', name: 'Annual Research Report 2024', type: 'annual', date: new Date() },
        { id: '2', name: 'Publication Analytics Q4', type: 'quarterly', date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
