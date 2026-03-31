import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-scheduling',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './scheduling.component.html',
  styleUrls: ['./scheduling.component.css']
})
export class SchedulingComponent implements OnInit {
  schedules: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadSchedules();
  }

  loadSchedules() {
    setTimeout(() => {
      this.schedules = [
        { id: '1', event: 'Tech Conference', date: new Date(), slots: 5 },
        { id: '2', event: 'Startup Pitch', date: new Date(), slots: 3 },
        { id: '3', event: 'Leadership Workshop', date: new Date(), slots: 4 },
      ];
      this.isLoading = false;
    }, 800);
  }
}
