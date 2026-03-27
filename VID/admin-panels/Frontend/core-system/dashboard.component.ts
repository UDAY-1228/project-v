import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-core-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    notifications: 5,
    upcoming_classes: 2,
    attendance: '98%'
  };

  constructor() { }

  ngOnInit(): void {
    // Core activity tracking
  }
}
