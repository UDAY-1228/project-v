import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-reports',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  selectedReport = 'employees';
  loading = false;
  
  filterDepartment = '';
  filterStartDate = '';
  filterEndDate = '';
  
  departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'Operations', 'IT', 'Admin'];
  
  reportData: any = null;
  summaryItems: Array<{ label: string; value: string | number }> = [];
  tableHeaders: string[] = [];
  tableData: any[][] = [];

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.setDefaultDates();
    this.generateReport();
  }

  setDefaultDates() {
    const today = new Date();
    const firstDay = new Date(today.getFullYear(), today.getMonth(), 1);
    const lastDay = new Date(today.getFullYear(), today.getMonth() + 1, 0);
    
    this.filterStartDate = firstDay.toISOString().split('T')[0];
    this.filterEndDate = today.toISOString().split('T')[0];
  }

  selectReport(report: string) {
    this.selectedReport = report;
    this.reportData = null;
    this.generateReport();
  }

  generateReport() {
    this.loading = true;
    
    switch (this.selectedReport) {
      case 'employees':
        this.loadEmployeeReport();
        break;
      case 'attendance':
        this.loadAttendanceReport();
        break;
      case 'leave':
        this.loadLeaveReport();
        break;
      case 'payroll':
        this.loadPayrollReport();
        break;
    }
  }

  loadEmployeeReport() {
    const params = new URLSearchParams();
    if (this.filterDepartment) {
      params.append('department', this.filterDepartment);
    }
    
    this.http.get<any>(`${this.apiUrl}/reports/employees?${params.toString()}`).subscribe({
      next: (data) => {
        this.reportData = data;
        this.summaryItems = [
          { label: 'Total Employees', value: data.total_employees || 0 },
          { label: 'Departments', value: data.department_breakdown?.length || 0 }
        ];
        
        if (data.department_breakdown && data.department_breakdown.length > 0) {
          this.tableHeaders = ['Department', 'Employee Count', 'Average Salary'];
          this.tableData = data.department_breakdown.map((dept: any) => [
            dept.department || 'N/A',
            dept.count.toString(),
            this.formatCurrency(dept.avg_salary || 0)
          ]);
        } else {
          this.tableHeaders = [];
          this.tableData = [];
        }
        
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  loadAttendanceReport() {
    if (!this.filterStartDate || !this.filterEndDate) return;
    
    const params = new URLSearchParams();
    params.append('start_date', this.filterStartDate);
    params.append('end_date', this.filterEndDate);
    if (this.filterDepartment) {
      params.append('department', this.filterDepartment);
    }
    
    this.http.get<any>(`${this.apiUrl}/reports/attendance?${params.toString()}`).subscribe({
      next: (data) => {
        this.reportData = data;
        const statusBreakdown = data.status_breakdown || {};
        
        this.summaryItems = [
          { label: 'Total Records', value: data.total_records || 0 },
          { label: 'Present', value: statusBreakdown.present || 0 },
          { label: 'Absent', value: statusBreakdown.absent || 0 },
          { label: 'Late', value: statusBreakdown.late || 0 }
        ];
        
        this.tableHeaders = ['Status', 'Count'];
        this.tableData = Object.entries(statusBreakdown).map(([status, count]) => [
          status.charAt(0).toUpperCase() + status.slice(1),
          count.toString()
        ]);
        
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  loadLeaveReport() {
    this.http.get<any[]>(`${this.apiUrl}/leaves?limit=100`).subscribe({
      next: (data) => {
        this.reportData = data;
        
        const pending = data.filter((l: any) => l.status === 'pending').length;
        const approved = data.filter((l: any) => l.status === 'approved').length;
        const rejected = data.filter((l: any) => l.status === 'rejected').length;
        
        this.summaryItems = [
          { label: 'Total Requests', value: data.length },
          { label: 'Pending', value: pending },
          { label: 'Approved', value: approved },
          { label: 'Rejected', value: rejected }
        ];
        
        this.tableHeaders = ['Employee', 'Leave Type', 'Start Date', 'End Date', 'Status'];
        this.tableData = data.slice(0, 20).map((leave: any) => [
          leave.employee_id,
          leave.leave_type,
          this.formatDate(leave.start_date),
          this.formatDate(leave.end_date),
          leave.status
        ]);
        
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  loadPayrollReport() {
    const params = new URLSearchParams();
    params.append('limit', '100');
    
    this.http.get<any[]>(`${this.apiUrl}/payroll?${params.toString()}`).subscribe({
      next: (data) => {
        this.reportData = data;
        
        const totalGross = data.reduce((sum: number, p: any) => sum + (p.basic_salary || 0), 0);
        const totalNet = data.reduce((sum: number, p: any) => sum + (p.net_salary || 0), 0);
        const totalBonuses = data.reduce((sum: number, p: any) => sum + (p.bonuses || 0), 0);
        
        this.summaryItems = [
          { label: 'Total Records', value: data.length },
          { label: 'Total Gross', value: this.formatCurrency(totalGross) },
          { label: 'Total Net', value: this.formatCurrency(totalNet) },
          { label: 'Total Bonuses', value: this.formatCurrency(totalBonuses) }
        ];
        
        this.tableHeaders = ['Employee', 'Month/Year', 'Basic', 'Net Salary', 'Status'];
        this.tableData = data.slice(0, 20).map((payroll: any) => [
          payroll.employee_id,
          `${this.getMonthName(payroll.month)} ${payroll.year}`,
          this.formatCurrency(payroll.basic_salary),
          this.formatCurrency(payroll.net_salary),
          payroll.status
        ]);
        
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  exportReport() {
    if (!this.reportData) return;
    
    let csvContent = '';
    
    if (this.tableHeaders.length > 0) {
      csvContent = this.tableHeaders.join(',') + '\n';
      csvContent += this.tableData.map(row => row.join(',')).join('\n');
    } else {
      csvContent = 'Report Data\n';
      csvContent += JSON.stringify(this.reportData, null, 2);
    }
    
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${this.selectedReport}_report_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount || 0);
  }

  formatDate(dateStr: string): string {
    if (!dateStr) return '-';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  getMonthName(month: number): string {
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return months[month - 1] || '';
  }
}
