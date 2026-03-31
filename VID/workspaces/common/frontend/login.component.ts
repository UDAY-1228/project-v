import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-common-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email = '';
  password = '';
  rememberMe = false;
  isLoading = false;
  errorMessage = '';
  showPassword = false;

  constructor(private router: Router) {}

  ngOnInit(): void {}

  async onSubmit(): Promise<void> {
    if (!this.email || !this.password) {
      this.errorMessage = 'Please enter both email and password';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';

    setTimeout(() => {
      if (this.email === 'demo@example.com' && this.password === 'demo') {
        this.router.navigate(['/dashboard']);
      } else {
        this.errorMessage = 'Invalid email or password';
      }
      this.isLoading = false;
    }, 1500);
  }

  togglePassword(): void {
    this.showPassword = !this.showPassword;
  }

  forgotPassword(): void {
    this.router.navigate(['/forgot-password']);
  }

  register(): void {
    this.router.navigate(['/register']);
  }
}
