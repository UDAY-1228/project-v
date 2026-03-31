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
  returns: any[] = [];

  ngOnInit(): void {
    this.issues = [
      { id: '1', member_name: 'Priya Sharma', book_title: 'Introduction to Algorithms', status: 'issued', issue_date: new Date(), due_date: new Date() },
      { id: '2', member_name: 'Rahul Verma', book_title: 'Clean Code', status: 'issued', issue_date: new Date(), due_date: new Date() },
      { id: '3', member_name: 'Sneha Patel', book_title: 'Design Patterns', status: 'issued', issue_date: new Date(), due_date: new Date() }
    ];
    this.returns = [
      { id: '1', member_name: 'Amit Kumar', book_title: 'Database Systems', return_date: new Date() },
      { id: '2', member_name: 'Neha Singh', book_title: 'Operating Systems', return_date: new Date() },
      { id: '3', member_name: 'Vikram Rao', book_title: 'Computer Networks', return_date: new Date() }
    ];
  }
}
