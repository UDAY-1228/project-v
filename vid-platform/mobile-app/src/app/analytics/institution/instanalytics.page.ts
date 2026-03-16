import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-instanalytics',
  template: `
    <ion-header [translucent]="true" class="ion-no-border">
      <ion-toolbar color="primary" class="dashboard-header">
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/home"></ion-back-button>
        </ion-buttons>
        <ion-title>Overview</ion-title>
        <ion-buttons slot="end">
          <ion-button>
            <ion-icon slot="icon-only" name="notifications-outline"></ion-icon>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content [fullscreen]="true" class="ion-padding dashboard-bg">
      <div class="header-section">
        <h2 class="title">Institution Analytics</h2>
        <p class="subtitle">Real-time performance metrics</p>
      </div>

      <div class="stats-grid">
        <div class="stat-card">
          <div class="icon-wrapper bg-indigo">
            <ion-icon name="people"></ion-icon>
          </div>
          <div class="stat-content">
            <p>Students</p>
            <h3>1,250</h3>
            <span class="trend positive">+12%</span>
          </div>
        </div>

        <div class="stat-card">
          <div class="icon-wrapper bg-emerald">
            <ion-icon name="checkmark-done-circle"></ion-icon>
          </div>
          <div class="stat-content">
            <p>Attendance</p>
            <h3>92.5%</h3>
            <span class="trend positive">+2%</span>
          </div>
        </div>

        <div class="stat-card">
          <div class="icon-wrapper bg-amber">
            <ion-icon name="cash"></ion-icon>
          </div>
          <div class="stat-content">
            <p>Fees Config</p>
            <h3>₹7.5L</h3>
            <span class="trend negative">-5%</span>
          </div>
        </div>

        <div class="stat-card">
          <div class="icon-wrapper bg-purple">
            <ion-icon name="book"></ion-icon>
          </div>
          <div class="stat-content">
            <p>Teachers</p>
            <h3>85</h3>
            <span class="trend neutral">0%</span>
          </div>
        </div>
      </div>

      <ion-card class="chart-card custom-card">
        <ion-card-header>
          <ion-card-subtitle>Weekly Performance</ion-card-subtitle>
          <ion-card-title>Attendance Flow</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <div class="mock-chart">
            <div class="bar" style="height: 60%"></div>
            <div class="bar" style="height: 80%"></div>
            <div class="bar" style="height: 50%"></div>
            <div class="bar" style="height: 90%"></div>
            <div class="bar" style="height: 70%"></div>
            <div class="bar" style="height: 100%"></div>
            <div class="bar" style="height: 85%"></div>
          </div>
          <div class="chart-labels">
            <span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span>S</span>
          </div>
        </ion-card-content>
      </ion-card>

      <div class="recent-actions">
        <h3 class="section-title">Quick Actions</h3>
        <ion-list lines="none" class="custom-list">
          <ion-item button detail="true" class="list-item">
            <div slot="start" class="list-icon bg-blue-light">
              <ion-icon name="document-text" color="primary"></ion-icon>
            </div>
            <ion-label>
              <h2>Generate Report</h2>
              <p>Download academic digest</p>
            </ion-label>
          </ion-item>
          <ion-item button detail="true" class="list-item">
            <div slot="start" class="list-icon bg-rose-light">
              <ion-icon name="alert-circle" color="danger"></ion-icon>
            </div>
            <ion-label>
              <h2>Review Absences</h2>
              <p>12 students flagged</p>
            </ion-label>
          </ion-item>
        </ion-list>
      </div>

      <style>
        .dashboard-bg {
          --background: #f8fafc;
        }

        .dashboard-header {
          --background: #4f46e5;
        }

        .header-section {
          margin-bottom: 24px;
        }

        .title {
          font-size: 1.8rem;
          font-weight: 700;
          color: #1e293b;
          margin: 0;
        }

        .subtitle {
          color: #64748b;
          margin-top: 4px;
          font-size: 0.95rem;
        }

        .stats-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 16px;
          margin-bottom: 24px;
        }

        .stat-card {
          background: white;
          border-radius: 20px;
          padding: 16px;
          box-shadow: 0 4px 15px rgba(0,0,0,0.03);
          border: 1px solid #f1f5f9;
        }

        .icon-wrapper {
          width: 40px;
          height: 40px;
          border-radius: 12px;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-bottom: 12px;
        }

        .icon-wrapper ion-icon {
          color: white;
          font-size: 1.2rem;
        }

        .bg-indigo { background: #4f46e5; }
        .bg-emerald { background: #10b981; }
        .bg-amber { background: #f59e0b; }
        .bg-purple { background: #8b5cf6; }

        .bg-blue-light { background: #eff6ff; }
        .bg-rose-light { background: #fff1f2; }

        .stat-content p {
          color: #64748b;
          font-size: 0.8rem;
          margin: 0 0 4px;
          font-weight: 500;
        }

        .stat-content h3 {
          color: #1e293b;
          font-size: 1.4rem;
          font-weight: 700;
          margin: 0 0 4px;
        }

        .trend {
          font-size: 0.75rem;
          font-weight: 600;
        }
        .trend.positive { color: #10b981; }
        .trend.negative { color: #ef4444; }
        .trend.neutral { color: #64748b; }

        .custom-card {
          border-radius: 20px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.04);
          margin: 0 0 24px;
          border: 1px solid #f1f5f9;
        }

        .mock-chart {
          display: flex;
          align-items: flex-end;
          justify-content: space-between;
          height: 120px;
          padding-top: 20px;
          margin-bottom: 10px;
        }

        .bar {
          width: 12%;
          background: linear-gradient(180deg, #4f46e5 0%, #818cf8 100%);
          border-radius: 4px 4px 0 0;
        }

        .chart-labels {
          display: flex;
          justify-content: space-between;
          color: #94a3b8;
          font-size: 0.75rem;
          font-weight: 500;
        }

        .section-title {
          font-size: 1.2rem;
          font-weight: 700;
          color: #1e293b;
          margin-bottom: 12px;
        }

        .custom-list {
          background: transparent;
        }

        .list-item {
          --background: white;
          --border-radius: 16px;
          margin-bottom: 12px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.02);
          border: 1px solid #f1f5f9;
        }

        .list-icon {
          width: 44px;
          height: 44px;
          border-radius: 12px;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-right: 16px;
        }

        .list-icon ion-icon {
          font-size: 1.4rem;
        }

        ion-label h2 {
          font-weight: 600;
          color: #1e293b;
          margin-bottom: 4px;
        }

        ion-label p {
          color: #64748b;
        }
      </style>
    </ion-content>
  `,
  styles: []
})
export class InstAnalyticsPage implements OnInit {
  constructor() { }
  ngOnInit() { }
}

