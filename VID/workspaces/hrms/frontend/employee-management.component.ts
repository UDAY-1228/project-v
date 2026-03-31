import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-employee-management',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './employee-management.component.html',
  styleUrls: ['./employee-management.component.css']
})
export class EmployeeManagementComponent implements OnInit {
  employees: any[] = [];
  filteredEmployees: any[] = [];
  departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'Operations', 'IT', 'Admin'];
  
  loading = false;
  searchTerm = '';
  filterDepartment = '';
  filterStatus = '';
  currentPage = 1;
  pageSize = 10;
  totalPages = 1;
  
  showModal = false;
  modalMode: 'create' | 'view' | 'edit' = 'create';
  employeeForm: FormGroup;
  selectedEmployee: any = null;

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.employeeForm = this.fb.group({
      employee_id: ['', Validators.required],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', Validators.required],
      date_of_birth: [''],
      gender: [''],
      address: [''],
      department: ['', Validators.required],
      designation: ['', Validators.required],
      employment_type: ['full_time'],
      joining_date: ['', Validators.required],
      salary: [''],
      status: ['active']
    });
  }

  ngOnInit() {
    this.loadEmployees();
  }

  loadEmployees() {
    this.loading = true;
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=100`).subscribe({
      next: (data) => {
        this.employees = data;
        this.filterEmployees();
        this.loading = false;
      },
      error: (err) => {
        console.error('Failed to load employees:', err);
        this.loading = false;
      }
    });
  }

  filterEmployees() {
    let filtered = [...this.employees];
    
    if (this.searchTerm) {
      const term = this.searchTerm.toLowerCase();
      filtered = filtered.filter(emp => 
        emp.first_name?.toLowerCase().includes(term) ||
        emp.last_name?.toLowerCase().includes(term) ||
        emp.email?.toLowerCase().includes(term) ||
        emp.employee_id?.toLowerCase().includes(term)
      );
    }
    
    if (this.filterDepartment) {
      filtered = filtered.filter(emp => emp.department === this.filterDepartment);
    }
    
    if (this.filterStatus) {
      filtered = filtered.filter(emp => emp.status === this.filterStatus);
    }
    
    this.totalPages = Math.ceil(filtered.length / this.pageSize) || 1;
    this.filteredEmployees = filtered.slice(
      (this.currentPage - 1) * this.pageSize,
      this.currentPage * this.pageSize
    );
  }

  goToPage(page: number) {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
      this.filterEmployees();
    }
  }

  openModal(mode: 'create' | 'view' | 'edit' = 'create') {
    this.modalMode = mode;
    this.showModal = true;
    if (mode === 'create') {
      this.employeeForm.reset({
        employment_type: 'full_time',
        status: 'active'
      });
    }
  }

  closeModal() {
    this.showModal = false;
    this.selectedEmployee = null;
    this.employeeForm.reset();
  }

  viewEmployee(employee: any) {
    this.selectedEmployee = employee;
    this.employeeForm.patchValue(employee);
    this.openModal('view');
  }

  editEmployee(employee: any) {
    this.selectedEmployee = employee;
    this.employeeForm.patchValue(employee);
    this.openModal('edit');
  }

  saveEmployee() {
    if (this.employeeForm.valid) {
      const formData = this.employeeForm.value;
      
      if (this.modalMode === 'create') {
        this.http.post(`${this.apiUrl}/employees`, formData).subscribe({
          next: () => {
            this.loadEmployees();
            this.closeModal();
          },
          error: (err) => console.error('Failed to create employee:', err)
        });
      } else {
        this.http.put(`${this.apiUrl}/employees/${this.selectedEmployee.employee_id}`, formData).subscribe({
          next: () => {
            this.loadEmployees();
            this.closeModal();
          },
          error: (err) => console.error('Failed to update employee:', err)
        });
      }
    }
  }

  deleteEmployee(employee: any) {
    if (confirm(`Are you sure you want to delete employee ${employee.first_name} ${employee.last_name}?`)) {
      this.http.delete(`${this.apiUrl}/employees/${employee.employee_id}`).subscribe({
        next: () => {
          this.loadEmployees();
        },
        error: (err) => console.error('Failed to delete employee:', err)
      });
    }
  }

  getInitials(employee: any): string {
    return `${employee.first_name?.[0] || ''}${employee.last_name?.[0] || ''}`.toUpperCase();
  }
}
