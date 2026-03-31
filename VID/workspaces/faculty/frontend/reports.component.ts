import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-reports',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  reports: any[] = [];
  isLoading = true;
  showGenerateModal = false;

  newReport = {
    report_name: '',
    report_type: 'attendance',
    class_id: '',
    start_date: '',
    end_date: ''
  };

  reportTypes = [
    { value: 'attendance', label: 'Attendance Report' },
    { value: 'performance', label: 'Performance Report' },
    { value: 'submission', label: 'Submission Report' },
    { value: 'summary', label: 'Class Summary' }
  ];

  ngOnInit(): void {
    this.fetchReports();
  }

  fetchReports() {
    setTimeout(() => {
      this.reports = [
        { id: '1', report_name: 'March 2026 Attendance Report - CS301', report_type: 'attendance', class_name: 'Data Structures', generated_date: '2026-03-31', generated_by: 'Dr. Sharma', status: 'completed' },
        { id: '2', report_name: 'Mid-Semester Performance - CS302', report_type: 'performance', class_name: 'Database Systems', generated_date: '2026-03-25', generated_by: 'Dr. Sharma', status: 'completed' },
        { id: '3', report_name: 'Assignment Submission Status', report_type: 'submission', class_name: 'Algorithms', generated_date: '2026-03-20', generated_by: 'Dr. Sharma', status: 'completed' },
        { id: '4', report_name: 'Weekly Class Summary', report_type: 'summary', class_name: 'All Classes', generated_date: '2026-03-15', generated_by: 'Dr. Sharma', status: 'pending' }
      ];
      this.isLoading = false;
    }, 800);
  }

  openGenerateModal() {
    this.showGenerateModal = true;
  }

  closeGenerateModal() {
    this.showGenerateModal = false;
  }

  generateReport() {
    const newReport = {
      ...this.newReport,
      id: Date.now().toString(),
      generated_date: new Date().toISOString().split('T')[0],
      generated_by: 'Dr. Sharma',
      status: 'pending'
    };
    this.reports.unshift(newReport);
    this.closeGenerateModal();
  }

  downloadReport(id: string) {
    console.log('Downloading report:', id);
  }

  deleteReport(id: string) {
    if (confirm('Delete this report?')) {
      this.reports = this.reports.filter(r => r.id !== id);
    }
  }

  getTypeColor(type: string) {
    switch(type) {
      case 'attendance': return 'bg-blue-500/10 text-blue-400';
      case 'performance': return 'bg-purple-500/10 text-purple-400';
      case 'submission': return 'bg-amber-500/10 text-amber-400';
      default: return 'bg-zinc-500/10 text-zinc-400';
    }
  }
}
