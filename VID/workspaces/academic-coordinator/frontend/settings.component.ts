import { Component, OnInit } from '@angular/core';
import { CommonModule, FormsModule } from '@angular/common';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    grading_system: 'absolute',
    max_credits_per_semester: 30,
    min_attendance_percentage: 75.0,
    pass_percentage: 40.0,
    allow_course_registration: true,
    result_publication_mode: 'manual',
    notification_preferences: {
      email: true,
      sms: false,
      push: true,
    },
    academic_calendar_enabled: true
  };

  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.isLoading = false;
    }, 800);
  }

  saveSettings() {
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      alert('Academic policy updated successfully.');
    }, 1200);
  }
}
