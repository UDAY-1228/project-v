import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-subjects',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './subjects.component.html',
  styleUrls: ['./subjects.component.css']
})
export class SubjectsComponent implements OnInit {
  subjects: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.subjects = [
        { id: '1', name: 'Data Structures', code: 'CS-201', credits: 4, faculty: 'Dr. Neeraj', type: 'theory' },
        { id: '2', name: 'Database Lab', code: 'CS-205', credits: 2, faculty: 'Prof. Anjali', type: 'lab' },
        { id: '3', name: 'Discrete Math', code: 'MA-102', credits: 3, faculty: 'Dr. Ramanujan', type: 'theory' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
