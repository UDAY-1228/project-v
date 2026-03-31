import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sports-teams',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './teams.component.html',
  styleUrls: ['./teams.component.css']
})
export class TeamsComponent implements OnInit {
  teams: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadTeams();
  }

  loadTeams() {
    setTimeout(() => {
      this.teams = [
        { id: '1', name: 'Thunder FC', sport: 'Football', code: 'THF', members: 22, wins: 8, losses: 2, draws: 3 },
        { id: '2', name: 'Spartans', sport: 'Basketball', code: 'SPT', members: 15, wins: 12, losses: 1, draws: 0 },
        { id: '3', name: 'Royal Strikers', sport: 'Cricket', code: 'RYS', members: 18, wins: 6, losses: 3, draws: 1 },
      ];
      this.isLoading = false;
    }, 800);
  }
}
