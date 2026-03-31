import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    aiProvider: 'openai',
    apiKeyEnv: 'OPENAI_API_KEY',
    maxTokens: 2048,
    temperature: 0.7,
    defaultModel: 'gpt-4',
    rateLimit: 100,
    enableCaching: true,
    cacheTtl: 3600
  };
  isSaving = false;
  activeTab = 'ai';

  ngOnInit(): void {}

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  saveSettings(): void {
    this.isSaving = true;
    setTimeout(() => { this.isSaving = false; }, 1000);
  }
}
