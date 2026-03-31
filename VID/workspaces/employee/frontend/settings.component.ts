import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    notificationEmail: true,
    notificationSms: false,
    notificationPush: true,
    theme: 'dark',
    language: 'en',
    timezone: 'UTC'
  };

  saveSettings() {}
}
