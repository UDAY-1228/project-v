import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-access-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './access-control.component.html',
  styleUrls: ['./access-control.component.css']
})
export class AccessControlComponent implements OnInit {
  roles: any[] = [];
  permissions: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData() {
    setTimeout(() => {
      this.roles = [
        { id: '1', name: 'Admin', code: 'ADMIN', description: 'Full access', member_count: 5 },
        { id: '2', name: 'Editor', code: 'EDITOR', description: 'Can edit content', member_count: 20 },
        { id: '3', name: 'Viewer', code: 'VIEWER', description: 'Read-only access', member_count: 50 },
      ];
      this.isLoading = false;
    }, 600);
  }

  createRole() { console.log('Creating role...'); }
  managePermissions(roleId: string) { console.log('Managing:', roleId); }
}
