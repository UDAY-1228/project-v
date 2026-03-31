import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-timetable-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class TimetableSettingsComponent {
  settings = {
    working_days: 6,
    slot_duration: 60,
    collision_detection: true,
    auto_allocation: false
  };

  saveSettings() { console.log('Saving settings...', this.settings); }
}
