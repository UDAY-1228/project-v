import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-book-catalog',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './book-catalog.component.html',
  styleUrls: ['./book-catalog.component.css']
})
export class BookCatalogComponent implements OnInit {
  books: any[] = [];

  ngOnInit(): void {
    this.books = [
      { id: '1', title: 'Introduction to Algorithms', author: 'Cormen et al.', isbn: '978-0262033848', copies_available: 3 },
      { id: '2', title: 'Clean Code', author: 'Robert C. Martin', isbn: '978-0132350884', copies_available: 5 },
      { id: '3', title: 'Design Patterns', author: 'Gang of Four', isbn: '978-0201633610', copies_available: 2 },
      { id: '4', title: 'Database System Concepts', author: 'Korth et al.', isbn: '978-0073523323', copies_available: 4 },
      { id: '5', title: 'Operating Systems', author: 'Silberschatz', isbn: '978-1118063330', copies_available: 0 },
      { id: '6', title: 'Computer Networks', author: 'Tanenbaum', isbn: '978-0132126953', copies_available: 6 },
      { id: '7', title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', isbn: '978-0135957059', copies_available: 3 },
      { id: '8', title: 'Structure and Interpretation', author: 'Abelson & Sussman', isbn: '978-0262510878', copies_available: 2 }
    ];
  }
}
