import { Component } from '@angular/core';

@Component({
  selector: 'app-user-management',
  templateUrl: './user-management.component.html',
  styleUrls: ['./user-management.component.css']
})
export class UserManagementComponent {
  users = [
    { username: 'john_doe', role: 'student', is_active: true },
    { username: 'jane_smith', role: 'faculty', is_active: true }
  ];

  createUser() {}
  manageUser(id: string) {}
  assignWorkspaces(id: string) {}
  updateUser(id: string) {}
  deactivateUser(id: string) {}
}
