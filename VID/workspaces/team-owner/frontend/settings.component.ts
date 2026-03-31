import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-team-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class TeamSettingsComponent {
  settings = {
    visibility: 'private',
    require_approval: true,
    two_factor: false,
    audit_logging: true
  };

  saveSettings() { console.log('Saving settings...', this.settings); }
}
