import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-fine-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fine-control.component.html',
  styleUrls: ['./fine-control.component.css']
})
export class FineControlComponent implements OnInit {
  fines: any[] = [];
  totalFines = 32500;
  collectedFines = 24500;
  pendingFines = 8000;
  overdueCases = 12;

  ngOnInit(): void {
    this.fines = [
      { id: '1', member_name: 'Amit Kumar', book_title: 'Computer Networks', fine_type: 'Overdue', days_overdue: 5, amount: 250, status: 'pending' },
      { id: '2', member_name: 'Neha Singh', book_title: 'Software Engineering', fine_type: 'Overdue', days_overdue: 3, amount: 150, status: 'paid' },
      { id: '3', member_name: 'Vikram Rao', book_title: 'Data Structures', fine_type: 'Damage', days_overdue: 0, amount: 500, status: 'pending' },
      { id: '4', member_name: 'Priya Sharma', book_title: 'Algorithms', fine_type: 'Overdue', days_overdue: 2, amount: 100, status: 'paid' }
    ];
  }
}
