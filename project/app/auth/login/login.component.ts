import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Store } from '@ngxs/store';
import { AuthService } from '../../../core/services/auth.service';
import { Login } from '../../../core/state/auth.actions';
import { UserRole } from '../../../models';

interface RoleOption { label: string; role: UserRole; icon: string; color: string; }

@Component({
  selector: 'eims-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `
    <div class="login-bg">
      <!-- Animated background particles -->
      <div class="particles">
        <div class="particle" *ngFor="let p of particles" [style.left.%]="p.x" [style.top.%]="p.y" [style.animation-delay.s]="p.delay"></div>
      </div>

      <div class="login-container">
        <!-- Left panel -->
        <div class="login-left">
          <div class="brand">
            <div class="brand-icon">🎓</div>
            <div>
              <h1 class="brand-name">EIMS</h1>
              <p class="brand-sub">Educational Institution<br>Management System</p>
            </div>
          </div>

          <div class="features-list">
            <div class="feature-item" *ngFor="let f of features">
              <span class="feature-icon">{{ f.icon }}</span>
              <div>
                <div class="feature-title">{{ f.title }}</div>
                <div class="feature-desc">{{ f.desc }}</div>
              </div>
            </div>
          </div>

          <div class="hyderabad-badge">
            <span>🏙️</span>
            <span>Designed for Hyderabad Institutions</span>
          </div>
        </div>

        <!-- Right panel — Login form -->
        <div class="login-right">
          <div class="login-card">
            <h2 class="login-title">Welcome Back</h2>
            <p class="login-subtitle">Sign in to your EIMS account</p>

            <!-- Role selector -->
            <div class="role-selector">
              <button
                *ngFor="let r of roles"
                class="role-btn"
                [class.active]="selectedRole === r.role"
                [style.--role-color]="r.color"
                (click)="selectRole(r.role)"
                [id]="'role-' + r.role"
              >
                <span class="role-icon">{{ r.icon }}</span>
                <span class="role-label">{{ r.label }}</span>
              </button>
            </div>

            <form [formGroup]="loginForm" (ngSubmit)="onLogin()" class="login-form">
              <div class="form-group">
                <label for="email">Email Address</label>
                <div class="input-wrapper">
                  <span class="input-icon">✉️</span>
                  <input
                    id="email"
                    type="email"
                    formControlName="email"
                    placeholder="Enter your email"
                    class="form-control-dark"
                    autocomplete="email"
                  >
                </div>
                <span class="error-msg" *ngIf="loginForm.get('email')?.touched && loginForm.get('email')?.invalid">
                  Valid email required
                </span>
              </div>

              <div class="form-group">
                <label for="password">Password</label>
                <div class="input-wrapper">
                  <span class="input-icon">🔒</span>
                  <input
                    id="password"
                    [type]="showPassword ? 'text' : 'password'"
                    formControlName="password"
                    placeholder="Enter your password"
                    class="form-control-dark"
                    autocomplete="current-password"
                  >
                  <button type="button" class="toggle-pw" (click)="showPassword = !showPassword">
                    {{ showPassword ? '🙈' : '👁️' }}
                  </button>
                </div>
              </div>

              <div class="form-group" *ngIf="needsInstitutionCode">
                <label for="instCode">Institution Code</label>
                <div class="input-wrapper">
                  <span class="input-icon">🏫</span>
                  <input
                    id="instCode"
                    type="text"
                    formControlName="institution_code"
                    placeholder="e.g. DPS-HYD"
                    class="form-control-dark"
                  >
                </div>
              </div>

              <div class="form-extras">
                <label class="remember-me">
                  <input type="checkbox" formControlName="remember">
                  <span>Remember me</span>
                </label>
                <a routerLink="/forgot-password" class="forgot-link">Forgot password?</a>
              </div>

              <button
                type="submit"
                class="btn-primary-glow login-btn"
                id="btn-login"
                [disabled]="loading || loginForm.invalid"
              >
                <span *ngIf="!loading">Sign In →</span>
                <span *ngIf="loading" class="loading-dots">
                  <span></span><span></span><span></span>
                </span>
              </button>

              <div class="error-banner" *ngIf="errorMsg">{{ errorMsg }}</div>
            </form>

            <div class="demo-creds">
              <div class="demo-title">🚀 Quick Demo Login</div>
              <div class="demo-btns">
                <button *ngFor="let d of demoCreds" class="demo-btn" (click)="fillDemo(d)">{{ d.label }}</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .login-bg {
      min-height: 100vh;
      background: var(--bg-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      position: relative;
      overflow: hidden;
    }
    .particles { position: absolute; inset: 0; pointer-events: none; }
    .particle {
      position: absolute;
      width: 4px;
      height: 4px;
      background: var(--primary);
      border-radius: 50%;
      opacity: 0.3;
      animation: float 6s infinite ease-in-out;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0); opacity: 0.3; }
      50% { transform: translateY(-20px); opacity: 0.6; }
    }
    .login-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      max-width: 1000px;
      width: 100%;
      gap: 2rem;
      position: relative;
      z-index: 1;
    }
    .login-left {
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2rem;
      padding: 2rem;
    }
    .brand { display: flex; align-items: center; gap: 1rem; }
    .brand-icon {
      font-size: 3rem;
      width: 72px;
      height: 72px;
      background: var(--gradient-primary);
      border-radius: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-glow);
    }
    .brand-name { font-size: 2.5rem; font-weight: 800; background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .brand-sub { color: var(--text-muted); font-size: 0.9rem; line-height: 1.4; }
    .features-list { display: flex; flex-direction: column; gap: 1rem; }
    .feature-item { display: flex; align-items: flex-start; gap: 1rem; padding: 1rem; background: var(--bg-card); border-radius: var(--border-radius); border: 1px solid var(--border-color); }
    .feature-icon { font-size: 1.5rem; }
    .feature-title { font-weight: 600; font-size: 0.9rem; color: var(--text-primary); }
    .feature-desc { font-size: 0.8rem; color: var(--text-muted); }
    .hyderabad-badge { display: flex; align-items: center; gap: 0.5rem; color: var(--text-muted); font-size: 0.85rem; }
    .login-right { display: flex; align-items: center; justify-content: center; }
    .login-card {
      background: var(--bg-card);
      backdrop-filter: blur(20px);
      border: 1px solid var(--border-color);
      border-radius: var(--border-radius-xl);
      padding: 2.5rem;
      width: 100%;
      max-width: 440px;
    }
    .login-title { font-size: 1.75rem; font-weight: 800; color: var(--text-primary); margin-bottom: 0.25rem; }
    .login-subtitle { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem; }
    .role-selector { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; margin-bottom: 1.5rem; }
    .role-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
      padding: 0.625rem 0.5rem;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--border-radius);
      cursor: pointer;
      transition: var(--transition);
      color: var(--text-secondary);
      font-size: 0.7rem;
    }
    .role-btn.active {
      background: rgba(79, 70, 229, 0.2);
      border-color: var(--primary);
      color: var(--primary-light);
    }
    .role-icon { font-size: 1.25rem; }
    .role-label { font-weight: 500; }
    .form-group { display: flex; flex-direction: column; gap: 0.375rem; margin-bottom: 1rem; }
    .form-group label { font-size: 0.85rem; font-weight: 600; color: var(--text-secondary); }
    .input-wrapper { position: relative; }
    .input-icon { position: absolute; left: 0.875rem; top: 50%; transform: translateY(-50%); font-size: 1rem; }
    .input-wrapper .form-control-dark { padding-left: 2.75rem; }
    .toggle-pw { position: absolute; right: 0.875rem; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; font-size: 1rem; }
    .error-msg { color: var(--danger); font-size: 0.75rem; }
    .form-extras { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
    .remember-me { display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--text-secondary); cursor: pointer; }
    .forgot-link { color: var(--primary-light); font-size: 0.85rem; text-decoration: none; }
    .forgot-link:hover { text-decoration: underline; }
    .login-btn { width: 100%; justify-content: center; padding: 0.875rem; font-size: 1rem; margin-bottom: 1rem; }
    .error-banner { background: rgba(239,68,68,0.15); border: 1px solid rgba(239,68,68,0.3); color: #ef4444; padding: 0.75rem; border-radius: var(--border-radius); font-size: 0.85rem; }
    .loading-dots { display: flex; gap: 0.35rem; align-items: center; }
    .loading-dots span { width: 8px; height: 8px; background: white; border-radius: 50%; animation: bounce 0.6s infinite alternate; }
    .loading-dots span:nth-child(2) { animation-delay: 0.2s; }
    .loading-dots span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce { from { transform: translateY(0); } to { transform: translateY(-6px); } }
    .demo-creds { border-top: 1px solid var(--border-color); padding-top: 1rem; }
    .demo-title { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.5rem; }
    .demo-btns { display: flex; flex-wrap: wrap; gap: 0.375rem; }
    .demo-btn { padding: 0.25rem 0.625rem; background: rgba(79,70,229,0.15); border: 1px solid rgba(79,70,229,0.3); border-radius: 999px; font-size: 0.7rem; color: var(--primary-light); cursor: pointer; transition: var(--transition-fast); }
    .demo-btn:hover { background: rgba(79,70,229,0.25); }
    @media (max-width: 768px) {
      .login-container { grid-template-columns: 1fr; }
      .login-left { display: none; }
      .login-card { max-width: 100%; padding: 1.5rem; }
    }
  `],
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  loading = false;
  errorMsg = '';
  showPassword = false;
  selectedRole: UserRole = 'student';

  particles = Array.from({ length: 20 }, (_, i) => ({
    x: Math.random() * 100,
    y: Math.random() * 100,
    delay: Math.random() * 6,
  }));

  features = [
    { icon: '🤖', title: 'AI Face Recognition', desc: 'Automated attendance with biometric verification' },
    { icon: '📱', title: 'Virtual ID Cards', desc: 'QR-based digital ID for all students & staff' },
    { icon: '📊', title: 'Smart Analytics', desc: 'At-risk prediction & learning insights' },
    { icon: '💬', title: 'Real-time Communication', desc: 'WebSocket chat, PTM booking & notifications' },
  ];

  roles: RoleOption[] = [
    { label: 'Super Admin', role: 'super_admin', icon: '👑', color: '#f59e0b' },
    { label: 'Institution', role: 'institution_admin', icon: '🏫', color: '#4f46e5' },
    { label: 'Faculty', role: 'faculty', icon: '👨‍🏫', color: '#06b6d4' },
    { label: 'Ed Official', role: 'ed_official', icon: '🏛️', color: '#8b5cf6' },
    { label: 'Student', role: 'student', icon: '📚', color: '#10b981' },
    { label: 'Parent', role: 'parent', icon: '👪', color: '#f97316' },
  ];

  demoCreds = [
    { label: 'Super Admin', email: 'super@eims.in', password: 'Admin@123', role: 'super_admin' as UserRole },
    { label: 'Institution Admin', email: 'admin@dps.edu.in', password: 'Admin@123', role: 'institution_admin' as UserRole },
    { label: 'Faculty', email: 'teacher@dps.edu.in', password: 'Faculty@123', role: 'faculty' as UserRole },
    { label: 'Student', email: 'student@dps.edu.in', password: 'Student@123', role: 'student' as UserRole },
    { label: 'Parent', email: 'parent@gmail.com', password: 'Parent@123', role: 'parent' as UserRole },
  ];

  get needsInstitutionCode(): boolean {
    return ['institution_admin', 'faculty', 'student', 'parent'].includes(this.selectedRole);
  }

  private roleDashboard: Record<UserRole, string> = {
    super_admin: '/super-admin/dashboard',
    institution_admin: '/institution-admin/dashboard',
    faculty: '/faculty/dashboard',
    ed_official: '/ed-officials/dashboard',
    student: '/student/dashboard',
    parent: '/parent/dashboard',
  };

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private store: Store,
    private router: Router,
    private route: ActivatedRoute,
  ) {}

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      institution_code: [''],
      remember: [false],
    });
  }

  selectRole(role: UserRole): void {
    this.selectedRole = role;
  }

  fillDemo(cred: { email: string; password: string; role: UserRole }): void {
    this.selectedRole = cred.role;
    this.loginForm.patchValue({ email: cred.email, password: cred.password });
  }

  async onLogin(): Promise<void> {
    if (this.loginForm.invalid) return;
    this.loading = true;
    this.errorMsg = '';

    try {
      const response = await this.authService.login(this.loginForm.value).toPromise();
      if (response) {
        this.store.dispatch(new Login(response));
        const returnUrl = this.route.snapshot.queryParams['returnUrl'];
        this.router.navigate([returnUrl || this.roleDashboard[response.role]]);
      }
    } catch (err: any) {
      this.errorMsg = err?.error?.detail || 'Login failed. Please check your credentials.';
    } finally {
      this.loading = false;
    }
  }
}
