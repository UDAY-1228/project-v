import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-leave-requests',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './leave-requests.component.html',
  styleUrls: ['./leave-requests.component.css']
})
export class LeaveRequestsComponent implements OnInit {
  requests: any[] = [];
  balance = { casual: 12, sick: 10, earned: 15, unpaid: 0 };
  isLoading = true;

  ngOnInit(): void {
    this.loadRequests();
  }

  loadRequests() {
    setTimeout(() => {
      this.requests = [
        { id: '1', type: 'Casual Leave', startDate: new Date(), endDate: new Date(), status: 'pending', reason: 'Personal work' },
        { id: '2', type: 'Sick Leave', startDate: new Date(Date.now() - 604800000), endDate: new Date(Date.now() - 518400000), status: 'approved', reason: 'Medical appointment' },
      ];
      this.isLoading = false;
    }, 800);
  }

  getStatusClass(status: string): string {
    const classes: any = { pending: 'text-yellow-400 bg-yellow-400/10', approved: 'text-emerald-400 bg-emerald-400/10', rejected: 'text-red-400 bg-red-400/10' };
    return classes[status] || 'text-zinc-400 bg-zinc-400/10';
  }
}
