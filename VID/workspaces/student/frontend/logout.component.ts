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
  studentName = '';
  countdown = 5;
  progress = 0;
  private intervalId: any;

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.studentName = localStorage.getItem('studentName') || 'Student';
    this.performLogout();
    this.startCountdown();
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  performLogout(): void {
    localStorage.removeItem('studentId');
    localStorage.removeItem('studentName');
    localStorage.removeItem('authToken');
    sessionStorage.clear();
  }

  startCountdown(): void {
    this.intervalId = setInterval(() => {
      this.countdown--;
      this.progress = ((5 - this.countdown) / 5) * 100;
      
      if (this.countdown <= 0) {
        this.navigateToLogin();
      }
    }, 1000);
  }

  stayLoggedIn(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
    this.router.navigate(['/dashboard']);
  }

  loginAgain(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
    this.navigateToLogin();
  }

  private navigateToLogin(): void {
    window.location.href = '/login';
  }
}
