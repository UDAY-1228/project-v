import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-hostel-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_rooms: 0,
    occupied_rooms: 0,
    vacant_rooms: 0,
    total_students: 0,
    pending_complaints: 0,
    pending_fees: 0,
    occupancy_rate: 0
  };

  blocks: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_rooms: 120,
        occupied_rooms: 95,
        vacant_rooms: 25,
        total_students: 380,
        pending_complaints: 8,
        pending_fees: 15,
        occupancy_rate: 79
      };

      this.blocks = [
        { block_name: 'Block A', occupied: 45, total: 50, occupancy_rate: 90 },
        { block_name: 'Block B', occupied: 30, total: 40, occupancy_rate: 75 },
        { block_name: 'Block C', occupied: 20, total: 30, occupancy_rate: 67 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
