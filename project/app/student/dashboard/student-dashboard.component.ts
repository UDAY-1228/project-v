import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Store } from '@ngxs/store';
import { AuthState } from '../../../../core/state/auth.state';

@Component({
  selector: 'eims-student-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <div class="stagger-children">
      <!-- Welcome banner -->
      <div class="welcome-banner">
        <div class="welcome-left">
          <div class="welcome-tag">📚 Student Portal</div>
          <h1 class="welcome-title">Good Morning, {{ user?.full_name?.split(' ')[0] }}! 👋</h1>
          <p class="welcome-sub">Class 10-A · Roll No: STU-2024-001 · DPS Hyderabad</p>
          <div class="quick-btns">
            <button class="btn-primary-glow" id="btn-view-id" routerLink="/student/virtual-id">
              <span class="material-icons" style="font-size:1rem">badge</span> My Virtual ID
            </button>
            <button class="btn-ghost" id="btn-homework" routerLink="/student/homework-helper">
              🤖 AI Homework Helper
            </button>
          </div>
        </div>
        <div class="welcome-card-graphic">
          <div class="mini-id-card">
            <div class="mic-header">EIMS Student ID</div>
            <div class="mic-initials">{{ user?.full_name?.charAt(0) }}{{ user?.full_name?.split(' ')[1]?.charAt(0) }}</div>
            <div class="mic-name">{{ user?.full_name }}</div>
            <div class="mic-id">STU-DPS-2024-001</div>
            <div class="mic-qr">▣ ▢ ▣</div>
          </div>
        </div>
      </div>

      <!-- Quick stats -->
      <div class="stats-grid">
        <div class="card-stat" *ngFor="let s of myStats" (click)="navigate(s.route)">
          <div class="stat-icon" [style.background]="s.iconBg">{{ s.icon }}</div>
          <div class="stat-value">{{ s.value }}</div>
          <div class="stat-label">{{ s.label }}</div>
          <div class="stat-meta" [style.color]="s.metaColor">{{ s.meta }}</div>
        </div>
      </div>

      <!-- Today's timetable + Attendance -->
      <div class="grid-2">
        <!-- Today's schedule -->
        <div class="card-glass">
          <h3 class="section-title">📅 Today's Schedule</h3>
          <div class="schedule-list">
            <div class="schedule-item" *ngFor="let s of todaySchedule" [class.current]="s.current">
              <div class="schedule-time">
                <span class="time-start">{{ s.start }}</span>
                <span class="time-end">{{ s.end }}</span>
              </div>
              <div class="schedule-divider" [style.background]="s.color"></div>
              <div class="schedule-details">
                <div class="schedule-subject">{{ s.subject }}</div>
                <div class="schedule-teacher">{{ s.teacher }} · {{ s.room }}</div>
              </div>
              <div class="schedule-status" *ngIf="s.current">
                <span class="badge-status badge-present">Now</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Attendance summary -->
        <div class="card-glass">
          <h3 class="section-title">📊 Attendance This Month</h3>
          <div class="attendance-circle-wrapper">
            <div class="attendance-circle" [style.--pct]="attendancePct + '%'">
              <div class="circle-value">{{ attendancePct }}%</div>
              <div class="circle-label">Overall</div>
            </div>
          </div>
          <div class="attendance-breakdown">
            <div class="breakdown-item" *ngFor="let b of attendanceBreakdown">
              <div class="breakdown-dot" [style.background]="b.color"></div>
              <div class="breakdown-label">{{ b.label }}</div>
              <div class="breakdown-value">{{ b.value }}</div>
            </div>
          </div>
          <div class="attendance-warning" *ngIf="attendancePct < 75">
            ⚠️ Your attendance is below 75%. Please contact your class teacher.
          </div>
          <a routerLink="/student/attendance" class="view-all-link" style="margin-top:1rem;display:block">View Full History →</a>
        </div>
      </div>

      <!-- Pending assignments + Recent results -->
      <div class="grid-2">
        <div class="card-glass">
          <h3 class="section-title">📝 Pending Assignments</h3>
          <div class="assignment-list">
            <div class="assignment-item" *ngFor="let a of pendingAssignments">
              <div class="assignment-info">
                <div class="assignment-title">{{ a.title }}</div>
                <div class="assignment-meta">{{ a.subject }} · Due {{ a.due }}</div>
              </div>
              <div class="assignment-actions">
                <span class="badge-status" [class]="a.urgent ? 'badge-absent' : 'badge-pending'">
                  {{ a.urgent ? 'Urgent' : 'Pending' }}
                </span>
                <button class="btn-ghost small-btn" routerLink="/student/assignments">Submit</button>
              </div>
            </div>
          </div>
        </div>

        <div class="card-glass">
          <h3 class="section-title">🏆 Recent Results</h3>
          <div class="results-list">
            <div class="result-item" *ngFor="let r of recentResults">
              <div class="result-subject">{{ r.subject }}</div>
              <div class="result-exam">{{ r.exam }}</div>
              <div class="result-progress">
                <div class="progress-custom">
                  <div class="progress-fill" [style.width.%]="r.pct" [style.background]="r.color"></div>
                </div>
                <span class="result-marks">{{ r.marks }}/{{ r.total }}</span>
              </div>
              <span class="badge-status" [class]="r.grade === 'A' || r.grade === 'A+' ? 'badge-present' : 'badge-pending'">
                Grade {{ r.grade }}
              </span>
            </div>
          </div>
          <a routerLink="/student/results" class="view-all-link" style="margin-top:1rem;display:block">View All Results →</a>
        </div>
      </div>

      <!-- Fee alert -->
      <div class="card-glass fee-alert" *ngIf="feesDue > 0">
        <div class="fee-alert-content">
          <span class="fee-icon">💳</span>
          <div>
            <div class="fee-title">Fee Due: ₹{{ feesDue | number }}</div>
            <div class="fee-desc">Term 2 fees due by March 31, 2024. Pay now to avoid late fee.</div>
          </div>
          <button class="btn-primary-glow" id="btn-pay-fee" routerLink="/student/fees">Pay Now</button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .welcome-banner { display:grid; grid-template-columns:1fr auto; gap:2rem; align-items:center; background:var(--gradient-card); border:1px solid var(--border-color); border-radius:var(--border-radius-xl); padding:2rem; margin-bottom:1.5rem; }
    .welcome-tag { font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:var(--primary-light); margin-bottom:0.5rem; }
    .welcome-title { font-size:1.75rem; font-weight:800; color:var(--text-primary); margin-bottom:0.25rem; }
    .welcome-sub { color:var(--text-muted); font-size:0.9rem; margin-bottom:1rem; }
    .quick-btns { display:flex; gap:0.75rem; flex-wrap:wrap; }
    .mini-id-card { width:160px; background:linear-gradient(135deg,#1a237e,#283593); border-radius:12px; padding:1rem; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.4); }
    .mic-header { font-size:0.6rem; font-weight:700; color:rgba(255,255,255,0.7); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem; }
    .mic-initials { width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.25rem; font-weight:800; color:white; margin:0 auto 0.5rem; }
    .mic-name { font-size:0.7rem; font-weight:600; color:white; }
    .mic-id { font-size:0.6rem; color:rgba(255,255,255,0.6); margin:0.125rem 0; }
    .mic-qr { font-size:1.25rem; margin-top:0.5rem; color:rgba(255,255,255,0.8); }
    .stat-meta { font-size:0.75rem; margin-top:0.25rem; }
    .grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    @media (max-width:768px) { .grid-2{grid-template-columns:1fr;} .welcome-banner{grid-template-columns:1fr;} .welcome-card-graphic{display:none;} }
    .section-title { font-size:1rem; font-weight:700; color:var(--text-primary); margin-bottom:1rem; }
    .schedule-list { display:flex; flex-direction:column; gap:0.5rem; }
    .schedule-item { display:grid; grid-template-columns:80px 3px 1fr auto; gap:0.75rem; align-items:center; padding:0.5rem; border-radius:var(--border-radius); transition:var(--transition-fast); }
    .schedule-item.current { background:rgba(79,70,229,0.1); }
    .schedule-time { display:flex; flex-direction:column; gap:0.125rem; }
    .time-start { font-size:0.8rem; font-weight:700; color:var(--text-primary); }
    .time-end { font-size:0.7rem; color:var(--text-muted); }
    .schedule-divider { width:3px; height:40px; border-radius:999px; }
    .schedule-subject { font-weight:600; font-size:0.875rem; color:var(--text-primary); }
    .schedule-teacher { font-size:0.75rem; color:var(--text-muted); }
    .attendance-circle-wrapper { display:flex; justify-content:center; margin:1rem 0; }
    .attendance-circle {
      width:120px; height:120px; border-radius:50%;
      background:conic-gradient(var(--primary) calc(var(--pct) * 3.6deg), var(--bg-input) 0deg);
      display:flex; flex-direction:column; align-items:center; justify-content:center;
      position:relative;
    }
    .attendance-circle::before { content:''; position:absolute; width:90px; height:90px; background:var(--bg-secondary); border-radius:50%; }
    .circle-value { font-size:1.5rem; font-weight:800; color:var(--text-primary); position:relative; z-index:1; }
    .circle-label { font-size:0.7rem; color:var(--text-muted); position:relative; z-index:1; }
    .attendance-breakdown { display:flex; flex-direction:column; gap:0.5rem; }
    .breakdown-item { display:flex; align-items:center; gap:0.5rem; font-size:0.85rem; }
    .breakdown-dot { width:10px; height:10px; border-radius:50%; flex-shrink:0; }
    .breakdown-label { flex:1; color:var(--text-secondary); }
    .breakdown-value { font-weight:700; color:var(--text-primary); }
    .attendance-warning { background:rgba(245,158,11,0.1); border:1px solid rgba(245,158,11,0.3); color:#f59e0b; padding:0.75rem; border-radius:var(--border-radius); font-size:0.85rem; margin-top:0.5rem; }
    .assignment-list,.results-list { display:flex; flex-direction:column; gap:0.75rem; }
    .assignment-item { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:0.75rem; background:rgba(255,255,255,0.03); border-radius:var(--border-radius); border:1px solid var(--border-color); }
    .assignment-title { font-weight:600; font-size:0.875rem; color:var(--text-primary); }
    .assignment-meta { font-size:0.75rem; color:var(--text-muted); }
    .assignment-actions { display:flex; align-items:center; gap:0.5rem; }
    .small-btn { padding:0.25rem 0.5rem; font-size:0.75rem; }
    .result-item { display:grid; grid-template-columns:1fr 1fr auto; align-items:center; gap:0.75rem; padding:0.5rem 0; border-bottom:1px solid rgba(255,255,255,0.05); }
    .result-subject { font-weight:700; font-size:0.875rem; color:var(--text-primary); }
    .result-exam { font-size:0.75rem; color:var(--text-muted); }
    .result-progress { display:flex; align-items:center; gap:0.5rem; }
    .result-marks { font-size:0.75rem; color:var(--text-muted); white-space:nowrap; }
    .view-all-link { color:var(--primary-light); text-decoration:none; font-size:0.85rem; }
    .fee-alert { background:rgba(79,70,229,0.08) !important; border-color:rgba(79,70,229,0.3) !important; }
    .fee-alert-content { display:flex; align-items:center; gap:1rem; flex-wrap:wrap; }
    .fee-icon { font-size:2rem; }
    .fee-title { font-weight:700; color:var(--text-primary); }
    .fee-desc { font-size:0.85rem; color:var(--text-muted); margin-top:0.25rem; }
  `],
})
export class StudentDashboardComponent implements OnInit {
  user: any = null;
  attendancePct = 82;
  feesDue = 15500;

  myStats = [
    { label: 'Attendance', value: '82%', meta: '⚠️ Below 85% target', metaColor: '#f59e0b', icon: '✅', iconBg: 'rgba(16,185,129,0.2)', route: '/student/attendance' },
    { label: 'Assignments Due', value: '3', meta: '2 urgent', metaColor: '#ef4444', icon: '📝', iconBg: 'rgba(239,68,68,0.2)', route: '/student/assignments' },
    { label: 'Avg Marks', value: '78/100', meta: '↑ 5 pts this term', metaColor: '#10b981', icon: '🎯', iconBg: 'rgba(79,70,229,0.2)', route: '/student/results' },
    { label: 'Courses', value: '6', meta: '2 with new content', metaColor: '#06b6d4', icon: '📚', iconBg: 'rgba(6,182,212,0.2)', route: '/student/lms' },
  ];

  todaySchedule = [
    { start: '09:00', end: '09:45', subject: 'Mathematics', teacher: 'Mrs. Reddy', room: 'Room 12', color: '#4f46e5', current: false },
    { start: '09:45', end: '10:30', subject: 'Physics', teacher: 'Mr. Kumar', room: 'Room 8', color: '#06b6d4', current: true },
    { start: '10:45', end: '11:30', subject: 'English', teacher: 'Ms. Priya', room: 'Room 12', color: '#10b981', current: false },
    { start: '11:30', end: '12:15', subject: 'Chemistry', teacher: 'Mr. Rao', room: 'Lab 2', color: '#f59e0b', current: false },
    { start: '13:00', end: '13:45', subject: 'Telugu', teacher: 'Mrs. Lakshmi', room: 'Room 12', color: '#8b5cf6', current: false },
    { start: '13:45', end: '14:30', subject: 'Social Studies', teacher: 'Mr. Sharma', room: 'Room 12', color: '#f97316', current: false },
  ];

  attendanceBreakdown = [
    { label: 'Present', value: 68, color: '#10b981' },
    { label: 'Late', value: 4, color: '#f59e0b' },
    { label: 'Absent', value: 10, color: '#ef4444' },
  ];

  pendingAssignments = [
    { title: 'Quadratic Equations Exercise', subject: 'Math', due: 'Tomorrow', urgent: true },
    { title: 'Essay on Indian Independence', subject: 'English', due: 'Mar 22', urgent: false },
    { title: 'Chemical Reactions Lab Report', subject: 'Chemistry', due: 'Mar 25', urgent: false },
  ];

  recentResults = [
    { subject: 'Mathematics', exam: 'Unit Test 2', marks: 88, total: 100, pct: 88, grade: 'A', color: '#4f46e5' },
    { subject: 'Physics', exam: 'Mid Term', marks: 72, total: 100, pct: 72, grade: 'B', color: '#06b6d4' },
    { subject: 'Chemistry', exam: 'Unit Test 2', marks: 91, total: 100, pct: 91, grade: 'A+', color: '#10b981' },
    { subject: 'English', exam: 'Unit Test 2', marks: 65, total: 100, pct: 65, grade: 'B', color: '#f59e0b' },
  ];

  constructor(private store: Store, private router: import('@angular/router').Router) {}

  ngOnInit(): void {
    this.user = this.store.selectSnapshot(AuthState.user);
  }

  navigate(route: string): void {
    this.router.navigate([route]);
  }
}
