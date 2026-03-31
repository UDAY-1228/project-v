import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-player-records',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './player-records.component.html',
  styleUrls: ['./player-records.component.css']
})
export class PlayerRecordsComponent implements OnInit {
  players: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadPlayers();
  }

  loadPlayers() {
    setTimeout(() => {
      this.players = [
        { id: '1', name: 'Alex Thompson', team: 'Thunder FC', position: 'Forward', jersey: 10, goals: 15, assists: 8, matches: 20 },
        { id: '2', name: 'Mike Johnson', team: 'Spartans', position: 'Center', jersey: 23, goals: 12, assists: 5, matches: 18 },
        { id: '3', name: 'Chris Williams', team: 'Royal Strikers', position: 'Batsman', jersey: 7, goals: 25, assists: 10, matches: 15 },
      ];
      this.isLoading = false;
    }, 800);
  }
}
