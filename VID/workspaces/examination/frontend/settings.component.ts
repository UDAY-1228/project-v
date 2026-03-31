import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-examination-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class ExaminationSettingsComponent {
  settings = {
    exam_mode: 'offline',
    passing_percentage: 40,
    allow_revaluation: true,
    grading_scale: { A: 90, B: 80, C: 70, D: 60, E: 50, F: 0 }
  };

  saveSettings() { console.log('Saving settings...', this.settings); }
}
