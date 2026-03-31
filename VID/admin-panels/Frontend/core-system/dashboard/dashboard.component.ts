import { Component } from '@angular/core';

@Component({
  selector: 'app-core-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  userProfile = {
    role: 'Student',
    email: 'user@example.com'
  };
  accessList = [
    { name: 'Computer Science Dept', description: 'Access to department-specific resources.' },
    { name: 'Student Library Portal', description: 'Search and reserve books.' }
  ];
  constructor() {}
  logout() {
    console.log('Logging out of Core System...');
  }
}
