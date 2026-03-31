import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-fee-collection',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fee-collection.component.html',
  styleUrls: ['./fee-collection.component.css']
})
export class FeeCollectionComponent implements OnInit {
  feeStructures: any[] = [];
  studentFees: any[] = [];
  isLoading = true;
  activeTab = 'structures';

  constructor() {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData() {
    setTimeout(() => {
      this.feeStructures = [
        { id: 'FS001', fee_name: 'Tuition Fee', fee_code: 'TUF001', amount: 45000, academic_year: '2025-2026', due_date: new Date('2026-04-15'), status: 'active' },
        { id: 'FS002', fee_name: 'Lab Fee', fee_code: 'LAB001', amount: 15000, academic_year: '2025-2026', due_date: new Date('2026-04-20'), status: 'active' },
        { id: 'FS003', fee_name: 'Examination Fee', fee_code: 'EXM001', amount: 8000, academic_year: '2025-2026', due_date: new Date('2026-05-01'), status: 'active' }
      ];
      this.studentFees = [
        { student_name: 'Priya Sharma', fee_name: 'Tuition Fee', amount_payable: 45000, amount_paid: 45000, balance: 0, status: 'paid' },
        { student_name: 'Rahul Kumar', fee_name: 'Tuition Fee', amount_payable: 45000, amount_paid: 20000, balance: 25000, status: 'partial' },
        { student_name: 'Sneha Patel', fee_name: 'Lab Fee', amount_payable: 15000, amount_paid: 0, balance: 15000, status: 'pending' }
      ];
      this.isLoading = false;
    }, 600);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
  }

  setActiveTab(tab: string) {
    this.activeTab = tab;
  }
}
