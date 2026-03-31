import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-pd-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    academic_year: '2025-2026',
    semester_system: 'semester',
    grading_system: 'cgpa',
    max_students_per_class: 60,
    attendance_threshold: 75.0,
    pass_percentage: 40.0
  };

  saveSettings() {
    console.log('Settings saved:', this.settings);
  }
}
