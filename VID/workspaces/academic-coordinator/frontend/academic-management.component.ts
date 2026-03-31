import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-academic-management',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './academic-management.component.html',
  styleUrls: ['./academic-management.component.css']
})
export class AcademicManagementComponent implements OnInit {
  academicYears: any[] = [];
  departments: any[] = [];
  activeTab: 'years' | 'departments' = 'years';
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData() {
    setTimeout(() => {
      this.academicYears = [
        { id: '1', year_name: '2024-2025', start_date: '2024-06-01', end_date: '2025-05-31', status: 'active' },
        { id: '2', year_name: '2023-2024', start_date: '2023-06-01', end_date: '2024-05-31', status: 'archived' }
      ];
      this.departments = [
        { id: '1', name: 'Computer Science', code: 'CS', hod: 'Dr. Alan Turing', students: 450 },
        { id: '2', name: 'Mathematics', code: 'MATH', hod: 'Dr. Emmy Noether', students: 320 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
