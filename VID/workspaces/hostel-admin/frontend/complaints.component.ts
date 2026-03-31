import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-complaints',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './complaints.component.html',
  styleUrls: ['./complaints.component.css']
})
export class ComplaintsComponent implements OnInit {
  complaints: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.complaints = [
      { id: '1', title: 'Water leakage in bathroom', student_name: 'Rahul Sharma', room_id: 'A101', description: 'Water dripping from ceiling pipe', priority: 'high', status: 'pending', created_at: new Date() },
      { id: '2', title: 'Broken window pane', student_name: 'Priya Patel', room_id: 'A102', description: 'Window glass cracked', priority: 'normal', status: 'in_progress', created_at: new Date() },
      { id: '3', title: 'Fan not working', student_name: 'Amit Kumar', room_id: 'B201', description: 'Ceiling fan stopped working', priority: 'normal', status: 'resolved', created_at: new Date() }
    ];
  }

  getComplaintCount(status: string): number {
    return this.complaints.filter(c => c.status === status).length;
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      pending: 'bg-amber-500/10 text-amber-400',
      in_progress: 'bg-blue-500/10 text-blue-400',
      resolved: 'bg-emerald-500/10 text-emerald-400'
    };
    return classes[status] || classes.pending;
  }

  getPriorityClass(priority: string): string {
    const classes: Record<string, string> = {
      high: 'bg-red-500/20 text-red-400',
      normal: 'bg-zinc-500/20 text-zinc-400',
      low: 'bg-zinc-500/10 text-zinc-500'
    };
    return classes[priority] || classes.normal;
  }
}
