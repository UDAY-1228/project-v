import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { Store } from '@ngxs/store';
import { AuthState } from '../state/auth.state';
import { UserRole } from '../../models';

export const roleGuard: CanActivateFn = (route, state) => {
  const store = inject(Store);
  const router = inject(Router);
  const currentRole = store.selectSnapshot(AuthState.role) as UserRole;
  const allowedRoles: UserRole[] = route.data?.['roles'] ?? [];

  if (!allowedRoles.includes(currentRole)) {
    // Redirect to user's own dashboard
    const roleDashboard: Record<UserRole, string> = {
      super_admin: '/super-admin/dashboard',
      institution_admin: '/institution-admin/dashboard',
      faculty: '/faculty/dashboard',
      ed_official: '/ed-officials/dashboard',
      student: '/student/dashboard',
      parent: '/parent/dashboard',
    };
    router.navigate([roleDashboard[currentRole] ?? '/login']);
    return false;
  }
  return true;
};
