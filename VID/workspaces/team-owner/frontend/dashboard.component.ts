import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-team-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class TeamDashboardComponent implements OnInit {
  stats = {
    total_workspaces: 0,
    total_members: 0,
    active_members: 0,
    pending_invitations: 0,
    total_roles: 0,
    access_logs: 0
  };

  activities: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchDashboardData();
  }

  fetchDashboardData() {
    setTimeout(() => {
      this.stats = {
        total_workspaces: 5,
        total_members: 150,
        active_members: 120,
        pending_invitations: 10,
        total_roles: 8,
        access_logs: 450
      };
      this.activities = [
        { id: '1', action: 'Member Added', actor: 'Admin', module: 'Members', description: 'New member joined workspace', timestamp: new Date() },
        { id: '2', action: 'Role Updated', actor: 'Owner', module: 'Access Control', description: 'Editor role permissions updated', timestamp: new Date() },
        { id: '3', action: 'Invitation Sent', actor: 'Admin', module: 'Members', description: '3 invitations pending acceptance', timestamp: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
