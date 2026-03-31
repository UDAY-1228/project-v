import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dc-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  settings = { committee_name: 'Disciplinary Committee', chair_name: 'Dr. John Doe', auto_escalation_days: 30, require_approval: true };
  save() { console.log('Settings saved'); }
}
