import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Notification {
  notificationId: string;
  title: string;
  message: string;
  type: string;
  isRead: boolean;
  priority: string;
  relatedId?: string;
  relatedType?: string;
  sentAt: string;
  readAt?: string;
}

@Component({
  selector: 'app-notifications',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent implements OnInit {
  notifications: Notification[] = [];
  unreadCount = 0;

  private apiBase = '/api/student';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadNotifications();
    this.loadUnreadCount();
  }

  private getStudentId(): string {
    return localStorage.getItem('studentId') || 'STU001';
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'X-Student-Id': this.getStudentId()
    });
  }

  loadNotifications(): void {
    this.http.get<Notification[]>(`${this.apiBase}/notifications?limit=100`, { headers: this.getHeaders() })
      .subscribe({
        next: (notifications) => this.notifications = notifications,
        error: (err) => console.error('Failed to load notifications:', err)
      });
  }

  loadUnreadCount(): void {
    this.http.get<{ unreadCount: number }>(`${this.apiBase}/notifications/unread-count`, { headers: this.getHeaders() })
      .subscribe({
        next: (data) => this.unreadCount = data.unreadCount,
        error: (err) => console.error('Failed to load unread count:', err)
      });
  }

  markAsRead(notification: Notification): void {
    if (notification.isRead) return;

    this.http.put(`${this.apiBase}/notifications/${notification.notificationId}/read`, {})
      .subscribe({
        next: () => {
          notification.isRead = true;
          this.unreadCount = Math.max(0, this.unreadCount - 1);
        },
        error: (err) => console.error('Failed to mark as read:', err)
      });
  }

  markAllAsRead(): void {
    this.http.put(`${this.apiBase}/notifications/read-all`, {})
      .subscribe({
        next: () => {
          this.notifications.forEach(n => n.isRead = true);
          this.unreadCount = 0;
        },
        error: (err) => console.error('Failed to mark all as read:', err)
      });
  }

  getNotificationIcon(type: string): string {
    const icons: Record<string, string> = {
      'general': '📢',
      'academic': '📚',
      'fee': '💰',
      'event': '🎉',
      'attendance': '📋',
      'exam': '📝',
      'result': '🎓'
    };
    return icons[type] || '📢';
  }

  formatTime(dateStr: string): string {
    const date = new Date(dateStr);
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const minutes = Math.floor(diff / (1000 * 60));
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const days = Math.floor(hours / 24);

    if (minutes < 1) return 'Just now';
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    if (days < 7) return `${days}d ago`;
    return date.toLocaleDateString();
  }
}
