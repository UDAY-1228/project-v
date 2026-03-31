import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-common-register',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  firstName = '';
  lastName = '';
  email = '';
  password = '';
  confirmPassword = '';
  agreeToTerms = false;
  isLoading = false;
  errorMessage = '';
  successMessage = '';

  constructor(private router: Router) {}

  ngOnInit(): void {}

  onSubmit(): void {
    if (!this.firstName || !this.email || !this.password) {
      this.errorMessage = 'Please fill in required fields';
      return;
    }
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'Passwords do not match';
      return;
    }
    this.isLoading = true;
    this.errorMessage = '';
    setTimeout(() => {
      this.successMessage = 'Account created! Check your email to verify.';
      this.isLoading = false;
      setTimeout(() => this.router.navigate(['/login']), 3000);
    }, 2000);
  }

  login(): void {
    this.router.navigate(['/login']);
  }
}
