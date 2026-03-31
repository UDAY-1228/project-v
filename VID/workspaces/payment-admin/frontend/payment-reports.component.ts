import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-payment-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './payment-reports.component.html',
  styleUrls: ['./payment-reports.component.css']
})
export class PaymentReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.loadReports();
  }

  loadReports() {
    setTimeout(() => {
      this.reports = [
        { id: 'RPT001', report_name: 'Monthly Collection Report', report_type: 'monthly', total_amount: 2456800, total_transactions: 1542, created_at: new Date() },
        { id: 'RPT002', report_name: 'Course-wise Revenue', report_type: 'course', total_amount: 1890000, total_transactions: 892, created_at: new Date() },
        { id: 'RPT003', report_name: 'Pending Payments Summary', report_type: 'pending', total_amount: 456000, total_transactions: 87, created_at: new Date() }
      ];
      this.isLoading = false;
    }, 600);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
  }
}
