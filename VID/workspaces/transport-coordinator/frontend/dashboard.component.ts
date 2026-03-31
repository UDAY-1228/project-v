import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-transport-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    total_vehicles: 0,
    active_vehicles: 0,
    total_routes: 0,
    total_students_transported: 0,
    pending_maintenance: 0,
    active_trips: 0
  };

  routes: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_vehicles: 25,
        active_vehicles: 20,
        total_routes: 15,
        total_students_transported: 450,
        pending_maintenance: 3,
        active_trips: 8
      };

      this.routes = [
        { id: '1', route_name: 'Route A', start_point: 'Main Gate', end_point: 'Campus', active_vehicles: 5 },
        { id: '2', route_name: 'Route B', start_point: 'City Center', end_point: 'Campus', active_vehicles: 3 },
        { id: '3', route_name: 'Route C', start_point: 'Residential Area', end_point: 'Campus', active_vehicles: 4 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
