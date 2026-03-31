import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {
  ngOnInit(): void {
    setTimeout(() => {
      console.log('Faculty session terminated. Redirecting to login...');
      window.location.href = '/login';
    }, 2000);
  }
}
