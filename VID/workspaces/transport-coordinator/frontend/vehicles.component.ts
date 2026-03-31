import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vehicles',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './vehicles.component.html',
  styleUrls: ['./vehicles.component.css']
})
export class VehiclesComponent implements OnInit {
  vehicles: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.vehicles = [
      { id: '1', vehicle_number: 'MH12AB1234', vehicle_type: 'Bus', driver_name: 'Ramesh Singh', capacity: 45, status: 'active' },
      { id: '2', vehicle_number: 'MH12CD5678', vehicle_type: 'Van', driver_name: 'Suresh Patel', capacity: 15, status: 'maintenance' },
      { id: '3', vehicle_number: 'MH12EF9012', vehicle_type: 'Bus', driver_name: 'Vikram Sharma', capacity: 50, status: 'active' }
    ];
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      active: 'bg-emerald-500/10 text-emerald-400',
      maintenance: 'bg-amber-500/10 text-amber-400',
      inactive: 'bg-zinc-500/10 text-zinc-400'
    };
    return classes[status] || classes.inactive;
  }
}
