import { Component, OnInit, HostListener, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule, NavigationEnd } from '@angular/router';
import { Store } from '@ngxs/store';
import { filter } from 'rxjs/operators';
import { AuthState } from '../state/auth.state';
import { Logout } from '../state/auth.actions';
import { UserRole, User } from '../../models';

interface NavItem { label: string; icon: string; route: string; badge?: number; }

@Component({
  selector: 'eims-shell',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div class="eims-layout">
      <!-- Mobile overlay -->
      <div class="sidebar-overlay" [class.open]="sidebarOpen()" (click)="sidebarOpen.set(false)"></div>

      <!-- Sidebar -->
      <aside class="eims-sidebar" [class.open]="sidebarOpen()">
        <!-- Logo -->
        <div class="sidebar-logo">
          <div class="sidebar-logo-icon">🎓</div>
          <div>
            <div class="sidebar-logo-text">EIMS</div>
            <div class="sidebar-logo-sub">{{ user()?.role | titlecase | replace:'_':' ' }}</div>
          </div>
        </div>

        <!-- User mini profile -->
        <div class="sidebar-user">
          <div class="user-avatar">{{ user()?.full_name?.charAt(0) || '?' }}</div>
          <div class="user-info">
            <div class="user-name">{{ user()?.full_name }}</div>
            <div class="user-email">{{ user()?.email }}</div>
          </div>
        </div>

        <!-- Navigation -->
        <nav class="sidebar-nav">
          <div *ngFor="let section of navSections">
            <div class="nav-section-title">{{ section.title }}</div>
            <a
              *ngFor="let item of section.items"
              class="nav-item-link"
              [routerLink]="item.route"
              routerLinkActive="active"
              (click)="sidebarOpen.set(false)"
            >
              <span class="material-icons">{{ item.icon }}</span>
              <span>{{ item.label }}</span>
              <span class="nav-badge" *ngIf="item.badge">{{ item.badge }}</span>
            </a>
          </div>
        </nav>

        <!-- Logout -->
        <div class="sidebar-footer">
          <button class="nav-item-link logout-btn" id="btn-logout" (click)="onLogout()">
            <span class="material-icons">logout</span>
            <span>Logout</span>
          </button>
          <div class="sidebar-version">v1.0.0 · Hyderabad, India</div>
        </div>
      </aside>

      <!-- Main Content -->
      <div class="eims-content">
        <!-- Top Header -->
        <header class="eims-header">
          <button class="hamburger" id="btn-toggle-sidebar" (click)="sidebarOpen.set(!sidebarOpen())">
            <span class="material-icons">{{ sidebarOpen() ? 'close' : 'menu' }}</span>
          </button>

          <span class="page-title">{{ pageTitle }}</span>

          <div class="header-spacer"></div>

          <!-- Header actions -->
          <div class="header-actions">
            <button class="header-btn" id="btn-notifications" routerLink="/notifications">
              <span class="material-icons">notifications</span>
              <span class="notif-dot" *ngIf="unreadNotifications > 0">{{ unreadNotifications }}</span>
            </button>
            <button class="header-btn" id="btn-chat" routerLink="/chat">
              <span class="material-icons">chat</span>
            </button>
            <button class="header-btn" id="btn-profile" routerLink="/profile">
              <div class="user-avatar-sm">{{ user()?.full_name?.charAt(0) || '?' }}</div>
            </button>
          </div>
        </header>

        <!-- Page Content -->
        <main class="eims-main">
          <router-outlet></router-outlet>
        </main>
      </div>
    </div>
  `,
  styles: [`
    .sidebar-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.5);
      z-index: 999;
      backdrop-filter: blur(2px);
    }
    @media (max-width: 992px) {
      .sidebar-overlay.open { display: block; }
    }
    .sidebar-user {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 1rem 1.5rem;
      border-bottom: 1px solid var(--border-color);
      background: rgba(79,70,229,0.05);
    }
    .user-avatar {
      width: 40px; height: 40px;
      background: var(--gradient-primary);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-weight: 700; font-size: 1.1rem; color: white;
      flex-shrink: 0;
    }
    .user-name { font-size: 0.875rem; font-weight: 600; color: var(--text-primary); }
    .user-email { font-size: 0.7rem; color: var(--text-muted); }
    .sidebar-nav { flex: 1; overflow-y: auto; padding: 0.5rem 0; }
    .nav-badge {
      margin-left: auto;
      background: var(--danger);
      color: white;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 0.15rem 0.45rem;
      border-radius: 999px;
    }
    .eims-sidebar { display: flex; flex-direction: column; }
    .sidebar-footer {
      padding: 1rem;
      border-top: 1px solid var(--border-color);
    }
    .logout-btn { color: #ef4444 !important; }
    .logout-btn:hover { background: rgba(239,68,68,0.1) !important; }
    .sidebar-version { font-size: 0.65rem; color: var(--text-muted); text-align: center; margin-top: 0.5rem; }
    .hamburger {
      background: none;
      border: none;
      color: var(--text-primary);
      cursor: pointer;
      padding: 0.25rem;
      border-radius: 8px;
      transition: var(--transition-fast);
      display: flex;
    }
    .hamburger:hover { background: var(--bg-card); }
    .page-title { font-weight: 700; font-size: 1.1rem; margin-left: 1rem; }
    .header-spacer { flex: 1; }
    .header-actions { display: flex; align-items: center; gap: 0.5rem; }
    .header-btn {
      position: relative;
      background: none;
      border: none;
      color: var(--text-secondary);
      cursor: pointer;
      padding: 0.5rem;
      border-radius: 10px;
      transition: var(--transition-fast);
      display: flex;
    }
    .header-btn:hover { background: var(--bg-card); color: var(--text-primary); }
    .notif-dot {
      position: absolute;
      top: 2px; right: 2px;
      background: var(--danger);
      color: white;
      font-size: 0.6rem;
      font-weight: 700;
      min-width: 16px;
      height: 16px;
      border-radius: 999px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 3px;
    }
    .user-avatar-sm {
      width: 32px; height: 32px;
      background: var(--gradient-primary);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-weight: 700; font-size: 0.9rem; color: white;
    }
  `],
})
export class ShellComponent implements OnInit {
  sidebarOpen = signal(false);
  pageTitle = 'Dashboard';
  unreadNotifications = 3;

  user = this.store.selectSignal(AuthState.user);
  role = this.store.selectSignal(AuthState.role);

  navSections: { title: string; items: NavItem[] }[] = [];

  private readonly roleNavMap: Partial<Record<UserRole, { title: string; items: NavItem[] }[]>> = {
    student: [
      {
        title: 'My Learning',
        items: [
          { label: 'Dashboard', icon: 'dashboard', route: '/student/dashboard' },
          { label: 'Timetable', icon: 'schedule', route: '/student/timetable' },
          { label: 'Attendance', icon: 'how_to_reg', route: '/student/attendance' },
          { label: 'My Courses', icon: 'book', route: '/student/lms' },
          { label: 'Assignments', icon: 'assignment', route: '/student/assignments' },
          { label: 'AI Homework', icon: 'psychology', route: '/student/homework-helper', badge: 0 },
        ],
      },
      {
        title: 'Exams & Fees',
        items: [
          { label: 'Exams', icon: 'quiz', route: '/student/exams' },
          { label: 'Results', icon: 'grade', route: '/student/results' },
          { label: 'Fee Payment', icon: 'payment', route: '/student/fees' },
          { label: 'Virtual ID', icon: 'badge', route: '/student/virtual-id' },
        ],
      },
    ],
  };

  constructor(private store: Store, private router: Router) {}

  ngOnInit(): void {
    const role = this.role() as UserRole;
    this.navSections = this.roleNavMap[role] ?? [];

    this.router.events.pipe(filter(e => e instanceof NavigationEnd)).subscribe(() => {
      this.updatePageTitle();
    });
    this.updatePageTitle();
  }

  @HostListener('window:resize')
  onResize() {
    if (window.innerWidth > 992) this.sidebarOpen.set(true);
  }

  private updatePageTitle(): void {
    const url = this.router.url;
    const allItems = this.navSections.flatMap(s => s.items);
    const match = allItems.find(i => url.startsWith(i.route));
    this.pageTitle = match?.label ?? 'Dashboard';
  }

  onLogout(): void {
    this.store.dispatch(new Logout());
    this.router.navigate(['/login']);
  }
}
