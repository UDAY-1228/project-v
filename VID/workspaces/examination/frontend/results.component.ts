import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-results',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  results: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchResults();
  }

  fetchResults() {
    setTimeout(() => {
      this.results = [
        { id: '1', student_name: 'John Doe', roll_number: 'CS2024001', subject: 'Mathematics', marks: 85, total: 100, grade: 'A', status: 'pass' },
        { id: '2', student_name: 'Jane Smith', roll_number: 'CS2024002', subject: 'Mathematics', marks: 72, total: 100, grade: 'B', status: 'pass' },
        { id: '3', student_name: 'Bob Wilson', roll_number: 'CS2024003', subject: 'Mathematics', marks: 38, total: 100, grade: 'F', status: 'fail' },
      ];
      this.isLoading = false;
    }, 600);
  }

  publishResults() { console.log('Publishing results...'); }
  uploadBulk() { console.log('Bulk upload...'); }
}
