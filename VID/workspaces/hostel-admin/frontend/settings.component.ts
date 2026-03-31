import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-hostel-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    hostelName: 'Main Hostel',
    wardenName: 'Mr. Rajesh Kumar',
    curfewTime: '21:00',
    visitorTimings: '10:00-18:00'
  };
}
