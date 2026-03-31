import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-rooms',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './rooms.component.html',
  styleUrls: ['./rooms.component.css']
})
export class RoomsComponent implements OnInit {
  rooms: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.rooms = [
      { id: '1', room_number: 'A101', block_name: 'Block A', floor: 1, room_type: 'shared', current_occupancy: 4, capacity: 4, rent_per_student: 5000, status: 'occupied' },
      { id: '2', room_number: 'A102', block_name: 'Block A', floor: 1, room_type: 'shared', current_occupancy: 2, capacity: 4, rent_per_student: 5000, status: 'vacant' },
      { id: '3', room_number: 'B201', block_name: 'Block B', floor: 2, room_type: 'single', current_occupancy: 1, capacity: 1, rent_per_student: 8000, status: 'occupied' }
    ];
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      occupied: 'bg-emerald-500/10 text-emerald-400',
      vacant: 'bg-amber-500/10 text-amber-400',
      maintenance: 'bg-red-500/10 text-red-400'
    };
    return classes[status] || classes.vacant;
  }
}
