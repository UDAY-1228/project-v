import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  stats = {
    users: 250,
    active_workspaces: 12,
    permission_requests: 3
  };

  constructor() { }

  ngOnInit(): void {
    // Admin analytics logic
  }
}
