import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-payment-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_revenue: 0,
    total_transactions: 0,
    pending_payments: 0,
    completed_payments: 0,
    failed_payments: 0,
    pending_invoices: 0
  };

  recentTransactions: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_revenue: 2456800,
        total_transactions: 1542,
        pending_payments: 87,
        completed_payments: 1432,
        failed_payments: 23,
        pending_invoices: 45
      };

      this.recentTransactions = [
        { id: 'TXN001', student_name: 'Priya Sharma', amount: 45000, status: 'completed', date: new Date() },
        { id: 'TXN002', student_name: 'Rahul Kumar', amount: 32000, status: 'pending', date: new Date() },
        { id: 'TXN003', student_name: 'Sneha Patel', amount: 55000, status: 'completed', date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
  }
}
