import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-library-admin-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_books: 0,
    issued_books: 0,
    available_books: 0,
    total_members: 0,
    overdue_books: 0,
    total_fines_collected: 0
  };

  recentIssues: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_books: 5420,
        issued_books: 156,
        available_books: 5120,
        total_members: 1850,
        overdue_books: 12,
        total_fines_collected: 24500
      };

      this.recentIssues = [
        { id: '1', member_name: 'Priya Sharma', book_title: 'Introduction to Algorithms', status: 'issued', due_date: new Date() },
        { id: '2', member_name: 'Rahul Verma', book_title: 'Database Systems', status: 'returned', due_date: new Date() },
        { id: '3', member_name: 'Sneha Patel', book_title: 'Operating Systems', status: 'issued', due_date: new Date() },
        { id: '4', member_name: 'Amit Kumar', book_title: 'Computer Networks', status: 'issued', due_date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
