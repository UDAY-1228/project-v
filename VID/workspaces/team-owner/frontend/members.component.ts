import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-members',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent implements OnInit {
  members: any[] = [];
  invitations: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData() {
    setTimeout(() => {
      this.members = [
        { id: '1', name: 'John Doe', email: 'john@example.com', role: 'admin', workspace: 'Academic', last_active: new Date() },
        { id: '2', name: 'Jane Smith', email: 'jane@example.com', role: 'editor', workspace: 'Academic', last_active: new Date() },
        { id: '3', name: 'Bob Wilson', email: 'bob@example.com', role: 'viewer', workspace: 'Examination', last_active: new Date() },
      ];
      this.invitations = [
        { id: '1', email: 'new1@example.com', role: 'viewer', status: 'pending' },
        { id: '2', email: 'new2@example.com', role: 'editor', status: 'pending' },
      ];
      this.isLoading = false;
    }, 600);
  }

  sendInvitation() { console.log('Sending invitation...'); }
  removeMember(id: string) { console.log('Removing:', id); }
}
