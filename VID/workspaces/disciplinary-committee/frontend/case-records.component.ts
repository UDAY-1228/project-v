import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-case-records',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './case-records.component.html',
  styleUrls: ['./case-records.component.css']
})
export class CaseRecordsComponent implements OnInit {
  cases: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.cases = [
        { id: '1', title: 'CASE-2024-001', complaint_id: 'CMP-001', status: 'investigating', members: 3, start_date: new Date() },
        { id: '2', title: 'CASE-2024-002', complaint_id: 'CMP-002', status: 'resolved', members: 2, start_date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
