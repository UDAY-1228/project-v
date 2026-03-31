import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sports-officer-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_events: 0,
    upcoming_events: 0,
    total_teams: 0,
    total_players: 0,
    completed_matches: 0,
    active_tournaments: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_events: 24,
        upcoming_events: 5,
        total_teams: 18,
        total_players: 360,
        completed_matches: 45,
        active_tournaments: 3
      };

      this.activities = [
        { id: '1', action: 'Match Completed', actor: 'Referee', module: 'Events', description: 'Final match of Soccer League', timestamp: new Date() },
        { id: '2', action: 'Team Registered', actor: 'Admin', module: 'Teams', description: 'New team added to Basketball league', timestamp: new Date() },
        { id: '3', action: 'Tournament Started', actor: 'System', module: 'Events', description: 'Inter-college Cricket Cup begins', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
