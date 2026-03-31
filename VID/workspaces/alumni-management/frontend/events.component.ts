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
        { id: '1', eventName: 'Annual Gala 2026', eventType: 'Gala', description: 'Annual fundraising gala', date: new Date('2026-04-15'), registeredCount: 200, status: 'active' },
        { id: '2', eventName: 'Alumni Reunion', eventType: 'Reunion', description: 'Batch of 2015 reunion', date: new Date('2026-05-10'), registeredCount: 80, status: 'active' },
        { id: '3', eventName: 'Career Fair', eventType: 'Career', description: 'Connect alumni with students', date: new Date('2026-04-20'), registeredCount: 150, status: 'draft' },
        { id: '4', eventName: ' Golf Tournament', eventType: 'Sports', description: 'Annual alumni golf event', date: new Date('2026-06-01'), registeredCount: 50, status: 'draft' }
      ];
      this.isLoading = false;
    }, 500);
  }
}
