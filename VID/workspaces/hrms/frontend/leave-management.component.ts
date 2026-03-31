import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-leave-management',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './leave-management.component.html',
  styleUrls: ['./leave-management.component.css']
})
export class LeaveManagementComponent implements OnInit {
  leaveRequests: any[] = [];
  filteredRequests: any[] = [];
  employees: any[] = [];
  
  loading = false;
  filterStatus = '';
  
  pendingCount = 0;
  approvedCount = 0;
  rejectedCount = 0;
  
  showModal = false;
  leaveForm: FormGroup;

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.leaveForm = this.fb.group({
      employee_id: ['', Validators.required],
      leave_type: ['casual', Validators.required],
      start_date: ['', Validators.required],
      end_date: ['', Validators.required],
      reason: ['', Validators.required]
    });
  }

  ngOnInit() {
    this.loadEmployees();
    this.loadLeaveRequests();
  }

  loadEmployees() {
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=100`).subscribe({
      next: (data) => {
        this.employees = data;
      }
    });
  }

  loadLeaveRequests() {
    this.loading = true;
    const url = this.filterStatus 
      ? `${this.apiUrl}/leaves?status=${this.filterStatus}` 
      : `${this.apiUrl}/leaves?limit=100`;
    
    this.http.get<any[]>(url).subscribe({
      next: (data) => {
        this.leaveRequests = data;
        this.filteredRequests = data;
        this.calculateCounts();
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  calculateCounts() {
    this.pendingCount = this.leaveRequests.filter(r => r.status === 'pending').length;
    this.approvedCount = this.leaveRequests.filter(r => r.status === 'approved').length;
    this.rejectedCount = this.leaveRequests.filter(r => r.status === 'rejected').length;
  }

  getInitials(employeeId: string): string {
    if (!employeeId) return '??';
    return employeeId.substring(0, 2).toUpperCase();
  }

  formatDate(dateStr: string): string {
    if (!dateStr) return '-';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  calculateDays(start: string, end: string): number {
    const startDate = new Date(start);
    const endDate = new Date(end);
    const diff = endDate.getTime() - startDate.getTime();
    return Math.ceil(diff / (1000 * 60 * 60 * 24)) + 1;
  }

  calculateFormDays(): number {
    const start = this.leaveForm.value.start_date;
    const end = this.leaveForm.value.end_date;
    if (!start || !end) return 0;
    return this.calculateDays(start, end);
  }

  truncateReason(reason: string): string {
    if (!reason) return '';
    return reason.length > 30 ? reason.substring(0, 30) + '...' : reason;
  }

  openModal() {
    this.leaveForm.reset({
      leave_type: 'casual'
    });
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
  }

  submitRequest() {
    if (this.leaveForm.valid) {
      this.http.post(`${this.apiUrl}/leaves`, this.leaveForm.value).subscribe({
        next: () => {
          this.loadLeaveRequests();
          this.closeModal();
        },
        error: (err) => console.error('Failed to submit leave request:', err)
      });
    }
  }

  updateStatus(request: any, status: 'approved' | 'rejected') {
    const approvedBy = 'Admin';
    this.http.put(`${this.apiUrl}/leaves/${request._id}`, {
      status,
      approved_by: approvedBy,
      notes: status === 'approved' ? 'Approved by HR' : 'Rejected by HR'
    }).subscribe({
      next: () => {
        this.loadLeaveRequests();
      },
      error: (err) => console.error('Failed to update leave request:', err)
    });
  }
}
