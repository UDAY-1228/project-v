import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {
  isLoggingOut = false;

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.performLogout();
  }

  performLogout(): void {
    this.isLoggingOut = true;
    setTimeout(() => {
      this.router.navigate(['/login']);
    }, 1500);
  }
}
