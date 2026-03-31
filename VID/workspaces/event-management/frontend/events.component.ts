import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-management-events',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {
  events: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadEvents();
  }

  loadEvents() {
    setTimeout(() => {
      this.events = [
        { id: '1', name: 'Annual Tech Conference', type: 'Conference', startDate: new Date(), venue: 'Main Hall', status: 'upcoming', registrations: 250, capacity: 300 },
        { id: '2', name: 'Startup Pitch Night', type: 'Networking', startDate: new Date(), venue: 'Innovation Hub', status: 'ongoing', registrations: 80, capacity: 100 },
        { id: '3', name: 'Leadership Workshop', type: 'Workshop', startDate: new Date(), venue: 'Training Center', status: 'completed', registrations: 45, capacity: 50 },
      ];
      this.isLoading = false;
    }, 800);
  }

  getStatusClass(status: string): string {
    const classes: any = { upcoming: 'text-blue-400 bg-blue-400/10', ongoing: 'text-violet-400 bg-violet-400/10', completed: 'text-emerald-400 bg-emerald-400/10' };
    return classes[status] || 'text-zinc-400 bg-zinc-400/10';
  }
}
