import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-revenue-stats',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './revenue-stats.component.html',
  styleUrls: ['./revenue-stats.component.css']
})
export class RevenueStatsComponent implements OnInit {
  monthlyRevenue: any[] = [];
  courseRevenue: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.loadStats();
  }

  loadStats() {
    setTimeout(() => {
      this.monthlyRevenue = [
        { month: 'Jan', revenue: 420000, transactions: 234 },
        { month: 'Feb', revenue: 380000, transactions: 198 },
        { month: 'Mar', revenue: 560000, transactions: 312 },
        { month: 'Apr', revenue: 490000, transactions: 267 },
        { month: 'May', revenue: 610000, transactions: 345 },
        { month: 'Jun', revenue: 580000, transactions: 298 }
      ];
      this.courseRevenue = [
        { course: 'B.Tech CSE', revenue: 1250000, students: 450 },
        { course: 'B.Tech ECE', revenue: 890000, students: 320 },
        { course: 'MBA', revenue: 650000, students: 180 },
        { course: 'B.Sc', revenue: 420000, students: 280 }
      ];
      this.isLoading = false;
    }, 600);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
  }
}
