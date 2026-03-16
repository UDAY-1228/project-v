import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-studenttimetable',
  template: `
    <ion-header [translucent]="true" class="ion-no-border">
      <ion-toolbar color="primary" class="timetable-header">
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/home"></ion-back-button>
        </ion-buttons>
        <ion-title>My Timetable</ion-title>
        <ion-buttons slot="end">
          <ion-button>
            <ion-icon slot="icon-only" name="calendar-outline"></ion-icon>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content [fullscreen]="true" class="ion-padding timetable-bg">
      <div class="day-selector">
        <div class="day-pill active">
          <span>Mon</span>
          <div class="dot"></div>
        </div>
        <div class="day-pill"><span>Tue</span></div>
        <div class="day-pill"><span>Wed</span></div>
        <div class="day-pill"><span>Thu</span></div>
        <div class="day-pill"><span>Fri</span></div>
      </div>

      <div class="info-section">
        <p class="current-date">Grade 10, Section A • Monday</p>
      </div>

      <div class="timeline-container">
        <!-- Class Item -->
        <div class="timeline-item">
          <div class="time-column">
            <span class="start-time">09:00</span>
            <span class="end-time">09:45</span>
          </div>
          <div class="line-column">
            <div class="circle bg-indigo"></div>
            <div class="line"></div>
          </div>
          <div class="card-column">
            <ion-card class="class-card border-indigo mb-0">
              <ion-card-content class="p-3">
                <div class="flex-between">
                  <h4>Mathematics</h4>
                  <ion-badge color="primary">R-101</ion-badge>
                </div>
                <div class="teacher-info mt-2">
                  <ion-icon name="person"></ion-icon>
                  <span>Dr. Sarah Wilson</span>
                </div>
              </ion-card-content>
            </ion-card>
          </div>
        </div>

        <!-- Class Item -->
        <div class="timeline-item">
          <div class="time-column">
            <span class="start-time">09:45</span>
            <span class="end-time">10:30</span>
          </div>
          <div class="line-column">
            <div class="circle bg-emerald"></div>
            <div class="line"></div>
          </div>
          <div class="card-column">
            <ion-card class="class-card border-emerald mb-0">
              <ion-card-content class="p-3">
                <div class="flex-between">
                  <h4>Physics</h4>
                  <ion-badge color="success">L-204</ion-badge>
                </div>
                <div class="teacher-info mt-2">
                  <ion-icon name="person"></ion-icon>
                  <span>Prof. James Chen</span>
                </div>
              </ion-card-content>
            </ion-card>
          </div>
        </div>

        <!-- Break Item -->
        <div class="timeline-item break-item">
          <div class="time-column">
            <span class="start-time">10:30</span>
            <span class="end-time">10:45</span>
          </div>
          <div class="line-column">
            <div class="circle-outline"></div>
            <div class="line dotted"></div>
          </div>
          <div class="card-column">
            <div class="break-card">
              <ion-icon name="cafe-outline"></ion-icon>
              <span>Short Break</span>
            </div>
          </div>
        </div>

        <!-- Class Item -->
        <div class="timeline-item">
          <div class="time-column">
            <span class="start-time">10:45</span>
            <span class="end-time">11:30</span>
          </div>
          <div class="line-column">
            <div class="circle bg-purple"></div>
            <div class="line"></div>
          </div>
          <div class="card-column">
            <ion-card class="class-card border-purple mb-0">
              <ion-card-content class="p-3">
                <div class="flex-between">
                  <h4>English Lit.</h4>
                  <ion-badge color="tertiary">R-302</ion-badge>
                </div>
                <div class="teacher-info mt-2">
                  <ion-icon name="person"></ion-icon>
                  <span>Ms. Emily Bronte</span>
                </div>
              </ion-card-content>
            </ion-card>
          </div>
        </div>
      </div>

      <style>
        .timetable-bg {
          --background: #f8fafc;
        }

        .timetable-header {
          --background: #4f46e5;
        }

        .day-selector {
          display: flex;
          justify-content: space-between;
          padding: 8px 4px 20px;
          overflow-x: auto;
        }

        .day-pill {
          padding: 10px 18px;
          border-radius: 20px;
          background: white;
          color: #64748b;
          font-weight: 600;
          font-size: 0.9rem;
          box-shadow: 0 4px 10px rgba(0,0,0,0.03);
          border: 1px solid #f1f5f9;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 4px;
        }

        .day-pill.active {
          background: #4f46e5;
          color: white;
          box-shadow: 0 6px 15px rgba(79, 70, 229, 0.3);
          border: none;
        }

        .dot {
          width: 6px;
          height: 6px;
          background: white;
          border-radius: 50%;
        }

        .info-section {
          margin-bottom: 24px;
        }

        .current-date {
          color: #64748b;
          font-weight: 500;
          font-size: 0.95rem;
          margin: 0;
        }

        .timeline-container {
          padding-right: 10px;
        }

        .timeline-item {
          display: flex;
          margin-bottom: 12px;
        }

        .time-column {
          width: 55px;
          display: flex;
          flex-direction: column;
          align-items: flex-end;
          padding-right: 12px;
          padding-top: 14px;
          flex-shrink: 0;
        }

        .start-time {
          font-weight: 700;
          color: #1e293b;
          font-size: 0.85rem;
        }

        .end-time {
          font-weight: 500;
          color: #94a3b8;
          font-size: 0.75rem;
        }

        .line-column {
          width: 24px;
          display: flex;
          flex-direction: column;
          align-items: center;
          position: relative;
          flex-shrink: 0;
        }

        .circle {
          width: 14px;
          height: 14px;
          border-radius: 50%;
          margin-top: 16px;
          z-index: 2;
          box-shadow: 0 0 0 4px #f8fafc;
        }

        .circle-outline {
          width: 12px;
          height: 12px;
          border-radius: 50%;
          border: 2px solid #cbd5e1;
          background: #f8fafc;
          margin-top: 17px;
          z-index: 2;
        }

        .line {
          width: 2px;
          background: #e2e8f0;
          flex: 1;
          margin-top: -6px;
          margin-bottom: -28px;
        }

        .line.dotted {
          background: repeating-linear-gradient(180deg, #cbd5e1, #cbd5e1 4px, transparent 4px, transparent 8px);
        }

        .card-column {
          flex: 1;
          padding-left: 12px;
          padding-bottom: 8px;
        }

        .class-card {
          margin-top: 0;
          box-shadow: 0 4px 15px rgba(0,0,0,0.03);
          border-radius: 16px;
        }

        .p-3 {
          padding: 16px;
        }

        .mb-0 {
          margin-bottom: 0;
        }

        .mt-2 {
          margin-top: 10px;
        }

        .flex-between {
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
        }

        .flex-between h4 {
          margin: 0;
          font-weight: 700;
          font-size: 1.1rem;
          color: #1e293b;
        }

        .teacher-info {
          display: flex;
          align-items: center;
          gap: 6px;
          color: #64748b;
          font-size: 0.85rem;
        }

        .bg-indigo { background: #4f46e5; }
        .bg-emerald { background: #10b981; }
        .bg-purple { background: #8b5cf6; }

        .border-indigo { border-left: 4px solid #4f46e5; }
        .border-emerald { border-left: 4px solid #10b981; }
        .border-purple { border-left: 4px solid #8b5cf6; }

        .break-card {
          padding: 12px 16px;
          background: #f1f5f9;
          border-radius: 12px;
          display: flex;
          align-items: center;
          gap: 10px;
          color: #64748b;
          font-weight: 600;
          font-size: 0.9rem;
          margin-top: 4px;
        }
      </style>
    </ion-content>
  `,
  styles: []
})
export class StudentTimetablePage implements OnInit {
  constructor() { }
  ngOnInit() { }
}
