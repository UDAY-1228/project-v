import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-transport-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    maxStudentsPerVehicle: 40,
    maintenanceAlertDays: 7,
    insuranceAlertDays: 30,
    emailNotifications: true,
    smsNotifications: true
  };
}
