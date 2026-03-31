import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Settings {
  studentId: string;
  emailNotifications: boolean;
  smsNotifications: boolean;
  pushNotifications: boolean;
  attendanceAlerts: boolean;
  feeReminders: boolean;
  examReminders: boolean;
  resultNotifications: boolean;
  language: string;
  timezone: string;
  theme: string;
}

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings: Settings | null = null;

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadSettings();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadSettings(): void {
    this.http.get<Settings>(`${this.apiBase}/settings`, { headers: this.getHeaders() })
      .subscribe({
        next: (settings) => this.settings = settings,
        error: (err) => console.error('Failed to load settings:', err)
      });
  }

  updateSetting(key: string): void {
    if (!this.settings) return;

    const updateData: any = {};
    updateData[key] = (this.settings as any)[key];

    this.http.put(`${this.apiBase}/settings`, updateData, { headers: this.getHeaders() })
      .subscribe({
        next: () => console.log('Setting updated:', key),
        error: (err) => {
          console.error('Failed to update setting:', err);
          this.loadSettings();
        }
      });
  }

  exportData(): void {
    alert('Data export feature coming soon!');
  }

  deactivateAccount(): void {
    if (confirm('Are you sure you want to deactivate your account? This action cannot be undone.')) {
      alert('Account deactivation feature coming soon!');
    }
  }
}
