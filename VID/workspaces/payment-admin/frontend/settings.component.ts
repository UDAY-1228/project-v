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
  settings = {
    institution_name: 'VID Institute',
    gst_percentage: 18.0,
    late_fee_percentage: 1.5,
    late_fee_grace_days: 15,
    currency: 'INR',
    payment_gateway_enabled: true,
    auto_receipt_generation: true,
    email_notifications: true
  };

  saveSettings() {
    console.log('Settings saved:', this.settings);
  }
}
