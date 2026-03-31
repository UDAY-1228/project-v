import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    notification_email: true,
    notification_sms: false,
    notification_push: true,
    default_lecture_duration: 60,
    default_attendance_threshold: 75.0,
    auto_close_assignment_days: 7,
    auto_publish_results: false,
    require_student_verification: true,
    theme_preference: 'dark',
    language_preference: 'en'
  };

  isLoading = false;
  saveSuccess = false;

  ngOnInit(): void {
    this.fetchSettings();
  }

  fetchSettings() {
    setTimeout(() => {
      this.isLoading = false;
    }, 500);
  }

  saveSettings() {
    this.isLoading = true;
    this.saveSuccess = false;
    setTimeout(() => {
      this.isLoading = false;
      this.saveSuccess = true;
      setTimeout(() => {
        this.saveSuccess = false;
      }, 3000);
    }, 800);
  }
}
