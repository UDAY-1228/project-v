import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-medical-reports',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './medical-reports.component.html',
  styleUrls: ['./medical-reports.component.css']
})
export class MedicalReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchReports();
  }

  fetchReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', student_id: 'STU001', student_name: 'Rahul Sharma', report_type: 'checkup', examination_date: new Date('2024-03-15') },
        { id: '2', student_id: 'STU002', student_name: 'Priya Patel', report_type: 'lab', examination_date: new Date('2024-03-10') },
        { id: '3', student_id: 'STU003', student_name: 'Amit Kumar', report_type: 'checkup', examination_date: new Date('2024-03-05') }
      ];
      this.isLoading = false;
    }, 800);
  }

  getReportCount(type: string): number {
    return this.reports.filter(r => r.report_type === type).length;
  }
}
