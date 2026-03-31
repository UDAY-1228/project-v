import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-assessments',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './assessments.component.html',
  styleUrls: ['./assessments.component.css']
})
export class AssessmentsComponent implements OnInit {
  assessments: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.assessments = [
        { id: '1', name: 'Mid-term Exam', subject: 'Data Structures', date: '2024-03-24', status: 'completed', type: 'internal' },
        { id: '2', name: 'Lab Viva', subject: 'Database Systems', date: '2024-04-12', status: 'active', type: 'internal' },
        { id: '3', name: 'Final Semester', subject: 'Operating Systems', date: '2024-05-15', status: 'draft', type: 'external' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
