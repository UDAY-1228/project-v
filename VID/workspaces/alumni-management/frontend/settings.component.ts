import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  organizationName = '';
  contactEmail = '';
  taxId = '';
  thankYouMessage = '';

  saveSettings() {
    console.log('Settings saved');
  }
}
