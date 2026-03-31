import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    company_name: 'Organization',
    working_hours_start: '09:00',
    working_hours_end: '17:00',
    late_threshold_minutes: 15,
    overtime_rate: 1.5,
    casual_leave_limit: 12,
    sick_leave_limit: 10,
    annual_leave_limit: 20
  };

  notifications = {
    leaveRequests: true,
    payrollUpdates: true,
    attendanceAlerts: true,
    newApplications: true
  };

  originalSettings: any = {};
  showToast = false;
  toastMessage = '';
  toastType: 'success' | 'error' = 'success';

  private apiUrl = '/api/hrms';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.originalSettings = { ...this.settings };
    this.loadSettings();
  }

  loadSettings() {
    this.http.get<any>(`${this.apiUrl}/settings`).subscribe({
      next: (data) => {
        if (data) {
          this.settings = {
            company_name: data.company_name || 'Organization',
            working_hours_start: data.working_hours_start || '09:00',
            working_hours_end: data.working_hours_end || '17:00',
            late_threshold_minutes: data.late_threshold_minutes || 15,
            overtime_rate: data.overtime_rate || 1.5,
            casual_leave_limit: data.casual_leave_limit || 12,
            sick_leave_limit: data.sick_leave_limit || 10,
            annual_leave_limit: data.annual_leave_limit || 20
          };
          this.originalSettings = { ...this.settings };
        }
      },
      error: (err) => {
        console.error('Failed to load settings:', err);
      }
    });
  }

  saveSettings() {
    this.http.put(`${this.apiUrl}/settings`, this.settings).subscribe({
      next: () => {
        this.originalSettings = { ...this.settings };
        this.showNotification('Settings saved successfully!', 'success');
      },
      error: (err) => {
        console.error('Failed to save settings:', err);
        this.showNotification('Failed to save settings', 'error');
      }
    });
  }

  resetSettings() {
    if (confirm('Are you sure you want to reset all settings to defaults?')) {
      this.settings = {
        company_name: 'Organization',
        working_hours_start: '09:00',
        working_hours_end: '17:00',
        late_threshold_minutes: 15,
        overtime_rate: 1.5,
        casual_leave_limit: 12,
        sick_leave_limit: 10,
        annual_leave_limit: 20
      };
      this.saveSettings();
    }
  }

  exportData() {
    const data = {
      settings: this.settings,
      notifications: this.notifications,
      exportDate: new Date().toISOString()
    };
    
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `hrms_settings_${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    window.URL.revokeObjectURL(url);
    
    this.showNotification('Data exported successfully!', 'success');
  }

  importData() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    
    input.onchange = (e: any) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event: any) => {
          try {
            const data = JSON.parse(event.target.result);
            if (data.settings) {
              this.settings = { ...this.settings, ...data.settings };
              this.showNotification('Data imported successfully!', 'success');
            }
          } catch (err) {
            this.showNotification('Invalid file format', 'error');
          }
        };
        reader.readAsText(file);
      }
    };
    
    input.click();
  }

  showNotification(message: string, type: 'success' | 'error') {
    this.toastMessage = message;
    this.toastType = type;
    this.showToast = true;
    
    setTimeout(() => {
      this.showToast = false;
    }, 3000);
  }
}
