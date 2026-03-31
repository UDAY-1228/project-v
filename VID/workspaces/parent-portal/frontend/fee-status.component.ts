import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-fee-status',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fee-status.component.html',
  styleUrls: ['./fee-status.component.css']
})
export class FeeStatusComponent implements OnInit {
  fees = [
    { feeType: 'Tuition Fee Q1', totalAmount: 2500, paidAmount: 2500, dueDate: new Date('2026-01-15'), status: 'paid' },
    { feeType: 'Tuition Fee Q2', totalAmount: 2500, paidAmount: 1500, dueDate: new Date('2026-04-15'), status: 'pending' },
    { feeType: 'Library Fee', totalAmount: 500, paidAmount: 500, dueDate: new Date('2026-02-01'), status: 'paid' },
    { feeType: 'Lab Fee', totalAmount: 500, paidAmount: 500, dueDate: new Date('2026-02-01'), status: 'paid' }
  ];

  ngOnInit(): void {}
}
