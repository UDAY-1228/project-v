import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  records: any[] = [];
  filteredRecords: any[] = [];
  employees: any[] = [];
  
  loading = false;
  searchTerm = '';
  filterDate = new Date().toISOString().split('T')[0];
  
  stats = {
    present: 0,
    absent: 0,
    late: 0,
    halfDay: 0
  };
  
  showModal = false;
  selectedRecord: any = null;
  attendanceForm: FormGroup;

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.attendanceForm = this.fb.group({
      employee_id: ['', Validators.required],
      date: [this.filterDate, Validators.required],
      check_in: [''],
      check_out: [''],
      status: ['present', Validators.required],
      overtime_hours: [0],
      notes: ['']
    });
  }

  ngOnInit() {
    this.loadAttendance();
    this.loadEmployees();
  }

  loadEmployees() {
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=100`).subscribe({
      next: (data) => {
        this.employees = data;
      }
    });
  }

  loadAttendance() {
    this.loading = true;
    const dateObj = this.filterDate ? new Date(this.filterDate) : new Date();
    const dateStr = dateObj.toISOString().split('T')[0];
    
    this.http.get<any[]>(`${this.apiUrl}/attendance?start_date=${dateStr}&end_date=${dateStr}`).subscribe({
      next: (data) => {
        this.records = data;
        this.calculateStats();
        this.filterAttendance();
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  calculateStats() {
    this.stats = {
      present: this.records.filter(r => r.status === 'present').length,
      absent: this.records.filter(r => r.status === 'absent').length,
      late: this.records.filter(r => r.status === 'late').length,
      halfDay: this.records.filter(r => r.status === 'half_day').length
    };
  }

  filterAttendance() {
    if (!this.searchTerm) {
      this.filteredRecords = [...this.records];
    } else {
      const term = this.searchTerm.toLowerCase();
      this.filteredRecords = this.records.filter(r => 
        r.employee_id?.toLowerCase().includes(term)
      );
    }
  }

  openMarkModal() {
    this.selectedRecord = null;
    this.attendanceForm.reset({
      date: this.filterDate,
      status: 'present',
      overtime_hours: 0
    });
    this.showModal = true;
  }

  editRecord(record: any) {
    this.selectedRecord = record;
    this.attendanceForm.patchValue({
      employee_id: record.employee_id,
      date: this.formatDateForInput(record.date),
      check_in: record.check_in ? this.formatTime(record.check_in) : '',
      check_out: record.check_out ? this.formatTime(record.check_out) : '',
      status: record.status,
      overtime_hours: record.overtime_hours || 0,
      notes: record.notes || ''
    });
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
    this.selectedRecord = null;
  }

  saveRecord() {
    if (this.attendanceForm.valid) {
      const formData = this.attendanceForm.value;
      
      if (this.selectedRecord) {
        this.http.put(`${this.apiUrl}/attendance/${this.selectedRecord._id}`, formData).subscribe({
          next: () => {
            this.loadAttendance();
            this.closeModal();
          },
          error: (err) => console.error('Failed to update attendance:', err)
        });
      } else {
        this.http.post(`${this.apiUrl}/attendance`, formData).subscribe({
          next: () => {
            this.loadAttendance();
            this.closeModal();
          },
          error: (err) => console.error('Failed to create attendance:', err)
        });
      }
    }
  }

  deleteRecord(record: any) {
    if (confirm('Are you sure you want to delete this attendance record?')) {
      this.http.delete(`${this.apiUrl}/attendance/${record._id}`).subscribe({
        next: () => {
          this.loadAttendance();
        },
        error: (err) => console.error('Failed to delete attendance:', err)
      });
    }
  }

  formatDate(dateStr: string | Date): string {
    if (!dateStr) return '-';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  formatDateForInput(dateStr: string | Date): string {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toISOString().split('T')[0];
  }

  formatTime(dateStr: string): string {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
  }

  getInitials(employeeId: string): string {
    if (!employeeId) return '??';
    return employeeId.substring(0, 2).toUpperCase();
  }
}
