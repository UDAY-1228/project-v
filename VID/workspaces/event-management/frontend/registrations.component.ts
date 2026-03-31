import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-registrations',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './registrations.component.html',
  styleUrls: ['./registrations.component.css']
})
export class RegistrationsComponent implements OnInit {
  registrations: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadRegistrations();
  }

  loadRegistrations() {
    setTimeout(() => {
      this.registrations = [
        { id: '1', name: 'John Smith', email: 'john@example.com', event: 'Tech Conference', date: new Date(), status: 'confirmed', payment: 'paid' },
        { id: '2', name: 'Sarah Johnson', email: 'sarah@example.com', event: 'Tech Conference', date: new Date(), status: 'confirmed', payment: 'paid' },
        { id: '3', name: 'Mike Brown', email: 'mike@example.com', event: 'Startup Pitch', date: new Date(), status: 'pending', payment: 'unpaid' },
      ];
      this.isLoading = false;
    }, 800);
  }

  checkIn(id: string) {
    const reg = this.registrations.find(r => r.id === id);
    if (reg) reg.status = 'checked-in';
  }
}
