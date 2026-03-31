import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sports-events',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './sports-events.component.html',
  styleUrls: ['./sports-events.component.css']
})
export class SportsEventsComponent implements OnInit {
  events: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadEvents();
  }

  loadEvents() {
    setTimeout(() => {
      this.events = [
        { id: '1', name: 'Inter-College Football Cup', type: 'Tournament', sport: 'Football', startDate: new Date(), venue: 'Main Stadium', status: 'upcoming', participants: 16 },
        { id: '2', name: 'Basketball League', type: 'League', sport: 'Basketball', startDate: new Date(), venue: 'Sports Complex', status: 'ongoing', participants: 8 },
        { id: '3', name: 'Cricket Championship', type: 'Tournament', sport: 'Cricket', startDate: new Date(), venue: 'Cricket Ground', status: 'completed', participants: 12 },
      ];
      this.isLoading = false;
    }, 800);
  }

  getStatusClass(status: string): string {
    const classes: any = { upcoming: 'text-blue-400 bg-blue-400/10', ongoing: 'text-orange-400 bg-orange-400/10', completed: 'text-emerald-400 bg-emerald-400/10' };
    return classes[status] || 'text-zinc-400 bg-zinc-400/10';
  }
}
