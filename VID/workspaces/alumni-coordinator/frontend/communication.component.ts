import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-communication',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './communication.component.html',
  styleUrls: ['./communication.component.css']
})
export class CommunicationComponent implements OnInit {
  communications: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadCommunications();
  }

  loadCommunications() {
    setTimeout(() => {
      this.communications = [
        { id: '1', title: 'March Newsletter 2026', message: 'Updates from campus and alumni achievements', sentAt: new Date('2026-03-01'), sentCount: 245, openedCount: 180, clickedCount: 45, status: 'sent' },
        { id: '2', title: 'Annual Meet Invitation', message: 'You are invited to our Annual Alumni Meet', sentAt: new Date('2026-02-15'), sentCount: 300, openedCount: 250, clickedCount: 200, status: 'sent' },
        { id: '3', title: 'Career Fair Announcement', message: 'Join us for the upcoming career fair', sentAt: new Date('2026-02-01'), sentCount: 280, openedCount: 190, clickedCount: 120, status: 'sent' }
      ];
      this.isLoading = false;
    }, 500);
  }
}
