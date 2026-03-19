import { Component, OnInit } from '@angular/core';
import { CommonModule, DecimalPipe } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../environments/environment';

@Component({
  selector: 'eims-sa-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule, DecimalPipe],
  template: `
    <div class="stagger-children">
      <!-- Page header -->
      <div class="page-header">
        <div>
          <h1 class="page-title-text">Platform Overview</h1>
          <p class="page-subtitle">EIMS Super Admin — Hyderabad, India</p>
        </div>
        <div class="header-actions">
          <button class="btn-ghost" id="btn-export" (click)="exportReport()">
            <span class="material-icons" style="font-size:1rem">download</span> Export
          </button>
          <button class="btn-primary-glow" id="btn-add-institution" routerLink="/super-admin/institutions">
            <span class="material-icons" style="font-size:1rem">add</span> Add Institution
          </button>
        </div>
      </div>

      <!-- KPI Stats -->
      <div class="stats-grid">
        <div class="card-stat" *ngFor="let stat of stats">
          <div class="d-flex justify-content-between align-items-start">
            <div>
              <div class="stat-label">{{ stat.label }}</div>
              <div class="stat-value">{{ stat.value | number }}</div>
              <div class="stat-change" [class.up]="stat.changePositive" [class.down]="!stat.changePositive">
                {{ stat.changePositive ? '↑' : '↓' }} {{ stat.change }}
              </div>
            </div>
            <div class="stat-icon" [style.background]="stat.iconBg">{{ stat.icon }}</div>
          </div>
        </div>
      </div>

      <!-- Charts row -->
      <div class="grid-2">
        <!-- Institutions by type -->
        <div class="card-glass">
          <h3 class="section-title">Institutions by Type</h3>
          <div class="chart-bars">
            <div class="chart-bar-item" *ngFor="let item of institutionTypes">
              <div class="bar-label">{{ item.label }}</div>
              <div class="bar-track">
                <div class="bar-fill" [style.width.%]="item.pct" [style.background]="item.color"></div>
              </div>
              <div class="bar-value">{{ item.count }}</div>
            </div>
          </div>
        </div>

        <!-- Monthly enrollment -->
        <div class="card-glass">
          <h3 class="section-title">Monthly Student Enrollments</h3>
          <div class="sparkline-chart">
            <div class="sparkline-bars">
              <div
                class="sparkline-bar"
                *ngFor="let m of monthlyEnrollment"
                [style.height.%]="(m.count / maxEnrollment) * 100"
                [title]="m.month + ': ' + m.count"
              ></div>
            </div>
            <div class="sparkline-labels">
              <span *ngFor="let m of monthlyEnrollment">{{ m.month }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Institutions Table -->
      <div class="card-glass">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h3 class="section-title">Recent Institutions</h3>
          <a routerLink="/super-admin/institutions" class="view-all-link">View All →</a>
        </div>
        <div class="table-responsive">
          <table class="table-dark-custom">
            <thead>
              <tr>
                <th>Institution</th>
                <th>Code</th>
                <th>Type</th>
                <th>Students</th>
                <th>Attendance Today</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr *ngFor="let inst of recentInstitutions; let i = index">
                <td>
                  <div class="inst-name">{{ inst.name }}</div>
                  <div class="inst-location">📍 {{ inst.city }}</div>
                </td>
                <td><code class="code-badge">{{ inst.code }}</code></td>
                <td>{{ inst.type }}</td>
                <td>{{ inst.students | number }}</td>
                <td>
                  <div class="attendance-bar">
                    <div class="progress-custom" style="width:120px">
                      <div class="progress-fill" [style.width.%]="inst.attendance"></div>
                    </div>
                    <span>{{ inst.attendance }}%</span>
                  </div>
                </td>
                <td><span class="badge-status badge-present">Active</span></td>
                <td>
                  <button class="btn-ghost" style="padding:0.25rem 0.5rem;font-size:0.75rem" [routerLink]="['/super-admin/institutions', inst.id]">View</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- At-risk alerts -->
      <div class="card-glass">
        <h3 class="section-title">⚠️ Platform Alerts</h3>
        <div class="alert-list">
          <div class="alert-item" *ngFor="let alert of platformAlerts" [class]="'alert-' + alert.level">
            <span class="alert-icon">{{ alert.icon }}</span>
            <div class="alert-content">
              <div class="alert-title">{{ alert.title }}</div>
              <div class="alert-desc">{{ alert.desc }}</div>
            </div>
            <span class="badge-status" [class]="'badge-' + alert.level">{{ alert.level | titlecase }}</span>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .page-header { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem; }
    .page-title-text { font-size:1.75rem; font-weight:800; color:var(--text-primary); }
    .page-subtitle { color:var(--text-muted); font-size:0.9rem; }
    .header-actions { display:flex; gap:0.75rem; }
    .grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    @media (max-width:768px) { .grid-2 { grid-template-columns:1fr; } }
    .section-title { font-size:1rem; font-weight:700; color:var(--text-primary); margin-bottom:1rem; }
    .stat-change { font-size:0.75rem; margin-top:0.25rem; }
    .stat-change.up { color:var(--success); }
    .stat-change.down { color:var(--danger); }
    .chart-bars { display:flex; flex-direction:column; gap:0.75rem; }
    .chart-bar-item { display:grid; grid-template-columns:120px 1fr 40px; align-items:center; gap:0.75rem; }
    .bar-label { font-size:0.8rem; color:var(--text-secondary); }
    .bar-track { height:8px; background:var(--bg-input); border-radius:999px; overflow:hidden; }
    .bar-fill { height:100%; border-radius:999px; transition:width 1s ease; }
    .bar-value { font-size:0.8rem; color:var(--text-primary); font-weight:600; text-align:right; }
    .sparkline-chart { display:flex; flex-direction:column; gap:0.5rem; }
    .sparkline-bars { display:flex; align-items:flex-end; gap:0.375rem; height:100px; }
    .sparkline-bar {
      flex:1; min-height:4px;
      background:var(--gradient-primary);
      border-radius:4px 4px 0 0;
      transition:height 0.5s ease;
      cursor:pointer;
    }
    .sparkline-bar:hover { opacity:0.8; }
    .sparkline-labels { display:flex; gap:0.375rem; }
    .sparkline-labels span { flex:1; text-align:center; font-size:0.65rem; color:var(--text-muted); }
    .inst-name { font-weight:600; color:var(--text-primary); font-size:0.875rem; }
    .inst-location { font-size:0.75rem; color:var(--text-muted); }
    .code-badge { background:rgba(79,70,229,0.2); color:var(--primary-light); padding:0.15rem 0.5rem; border-radius:4px; font-size:0.75rem; }
    .attendance-bar { display:flex; align-items:center; gap:0.5rem; font-size:0.8rem; color:var(--text-secondary); }
    .view-all-link { color:var(--primary-light); text-decoration:none; font-size:0.85rem; }
    .view-all-link:hover { text-decoration:underline; }
    .alert-list { display:flex; flex-direction:column; gap:0.75rem; }
    .alert-item { display:flex; align-items:center; gap:1rem; padding:0.875rem; border-radius:var(--border-radius); border:1px solid var(--border-color); }
    .alert-high { border-color:rgba(239,68,68,0.3); background:rgba(239,68,68,0.05); }
    .alert-medium { border-color:rgba(245,158,11,0.3); background:rgba(245,158,11,0.05); }
    .alert-low { border-color:rgba(16,185,129,0.3); background:rgba(16,185,129,0.05); }
    .alert-icon { font-size:1.5rem; }
    .alert-content { flex:1; }
    .alert-title { font-weight:600; font-size:0.875rem; color:var(--text-primary); }
    .alert-desc { font-size:0.8rem; color:var(--text-muted); }
    .d-flex { display:flex; }
    .justify-content-between { justify-content:space-between; }
    .align-items-center { align-items:center; }
    .align-items-start { align-items:flex-start; }
    .mb-3 { margin-bottom:1rem; }
    .table-responsive { overflow-x:auto; }
  `],
})
export class SaDashboardComponent implements OnInit {
  stats = [
    { label: 'Total Institutions', value: 48, change: '+3 this month', changePositive: true, icon: '🏫', iconBg: 'rgba(79,70,229,0.2)' },
    { label: 'Total Students', value: 124580, change: '+1,240 this month', changePositive: true, icon: '📚', iconBg: 'rgba(6,182,212,0.2)' },
    { label: 'Total Faculty', value: 4820, change: '+35 this month', changePositive: true, icon: '👨‍🏫', iconBg: 'rgba(16,185,129,0.2)' },
    { label: 'Platform Attendance', value: 91, change: '-1.2% vs last week', changePositive: false, icon: '✅', iconBg: 'rgba(245,158,11,0.2)' },
  ];

  institutionTypes = [
    { label: 'CBSE Schools', count: 18, pct: 38, color: '#4f46e5' },
    { label: 'ICSE Schools', count: 8, pct: 17, color: '#06b6d4' },
    { label: 'SSC Schools', count: 14, pct: 29, color: '#10b981' },
    { label: 'Degree Colleges', count: 5, pct: 10, color: '#f59e0b' },
    { label: 'Junior Colleges', count: 3, pct: 6, color: '#8b5cf6' },
  ];

  monthlyEnrollment = [
    { month: 'Jun', count: 8200 }, { month: 'Jul', count: 12400 }, { month: 'Aug', count: 18600 },
    { month: 'Sep', count: 15200 }, { month: 'Oct', count: 11800 }, { month: 'Nov', count: 9600 },
    { month: 'Dec', count: 6200 }, { month: 'Jan', count: 8800 }, { month: 'Feb', count: 10200 },
    { month: 'Mar', count: 12600 }, { month: 'Apr', count: 11400 }, { month: 'May', count: 7400 },
  ];

  get maxEnrollment() { return Math.max(...this.monthlyEnrollment.map(m => m.count)); }

  recentInstitutions = [
    { id: '1', name: 'Delhi Public School, Hyderabad', code: 'DPS-HYD', type: 'CBSE School', city: 'Hyderabad', students: 3420, attendance: 94 },
    { id: '2', name: 'Narayana Junior College', code: 'NJC-HYD', type: 'Junior College', city: 'Secunderabad', students: 1850, attendance: 88 },
    { id: '3', name: 'Chaitanya Schools', code: 'CHT-HYD', type: 'SSC School', city: 'KPHB', students: 2100, attendance: 91 },
    { id: '4', name: 'St. Francis School', code: 'SFS-HYD', type: 'ICSE School', city: 'Banjara Hills', students: 1240, attendance: 96 },
    { id: '5', name: 'Vignan Degree College', code: 'VIG-HYD', type: 'Degree College', city: 'Ameerpet', students: 860, attendance: 82 },
  ];

  platformAlerts = [
    { level: 'high', icon: '🚨', title: '3 Institutions with <70% attendance today', desc: 'NJC-HYD, VIG-HYD, and 1 more require immediate attention' },
    { level: 'medium', icon: '⚠️', title: '128 students flagged as at-risk', desc: 'Based on AI prediction model — attendance + grades pattern' },
    { level: 'low', icon: '💡', title: 'System backup completed', desc: 'MongoDB snapshot at 02:00 IST — all data secured' },
  ];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // In production: load from API
    // this.http.get(`${environment.apiUrl}/analytics/super-admin/platform`).subscribe(...)
  }

  exportReport(): void {
    console.log('Exporting report...');
    // TODO: generate PDF/Excel report
  }
}
