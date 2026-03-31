import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface FeeRecord {
  feeId: string;
  feeType: string;
  amount: number;
  paidAmount: number;
  dueDate: string;
  paidDate?: string;
  status: string;
  academicYear: string;
  semester: number;
  description?: string;
  paymentMethod?: string;
  transactionId?: string;
}

interface FeeSummary {
  totalFees: number;
  totalPaid: number;
  totalPending: number;
  overdueAmount: number;
}

@Component({
  selector: 'app-fee-status',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './fee-status.component.html',
  styleUrls: ['./fee-status.component.css']
})
export class FeeStatusComponent implements OnInit {
  fees: FeeRecord[] = [];
  selectedStatus: string | null = null;
  selectedFee: FeeRecord | null = null;
  paymentAmount = 0;
  paymentMethod = 'card';

  summary: FeeSummary = {
    totalFees: 0,
    totalPaid: 0,
    totalPending: 0,
    overdueAmount: 0
  };

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadFees();
    this.loadSummary();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadFees(): void {
    let url = `${this.apiBase}/fees`;
    if (this.selectedStatus) {
      url += `?status=${this.selectedStatus}`;
    }

    this.http.get<FeeRecord[]>(url, { headers: this.getHeaders() })
      .subscribe({
        next: (fees) => this.fees = fees,
        error: (err) => console.error('Failed to load fees:', err)
      });
  }

  loadSummary(): void {
    this.http.get<FeeSummary>(`${this.apiBase}/fees/summary`, { headers: this.getHeaders() })
      .subscribe({
        next: (summary) => this.summary = summary,
        error: (err) => console.error('Failed to load summary:', err)
      });
  }

  filterByStatus(): void {
    this.loadFees();
  }

  formatDate(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  isOverdue(fee: FeeRecord): boolean {
    const today = new Date();
    const dueDate = new Date(fee.dueDate);
    return fee.status !== 'paid' && today > dueDate;
  }

  openPaymentModal(fee: FeeRecord): void {
    this.selectedFee = fee;
    this.paymentAmount = fee.amount - fee.paidAmount;
  }

  closePaymentModal(): void {
    this.selectedFee = null;
    this.paymentAmount = 0;
    this.paymentMethod = 'card';
  }

  processPayment(): void {
    if (!this.selectedFee || !this.paymentAmount) return;

    this.http.post(
      `${this.apiBase}/fees/${this.selectedFee.feeId}/pay?amount=${this.paymentAmount}&paymentMethod=${this.paymentMethod}`,
      {},
      { headers: this.getHeaders() }
    ).subscribe({
      next: () => {
        alert('Payment successful!');
        this.closePaymentModal();
        this.loadFees();
        this.loadSummary();
      },
      error: (err) => {
        console.error('Payment failed:', err);
        alert('Payment failed. Please try again.');
      }
    });
  }
}
