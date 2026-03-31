import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-workspace-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './workspace-control.component.html',
  styleUrls: ['./workspace-control.component.css']
})
export class WorkspaceControlComponent implements OnInit {
  workspaces: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchWorkspaces();
  }

  fetchWorkspaces() {
    setTimeout(() => {
      this.workspaces = [
        { id: '1', name: 'Academic Portal', code: 'ACAD', type: 'standard', members: 45, status: 'active' },
        { id: '2', name: 'Examination Cell', code: 'EXAM', type: 'standard', members: 30, status: 'active' },
        { id: '3', name: 'Research Hub', code: 'RESH', type: 'premium', members: 25, status: 'suspended' },
      ];
      this.isLoading = false;
    }, 600);
  }

  createWorkspace() { console.log('Creating workspace...'); }
  suspendWorkspace(id: string) { console.log('Suspending:', id); }
}
