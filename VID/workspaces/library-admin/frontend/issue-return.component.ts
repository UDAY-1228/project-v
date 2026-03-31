import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-issue-return',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './issue-return.component.html',
  styleUrls: ['./issue-return.component.css']
})
export class IssueReturnComponent implements OnInit {
  issues: any[] = [];
  overdueBooks: any[] = [];

  ngOnInit(): void {
    this.issues = [
      { id: '1', member_name: 'Priya Sharma', book_title: 'Introduction to Algorithms', status: 'issued', issue_date: new Date(), due_date: new Date() },
      { id: '2', member_name: 'Rahul Verma', book_title: 'Database Systems', status: 'issued', issue_date: new Date(), due_date: new Date() },
      { id: '3', member_name: 'Sneha Patel', book_title: 'Operating Systems', status: 'returned', issue_date: new Date(), due_date: new Date() }
    ];
    this.overdueBooks = [
      { id: '1', member_name: 'Amit Kumar', book_title: 'Computer Networks', days_overdue: 5, fine_amount: 250 },
      { id: '2', member_name: 'Neha Singh', book_title: 'Software Engineering', days_overdue: 3, fine_amount: 150 }
    ];
  }
}
