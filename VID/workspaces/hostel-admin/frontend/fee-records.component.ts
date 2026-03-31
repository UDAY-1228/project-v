import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-fee-records',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fee-records.component.html',
  styleUrls: ['./fee-records.component.css']
})
export class FeeRecordsComponent implements OnInit {
  fees: any[] = [];
  totalCollected = 0;
  totalPending = 0;
  overdueCount = 0;

  constructor() {}

  ngOnInit(): void {
    this.fees = [
      { id: '1', student_name: 'Rahul Sharma', amount: 30000, paid_amount: 30000, due_date: new Date('2024-01-15'), status: 'paid' },
      { id: '2', student_name: 'Priya Patel', amount: 30000, paid_amount: 15000, due_date: new Date('2024-01-20'), status: 'partially_paid' },
      { id: '3', student_name: 'Amit Kumar', amount: 30000, paid_amount: 0, due_date: new Date('2024-01-10'), status: 'unpaid' }
    ];
    this.calculateTotals();
  }

  calculateTotals() {
    this.totalCollected = this.fees.reduce((sum, f) => sum + f.paid_amount, 0);
    this.totalPending = this.fees.reduce((sum, f) => sum + (f.amount - f.paid_amount), 0);
    this.overdueCount = this.fees.filter(f => f.status === 'unpaid' && new Date(f.due_date) < new Date()).length;
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      paid: 'bg-emerald-500/10 text-emerald-400',
      partially_paid: 'bg-amber-500/10 text-amber-400',
      unpaid: 'bg-red-500/10 text-red-400'
    };
    return classes[status] || classes.unpaid;
  }
}
