import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-health-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    checkupFrequency: 90,
    bmiMin: 15.0,
    bmiMax: 35.0,
    emailNotifications: true,
    smsNotifications: false,
    pushNotifications: true
  };

  saveSettings() {
    console.log('Settings saved:', this.settings);
  }
}
