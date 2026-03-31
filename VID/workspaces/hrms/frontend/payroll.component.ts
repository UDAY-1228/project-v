import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-payroll',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './payroll.component.html',
  styleUrls: ['./payroll.component.css']
})
export class PayrollComponent implements OnInit {
  payrollRecords: any[] = [];
  employees: any[] = [];
  
  loading = false;
  filterMonth = new Date().getMonth() + 1;
  filterYear = new Date().getFullYear();
  
  months = [
    { value: 1, label: 'January' },
    { value: 2, label: 'February' },
    { value: 3, label: 'March' },
    { value: 4, label: 'April' },
    { value: 5, label: 'May' },
    { value: 6, label: 'June' },
    { value: 7, label: 'July' },
    { value: 8, label: 'August' },
    { value: 9, label: 'September' },
    { value: 10, label: 'October' },
    { value: 11, label: 'November' },
    { value: 12, label: 'December' }
  ];
  
  years: number[] = [];
  
  totalGross = 0;
  totalDeductions = 0;
  totalNet = 0;
  pendingCount = 0;
  
  showModal = false;
  selectedRecord: any = null;
  payrollForm: FormGroup;

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient, private fb: FormBuilder) {
    const currentYear = new Date().getFullYear();
    this.years = Array.from({ length: 6 }, (_, i) => currentYear - 2 + i);
    
    this.payrollForm = this.fb.group({
      employee_id: ['', Validators.required],
      month: [this.filterMonth, Validators.required],
      year: [this.filterYear, Validators.required],
      basic_salary: [0, [Validators.required, Validators.min(0)]],
      allowances: [0],
      deductions: [0],
      overtime_pay: [0],
      bonuses: [0],
      tax: [0]
    });
  }

  ngOnInit() {
    this.loadEmployees();
    this.loadPayroll();
  }

  loadEmployees() {
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=100`).subscribe({
      next: (data) => {
        this.employees = data;
      }
    });
  }

  loadPayroll() {
    this.loading = true;
    this.http.get<any[]>(`${this.apiUrl}/payroll?month=${this.filterMonth}&year=${this.filterYear}`).subscribe({
      next: (data) => {
        this.payrollRecords = data;
        this.calculateTotals();
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  calculateTotals() {
    this.totalGross = this.payrollRecords.reduce((sum, r) => sum + (r.basic_salary || 0), 0);
    this.totalDeductions = this.payrollRecords.reduce((sum, r) => sum + (r.deductions || 0) + (r.tax || 0), 0);
    this.totalNet = this.payrollRecords.reduce((sum, r) => sum + (r.net_salary || 0), 0);
    this.pendingCount = this.payrollRecords.filter(r => r.status === 'pending').length;
  }

  getEmployeeName(employeeId: string): string {
    const emp = this.employees.find(e => e.employee_id === employeeId);
    return emp ? `${emp.first_name} ${emp.last_name}` : employeeId;
  }

  formatCurrency(amount: number): string {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount || 0);
  }

  calculateNet(): number {
    const values = this.payrollForm.value;
    return (values.basic_salary || 0)
      + (values.allowances || 0)
      + (values.overtime_pay || 0)
      + (values.bonuses || 0)
      - (values.deductions || 0)
      - (values.tax || 0);
  }

  openModal() {
    this.selectedRecord = null;
    this.payrollForm.reset({
      month: this.filterMonth,
      year: this.filterYear,
      basic_salary: 0,
      allowances: 0,
      deductions: 0,
      overtime_pay: 0,
      bonuses: 0,
      tax: 0
    });
    this.showModal = true;
  }

  viewRecord(record: any) {
    this.selectedRecord = record;
    this.payrollForm.patchValue(record);
    this.payrollForm.disable();
    this.showModal = true;
  }

  editRecord(record: any) {
    this.selectedRecord = record;
    this.payrollForm.patchValue(record);
    this.payrollForm.enable();
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
    this.selectedRecord = null;
    this.payrollForm.enable();
  }

  savePayroll() {
    if (this.payrollForm.valid) {
      const formData = this.payrollForm.value;
      formData.net_salary = this.calculateNet();
      
      if (this.selectedRecord) {
        this.http.put(`${this.apiUrl}/payroll/${this.selectedRecord._id}`, formData).subscribe({
          next: () => {
            this.loadPayroll();
            this.closeModal();
          },
          error: (err) => console.error('Failed to update payroll:', err)
        });
      } else {
        this.http.post(`${this.apiUrl}/payroll`, formData).subscribe({
          next: () => {
            this.loadPayroll();
            this.closeModal();
          },
          error: (err) => console.error('Failed to create payroll:', err)
        });
      }
    }
  }

  markAsPaid(record: any) {
    this.http.put(`${this.apiUrl}/payroll/${record._id}`, { status: 'paid' }).subscribe({
      next: () => {
        this.loadPayroll();
      },
      error: (err) => console.error('Failed to update payroll:', err)
    });
  }
}
