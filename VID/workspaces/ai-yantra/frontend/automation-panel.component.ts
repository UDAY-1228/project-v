import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Automation {
  id: string;
  name: string;
  description: string;
  triggerType: string;
  isActive: boolean;
  runCount: number;
  lastRun: Date | null;
}

@Component({
  selector: 'app-automation-panel',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './automation-panel.component.html',
  styleUrls: ['./automation-panel.component.css']
})
export class AutomationPanelComponent implements OnInit {
  automations: Automation[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.automations = [
        { id: '1', name: 'Daily Report Generator', description: 'Generate daily analytics reports', triggerType: 'schedule', isActive: true, runCount: 45, lastRun: new Date() },
        { id: '2', name: 'Data Sync', description: 'Sync data from external sources', triggerType: 'webhook', isActive: true, runCount: 120, lastRun: new Date(Date.now() - 3600000) },
        { id: '3', name: 'Model Health Check', description: 'Monitor model performance', triggerType: 'interval', isActive: false, runCount: 30, lastRun: new Date(Date.now() - 86400000) },
        { id: '4', name: 'Alert Notifier', description: 'Send alerts based on conditions', triggerType: 'event', isActive: true, runCount: 89, lastRun: new Date(Date.now() - 7200000) }
      ];
      this.isLoading = false;
    }, 800);
  }

  toggleAutomation(automation: Automation): void {
    automation.isActive = !automation.isActive;
  }

  runNow(automation: Automation): void {
    automation.lastRun = new Date();
    automation.runCount++;
  }

  createAutomation(): void {
    alert('Create new automation...');
  }
}
