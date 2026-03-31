import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-book-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './book-control.component.html',
  styleUrls: ['./book-control.component.css']
})
export class BookControlComponent implements OnInit {
  books: any[] = [];

  ngOnInit(): void {
    this.books = [
      { accession_number: 'ACC-001', title: 'Introduction to Algorithms', author: 'Cormen', category: 'Computer Science', available: 5, total: 10 },
      { accession_number: 'ACC-002', title: 'Database Systems', author: 'Korth', category: 'Computer Science', available: 3, total: 8 },
      { accession_number: 'ACC-003', title: 'Operating Systems', author: 'Silberschatz', category: 'Computer Science', available: 0, total: 6 },
      { accession_number: 'ACC-004', title: 'Computer Networks', author: 'Tanenbaum', category: 'Computer Science', available: 7, total: 12 }
    ];
  }
}
