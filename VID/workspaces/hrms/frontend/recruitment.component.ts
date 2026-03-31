import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-recruitment',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './recruitment.component.html',
  styleUrls: ['./recruitment.component.css']
})
export class RecruitmentComponent implements OnInit {
  positions: any[] = [];
  filteredPositions: any[] = [];
  applications: any[] = [];
  employees: any[] = [];
  
  loading = false;
  filterStatus = '';
  activeTab = 'positions';
  
  departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'Operations', 'IT', 'Admin'];
  
  showPositionModal = false;
  selectedPosition: any = null;
  positionForm: FormGroup;

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.positionForm = this.fb.group({
      title: ['', Validators.required],
      department: ['', Validators.required],
      description: ['', Validators.required],
      requirements: [''],
      salary_range_min: [null],
      salary_range_max: [null]
    });
  }

  ngOnInit() {
    this.loadPositions();
    this.loadApplications();
    this.loadEmployees();
  }

  loadPositions() {
    this.loading = true;
    this.http.get<any[]>(`${this.apiUrl}/recruitment/positions?limit=100`).subscribe({
      next: (data) => {
        this.positions = data;
        this.filterPositions();
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }

  loadApplications() {
    this.http.get<any[]>(`${this.apiUrl}/recruitment/applications?limit=100`).subscribe({
      next: (data) => {
        this.applications = data;
      }
    });
  }

  loadEmployees() {
    this.http.get<any[]>(`${this.apiUrl}/employees?limit=100`).subscribe({
      next: (data) => {
        this.employees = data;
      }
    });
  }

  filterPositions() {
    if (!this.filterStatus) {
      this.filteredPositions = [...this.positions];
    } else {
      this.filteredPositions = this.positions.filter(p => p.status === this.filterStatus);
    }
  }

  switchTab(tab: 'positions' | 'applications') {
    this.activeTab = tab;
  }

  formatCurrency(amount: number): string {
    if (!amount) return '';
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  }

  formatDate(dateStr: string | undefined): string {
    if (!dateStr) return '-';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  getInitials(app: any): string {
    return `${app.first_name?.[0] || ''}${app.last_name?.[0] || ''}`.toUpperCase();
  }

  getPositionTitle(positionId: string): string {
    const pos = this.positions.find(p => p._id === positionId);
    return pos ? pos.title : positionId;
  }

  openPositionModal() {
    this.selectedPosition = null;
    this.positionForm.reset();
    this.showPositionModal = true;
  }

  editPosition(position: any) {
    this.selectedPosition = position;
    const requirements = Array.isArray(position.requirements) 
      ? position.requirements.join('\n') 
      : position.requirements || '';
    this.positionForm.patchValue({
      title: position.title,
      department: position.department,
      description: position.description,
      requirements: requirements,
      salary_range_min: position.salary_range_min,
      salary_range_max: position.salary_range_max
    });
    this.showPositionModal = true;
  }

  closePositionModal() {
    this.showPositionModal = false;
    this.selectedPosition = null;
  }

  savePosition() {
    if (this.positionForm.valid) {
      const formData = this.positionForm.value;
      formData.requirements = formData.requirements.split('\n').filter((r: string) => r.trim());
      
      if (this.selectedPosition) {
        this.http.put(`${this.apiUrl}/recruitment/positions/${this.selectedPosition._id}`, formData).subscribe({
          next: () => {
            this.loadPositions();
            this.closePositionModal();
          },
          error: (err) => console.error('Failed to update position:', err)
        });
      } else {
        this.http.post(`${this.apiUrl}/recruitment/positions`, formData).subscribe({
          next: () => {
            this.loadPositions();
            this.closePositionModal();
          },
          error: (err) => console.error('Failed to create position:', err)
        });
      }
    }
  }

  viewApplications(position: any) {
    this.activeTab = 'applications';
    this.http.get<any[]>(`${this.apiUrl}/recruitment/applications?position_id=${position._id}`).subscribe({
      next: (data) => {
        this.applications = data;
      }
    });
  }

  updateApplicationStatus(app: any) {
    this.http.put(`${this.apiUrl}/recruitment/applications/${app._id}`, { status: app.status }).subscribe({
      next: () => {
        console.log('Application status updated');
      },
      error: (err) => console.error('Failed to update application:', err)
    });
  }
}
