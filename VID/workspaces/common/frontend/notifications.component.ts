import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Notification {
  id: string;
  title: string;
  message: string;
  type: string;
  priority: string;
  isRead: boolean;
  timestamp: Date;
}

@Component({
  selector: 'app-common-notifications',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent implements OnInit {
  notifications: Notification[] = [];
  isLoading = true;
  filterUnread = false;

  ngOnInit(): void {
    setTimeout(() => {
      this.notifications = [
        { id: '1', title: 'Welcome!', message: 'Your account is ready to use.', type: 'success', priority: 'normal', isRead: false, timestamp: new Date() },
        { id: '2', title: 'New Feature', message: 'Check out our latest updates.', type: 'info', priority: 'low', isRead: false, timestamp: new Date(Date.now() - 3600000) },
        { id: '3', title: 'Reminder', message: 'Complete your profile setup.', type: 'warning', priority: 'high', isRead: true, timestamp: new Date(Date.now() - 86400000) }
      ];
      this.isLoading = false;
    }, 800);
  }

  get unreadCount(): number {
    return this.notifications.filter(n => !n.isRead).length;
  }

  markAsRead(notification: Notification): void {
    notification.isRead = true;
  }

  markAllAsRead(): void {
    this.notifications.forEach(n => n.isRead = true);
  }

  deleteNotification(id: string): void {
    this.notifications = this.notifications.filter(n => n.id !== id);
  }

  getTypeIcon(type: string): string {
    const icons: Record<string, string> = {
      success: 'M5 13l4 4L19 7',
      info: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
      warning: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z',
      error: 'M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z'
    };
    return icons[type] || icons['info'];
  }
}
