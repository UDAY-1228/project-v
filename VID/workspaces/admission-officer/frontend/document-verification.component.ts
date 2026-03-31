import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-document-verification',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './document-verification.component.html',
  styleUrls: ['./document-verification.component.css']
})
export class DocumentVerificationComponent implements OnInit {
  documents: any[] = [];

  ngOnInit(): void {
    this.documents = [
      { application_id: 'APP-2026030101', student_name: 'Priya Sharma', status: 'pending', documents: [
        { type: '10th Certificate', verified: true },
        { type: '12th Certificate', verified: false },
        { type: 'Income Certificate', verified: false }
      ]},
      { application_id: 'APP-2026030102', student_name: 'Rahul Verma', status: 'pending', documents: [
        { type: '10th Certificate', verified: true },
        { type: '12th Certificate', verified: true },
        { type: 'Caste Certificate', verified: false }
      ]}
    ];
  }

  getStatusClass(status: string): string {
    const classes: Record<string, string> = {
      'pending': 'bg-amber-500/20 text-amber-400',
      'verified': 'bg-emerald-500/20 text-emerald-400',
      'rejected': 'bg-red-500/20 text-red-400'
    };
    return classes[status] || 'bg-zinc-500/20 text-zinc-400';
  }
}
