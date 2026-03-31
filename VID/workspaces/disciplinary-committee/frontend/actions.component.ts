import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-actions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './actions.component.html',
  styleUrls: ['./actions.component.css']
})
export class ActionsComponent implements OnInit {
  actions: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.actions = [
        { id: '1', type: 'Warning', target: 'Student A', case_id: 'CASE-2024-001', severity: 'low', status: 'active' },
        { id: '2', type: 'Suspension', target: 'Student B', case_id: 'CASE-2024-002', severity: 'high', status: 'completed' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
