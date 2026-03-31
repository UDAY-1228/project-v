import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-hall-tickets',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './hall-tickets.component.html',
  styleUrls: ['./hall-tickets.component.css']
})
export class HallTicketsComponent implements OnInit {
  tickets: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchTickets();
  }

  fetchTickets() {
    setTimeout(() => {
      this.tickets = [
        { id: '1', student_name: 'John Doe', roll_number: 'CS2024001', course: 'B.Sc CS', semester: '5', session: '2026', status: 'issued' },
        { id: '2', student_name: 'Jane Smith', roll_number: 'CS2024002', course: 'B.Sc CS', semester: '5', session: '2026', status: 'issued' },
        { id: '3', student_name: 'Bob Wilson', roll_number: 'CS2024003', course: 'B.Sc CS', semester: '5', session: '2026', status: 'pending' },
      ];
      this.isLoading = false;
    }, 600);
  }

  generateTickets() { console.log('Generating tickets...'); }
  verifyTicket(id: string) { console.log('Verifying ticket:', id); }
}
