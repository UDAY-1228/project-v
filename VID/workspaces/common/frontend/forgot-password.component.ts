import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-common-forgot-password',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.css']
})
export class ForgotPasswordComponent implements OnInit {
  email = '';
  isLoading = false;
  successMessage = '';
  errorMessage = '';

  constructor(private router: Router) {}

  ngOnInit(): void {}

  onSubmit(): void {
    if (!this.email) {
      this.errorMessage = 'Please enter your email';
      return;
    }
    this.isLoading = true;
    this.errorMessage = '';
    setTimeout(() => {
      this.successMessage = 'Password reset link sent! Check your email.';
      this.isLoading = false;
    }, 1500);
  }

  login(): void {
    this.router.navigate(['/login']);
  }
}
