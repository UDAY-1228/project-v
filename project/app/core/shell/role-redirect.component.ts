import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Store } from '@ngxs/store';
import { AuthState } from '../state/auth.state';
import { UserRole } from '../../models';

@Component({
  selector: 'eims-role-redirect',
  standalone: true,
  template: `<div class="loading-screen"><div class="spinner"></div></div>`,
  styles: [`.loading-screen { display:flex; justify-content:center; align-items:center; min-height:60vh; } .spinner { width:40px; height:40px; border:3px solid var(--border-color); border-top-color:var(--primary); border-radius:50%; animation:spin 0.8s linear infinite; } @keyframes spin { to { transform:rotate(360deg); } }`],
})
export class RoleRedirectComponent implements OnInit {
  private readonly dashboards: Record<UserRole, string> = {
    super_admin: '/super-admin/dashboard',
    institution_admin: '/institution-admin/dashboard',
    faculty: '/faculty/dashboard',
    ed_official: '/ed-officials/dashboard',
    student: '/student/dashboard',
    parent: '/parent/dashboard',
  };

  constructor(private store: Store, private router: Router) {}

  ngOnInit(): void {
    const role = this.store.selectSnapshot(AuthState.role) as UserRole;
    this.router.navigate([this.dashboards[role] ?? '/login']);
  }
}
