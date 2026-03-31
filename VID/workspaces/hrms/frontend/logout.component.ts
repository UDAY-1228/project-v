import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit, OnDestroy {
  sessionDuration = '0h 0m';
  lastActivity = 'Just now';
  
  private sessionStart: Date = new Date();
  private activityInterval: any;

  constructor(private router: Router) {}

  ngOnInit() {
    const storedSession = localStorage.getItem('session_start');
    if (storedSession) {
      this.sessionStart = new Date(storedSession);
    } else {
      localStorage.setItem('session_start', this.sessionStart.toISOString());
    }
    
    this.updateSessionDuration();
    this.activityInterval = setInterval(() => {
      this.updateSessionDuration();
    }, 60000);
  }

  ngOnDestroy() {
    if (this.activityInterval) {
      clearInterval(this.activityInterval);
    }
  }

  updateSessionDuration() {
    const now = new Date();
    const diff = now.getTime() - this.sessionStart.getTime();
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    this.sessionDuration = `${hours}h ${minutes}m`;
    
    const activityDiff = now.getTime() - this.sessionStart.getTime();
    if (activityDiff < 60000) {
      this.lastActivity = 'Just now';
    } else if (activityDiff < 3600000) {
      const mins = Math.floor(activityDiff / 60000);
      this.lastActivity = `${mins} minute${mins > 1 ? 's' : ''} ago`;
    } else {
      const hrs = Math.floor(activityDiff / 3600000);
      this.lastActivity = `${hrs} hour${hrs > 1 ? 's' : ''} ago`;
    }
  }

  goBack() {
    this.router.navigate(['/dashboard']);
  }

  confirmLogout() {
    localStorage.removeItem('session_start');
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user_data');
    
    console.log('User logged out successfully');
    
    this.router.navigate(['/login']);
  }
}
