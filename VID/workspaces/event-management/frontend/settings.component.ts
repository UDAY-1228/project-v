import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    defaultFee: 0,
    maxCapacity: 100,
    reminderDays: 3,
    allowCancellations: true,
    refundDays: 7
  };

  saveSettings() {}
}
