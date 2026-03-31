import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-events',
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
        { id: '1', eventName: 'Annual Alumni Meet 2026', eventType: 'Reunion', description: 'Annual gathering of all alumni', date: new Date('2026-03-15'), registeredCount: 150, status: 'active' },
        { id: '2', eventName: 'Networking Night', eventType: 'Networking', description: 'Professional networking session', date: new Date('2026-04-10'), registeredCount: 75, status: 'active' },
        { id: '3', eventName: 'Guest Lecture Series', eventType: 'Academic', description: 'Industry experts sharing insights', date: new Date('2026-04-20'), registeredCount: 200, status: 'draft' },
        { id: '4', eventName: 'Sports Day', eventType: 'Sports', description: 'Inter-batch sports competition', date: new Date('2026-05-05'), registeredCount: 120, status: 'draft' }
      ];
      this.isLoading = false;
    }, 500);
  }
}
