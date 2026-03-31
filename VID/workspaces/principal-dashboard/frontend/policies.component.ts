import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-policies',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './policies.component.html',
  styleUrls: ['./policies.component.css']
})
export class PoliciesComponent implements OnInit {
  policies: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.policies = [
        { id: '1', name: 'Attendance Policy', type: 'academic', status: 'active', effective_date: new Date('2024-01-01') },
        { id: '2', name: 'Examination Guidelines', type: 'exam', status: 'active', effective_date: new Date('2024-01-15') },
        { id: '3', name: 'Anti-Ragging Policy', type: 'conduct', status: 'active', effective_date: new Date('2023-06-01') }
      ];
      this.isLoading = false;
    }, 800);
  }
}
