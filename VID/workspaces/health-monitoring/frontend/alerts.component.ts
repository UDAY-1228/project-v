import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-alerts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './alerts.component.html',
  styleUrls: ['./alerts.component.css']
})
export class AlertsComponent implements OnInit {
  alerts: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.alerts = [
      { id: '1', title: 'Critical BMI Alert', description: 'Student BMI below normal range', student_name: 'Rahul Sharma', severity: 'critical', status: 'pending', created_at: new Date() },
      { id: '2', title: 'Allergy Reaction Reported', description: 'Student experienced allergic reaction', student_name: 'Priya Patel', severity: 'high', status: 'pending', created_at: new Date() },
      { id: '3', title: 'Follow-up Required', description: 'Routine checkup follow-up needed', student_name: 'Amit Kumar', severity: 'normal', status: 'resolved', created_at: new Date() }
    ];
  }

  getAlertCount(severity: string): number {
    return this.alerts.filter(a => a.severity === severity || a.status === severity).length;
  }

  getSeverityClass(severity: string): string {
    const classes: Record<string, string> = {
      critical: 'bg-red-500/20 text-red-400',
      high: 'bg-amber-500/20 text-amber-400',
      normal: 'bg-zinc-500/20 text-zinc-400'
    };
    return classes[severity] || classes.normal;
  }
}
