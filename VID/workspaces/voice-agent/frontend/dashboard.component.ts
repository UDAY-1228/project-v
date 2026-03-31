import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-voice-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_conversations: 0,
    total_commands_executed: 0,
    active_sessions: 0,
    success_rate: 0.0,
    avg_response_time_ms: 0.0,
    failed_interactions: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_conversations: 1247,
        total_commands_executed: 8934,
        active_sessions: 23,
        success_rate: 94.7,
        avg_response_time_ms: 245,
        failed_interactions: 89
      };

      this.activities = [
        { id: '1', action: 'Command Executed', actor: 'User', module: 'Voice Commands', description: 'Check attendance status', timestamp: new Date() },
        { id: '2', action: 'Conversation Started', actor: 'User', module: 'AI Conversations', description: 'New session initiated', timestamp: new Date() },
        { id: '3', action: 'System Optimized', actor: 'System', module: 'Settings', description: 'AI model parameters updated', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }

  refreshData() {
    this.isLoading = true;
    this.fetchDashboardData();
  }
}
