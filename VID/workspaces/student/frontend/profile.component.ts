import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Profile {
  studentId: string;
  firstName: string;
  lastName: string;
  email: string;
  phone?: string;
  dateOfBirth?: string;
  gender?: string;
  address?: string;
  department: string;
  batch: string;
  section?: string;
  semester: number;
  enrollmentDate: string;
  profileImage?: string;
  parentName?: string;
  parentPhone?: string;
  emergencyContact?: string;
  bloodGroup?: string;
  isActive: boolean;
}

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profile: Profile | null = null;
  showEditModal = false;
  editForm: any = {};

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadProfile();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadProfile(): void {
    this.http.get<Profile>(`${this.apiBase}/profile`, { headers: this.getHeaders() })
      .subscribe({
        next: (profile) => this.profile = profile,
        error: (err) => console.error('Failed to load profile:', err)
      });
  }

  getInitials(): string {
    if (!this.profile) return '';
    return `${this.profile.firstName[0]}${this.profile.lastName[0]}`.toUpperCase();
  }

  formatDate(dateStr: string): string {
    if (!dateStr) return 'N/A';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  openEditModal(): void {
    if (!this.profile) return;
    this.editForm = {
      phone: this.profile.phone || '',
      address: this.profile.address || '',
      parentName: this.profile.parentName || '',
      parentPhone: this.profile.parentPhone || '',
      emergencyContact: this.profile.emergencyContact || ''
    };
    this.showEditModal = true;
  }

  closeEditModal(): void {
    this.showEditModal = false;
    this.editForm = {};
  }

  saveProfile(): void {
    this.http.put(`${this.apiBase}/profile`, this.editForm, { headers: this.getHeaders() })
      .subscribe({
        next: () => {
          alert('Profile updated successfully!');
          this.closeEditModal();
          this.loadProfile();
        },
        error: (err) => {
          console.error('Failed to update profile:', err);
          alert('Failed to update profile. Please try again.');
        }
      });
  }
}
