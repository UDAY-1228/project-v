import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-analytics',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit {
  isLoading = true;
  timeRange = '7d';
  
  metrics = [
    { label: 'Total API Calls', value: 1247, change: 12.5, trend: 'up' },
    { label: 'Success Rate', value: 99.2, change: 0.3, trend: 'up', suffix: '%' },
    { label: 'Avg Response Time', value: 245, change: -8.2, trend: 'down', suffix: 'ms' },
    { label: 'Active Models', value: 5, change: 0, trend: 'neutral' }
  ];

  chartData: number[] = [65, 78, 72, 85, 82, 90, 88, 95, 92, 98, 94, 100];

  ngOnInit(): void {
    setTimeout(() => { this.isLoading = false; }, 800);
  }
}
