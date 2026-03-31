import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-routes',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './routes.component.html',
  styleUrls: ['./routes.component.css']
})
export class RoutesComponent implements OnInit {
  routes: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.routes = [
      { id: '1', route_name: 'Route A', start_point: 'Main Gate', end_point: 'Campus', distance_km: 5.2, total_students_assigned: 45 },
      { id: '2', route_name: 'Route B', start_point: 'City Center', end_point: 'Campus', distance_km: 12.5, total_students_assigned: 60 },
      { id: '3', route_name: 'Route C', start_point: 'Residential Area', end_point: 'Campus', distance_km: 8.0, total_students_assigned: 35 }
    ];
  }
}
