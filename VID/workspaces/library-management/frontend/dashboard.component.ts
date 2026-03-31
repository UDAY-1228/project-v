import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-library-management-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_catalog_books: 0,
    total_issues: 0,
    active_members: 0,
    reserved_books: 0,
    overdue_returns: 0,
    monthly_issues: 0
  };

  popularBooks: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_catalog_books: 8450,
        total_issues: 1245,
        active_members: 2100,
        reserved_books: 45,
        overdue_returns: 18,
        monthly_issues: 342
      };

      this.popularBooks = [
        { id: '1', title: 'Introduction to Algorithms', author: 'Cormen et al.', category: 'Computer Science', times_issued: 156, copies_available: 3 },
        { id: '2', title: 'Clean Code', author: 'Robert C. Martin', category: 'Programming', times_issued: 134, copies_available: 5 },
        { id: '3', title: 'Design Patterns', author: 'Gang of Four', category: 'Programming', times_issued: 112, copies_available: 2 },
        { id: '4', title: 'Database System Concepts', author: 'Korth et al.', category: 'Database', times_issued: 98, copies_available: 4 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
