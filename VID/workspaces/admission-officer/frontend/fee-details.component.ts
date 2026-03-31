import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-fee-details',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fee-details.component.html',
  styleUrls: ['./fee-details.component.css']
})
export class FeeDetailsComponent implements OnInit {
  fees: any[] = [];

  ngOnInit(): void {
    this.fees = [
      { student_name: 'Priya Sharma', course: 'Computer Science', total_amount: 150000, paid_amount: 150000, pending_amount: 0, payment_status: 'completed' },
      { student_name: 'Rahul Verma', course: 'Electronics', total_amount: 120000, paid_amount: 80000, pending_amount: 40000, payment_status: 'partial' },
      { student_name: 'Sneha Patel', course: 'Mechanical', total_amount: 100000, paid_amount: 50000, pending_amount: 50000, payment_status: 'partial' },
      { student_name: 'Amit Kumar', course: 'Civil', total_amount: 110000, paid_amount: 110000, pending_amount: 0, payment_status: 'completed' }
    ];
  }
}
