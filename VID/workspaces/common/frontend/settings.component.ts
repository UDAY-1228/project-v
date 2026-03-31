import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-common-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    theme: 'dark',
    language: 'en',
    timezone: 'UTC',
    dateFormat: 'MM/DD/YYYY',
    timeFormat: '12h',
    compactMode: false,
    animationsEnabled: true,
    emailNotifications: true,
    pushNotifications: true,
    smsNotifications: false,
    notifyOnMentions: true,
    notifyOnAssignments: true,
    notifyOnComments: true,
    digestFrequency: 'daily'
  };
  activeTab = 'general';
  isSaving = false;

  ngOnInit(): void {}

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  saveSettings(): void {
    this.isSaving = true;
    setTimeout(() => {
      this.isSaving = false;
    }, 1000);
  }
}
