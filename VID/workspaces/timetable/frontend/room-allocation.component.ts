import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-room-allocation',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './room-allocation.component.html',
  styleUrls: ['./room-allocation.component.css']
})
export class RoomAllocationComponent implements OnInit {
  rooms: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchRooms();
  }

  fetchRooms() {
    setTimeout(() => {
      this.rooms = [
        { id: '1', name: 'Room 101', building: 'Block A', capacity: 60, type: 'classroom', status: 'available' },
        { id: '2', name: 'Lab 1', building: 'Block B', capacity: 40, type: 'lab', status: 'allocated' },
        { id: '3', name: 'Room 202', building: 'Block A', capacity: 80, type: 'classroom', status: 'available' },
      ];
      this.isLoading = false;
    }, 600);
  }

  allocateRoom() { console.log('Allocating room...'); }
}
