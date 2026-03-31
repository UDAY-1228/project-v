import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-transactions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.css']
})
export class TransactionsComponent implements OnInit {
  transactions: any[] = [];
  isLoading = true;
  searchQuery = '';

  constructor() {}

  ngOnInit(): void {
    this.loadTransactions();
  }

  loadTransactions() {
    setTimeout(() => {
      this.transactions = [
        { id: 'TXN001', student_name: 'Priya Sharma', amount: 45000, payment_mode: 'online', status: 'completed', date: new Date('2026-03-28') },
        { id: 'TXN002', student_name: 'Rahul Kumar', amount: 32000, payment_mode: 'offline', status: 'pending', date: new Date('2026-03-27') },
        { id: 'TXN003', student_name: 'Sneha Patel', amount: 55000, payment_mode: 'online', status: 'completed', date: new Date('2026-03-26') },
        { id: 'TXN004', student_name: 'Amit Singh', amount: 28000, payment_mode: 'online', status: 'failed', date: new Date('2026-03-25') },
        { id: 'TXN005', student_name: 'Neha Gupta', amount: 42000, payment_mode: 'offline', status: 'completed', date: new Date('2026-03-24') }
      ];
      this.isLoading = false;
    }, 600);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      completed: 'bg-emerald-500/20 text-emerald-400',
      pending: 'bg-yellow-500/20 text-yellow-400',
      failed: 'bg-red-500/20 text-red-400',
      refunded: 'bg-purple-500/20 text-purple-400'
    };
    return classes[status] || 'bg-zinc-500/20 text-zinc-400';
  }
}
