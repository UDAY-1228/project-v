import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'eims-forgot-password',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div class="stagger-children">
      <div class="page-header">
        <h1 class="page-title-text">🔐 Forgot Password</h1>
      </div>
      <div class="card-glass" style="text-align:center;padding:3rem">
        <div style="font-size:3rem;margin-bottom:1rem">🚧</div>
        <h2 style="color:var(--text-primary)">Coming Soon</h2>
        <p style="color:var(--text-muted)">This page is under development.</p>
        <a routerLink="/" style="color:var(--primary-light)">← Go Back</a>
      </div>
    </div>
  `,
  styles: [`.page-header{margin-bottom:1.5rem;} .page-title-text{font-size:1.75rem;font-weight:800;color:var(--text-primary);}`]
})
export class ForgotPasswordComponent {}
