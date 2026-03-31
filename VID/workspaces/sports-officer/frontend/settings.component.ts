import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sports-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = {
    matchDuration: 90,
    overtimeEnabled: true,
    tiebreakerMethod: 'penalty_shootout',
    maxTeamSize: 25,
    minTeamSize: 11
  };

  saveSettings() {}
}
