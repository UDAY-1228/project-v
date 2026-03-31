import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-notifications',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent implements OnInit {
  notifications = [
    { id: '1', title: 'Fee Payment Reminder', message: 'Q2 tuition fee is due on April 15th', notificationType: 'Fee', isRead: false, createdAt: new Date() },
    { id: '2', title: 'Parent-Teacher Meeting', message: 'Scheduled for March 20th at 4 PM', notificationType: 'Event', isRead: false, createdAt: new Date() },
    { id: '3', title: 'Exam Schedule Released', message: 'Mid-term exam schedule is now available', notificationType: 'Academic', isRead: true, createdAt: new Date() },
    { id: '4', title: 'Holiday Notice', message: 'School will be closed from March 25-30', notificationType: 'General', isRead: true, createdAt: new Date() }
  ];

  ngOnInit(): void {}
}
