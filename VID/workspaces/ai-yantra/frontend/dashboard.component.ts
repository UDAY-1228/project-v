import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-ai-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = { total_models: 0, active_models: 0, total_automations: 0, active_automations: 0, api_calls_today: 0, success_rate: 0 };
  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.stats = { total_models: 8, active_models: 5, total_automations: 12, active_automations: 9, api_calls_today: 1247, success_rate: 99.2 };
      this.activities = [
        { id: '1', action: 'Model Started', actor: 'System', description: 'GPT-4 model is now running', timestamp: new Date() },
        { id: '2', action: 'Automation Triggered', actor: 'Scheduler', description: 'Daily report generation completed', timestamp: new Date(Date.now() - 3600000) },
        { id: '3', action: 'API Call', actor: 'API', description: 'Successfully processed 150 requests', timestamp: new Date(Date.now() - 7200000) }
      ];
      this.isLoading = false;
    }, 800);
  }
}
