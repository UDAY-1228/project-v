import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  template: `
    <ion-content [fullscreen]="true" class="ion-no-padding">
      <div class="login-container">
        <!-- Top decorative section -->
        <div class="top-section">
          <div class="branding">
            <h1 class="logo-text">DOLLA</h1>
            <p class="subtitle">Academic Management</p>
          </div>
          <div class="decor-circle circle-1"></div>
          <div class="decor-circle circle-2"></div>
        </div>

        <!-- Form section -->
        <div class="form-section">
          <div class="form-header">
            <h2>Welcome Back</h2>
            <p>Sign in to continue</p>
          </div>

          <form (submit)="onLogin($event)">
            <div class="input-group">
              <ion-item lines="none" class="custom-input">
                <ion-icon name="person-outline" slot="start"></ion-icon>
                <ion-input [(ngModel)]="username" name="username" type="text" placeholder="Username"></ion-input>
              </ion-item>
            </div>

            <div class="input-group">
              <ion-item lines="none" class="custom-input">
                <ion-icon name="lock-closed-outline" slot="start"></ion-icon>
                <ion-input [(ngModel)]="password" name="password" type="password" placeholder="Password"></ion-input>
              </ion-item>
              <div class="forgot-link">
                <a href="#">Forgot Password?</a>
              </div>
            </div>

            <ion-button expand="block" type="submit" class="login-btn" color="primary">
              Sign In
              <ion-icon name="arrow-forward-outline" slot="end"></ion-icon>
            </ion-button>
            
            <div class="quick-login">
               <p>Quick Login</p>
               <div class="role-buttons">
                  <ion-button fill="outline" size="small" (click)="setRole('superadmin')">Admin</ion-button>
                  <ion-button fill="outline" size="small" (click)="setRole('teacher')">Teacher</ion-button>
                  <ion-button fill="outline" size="small" (click)="setRole('student')">Student</ion-button>
               </div>
            </div>
          </form>
        </div>
      </div>

      <style>
        .login-container {
          height: 100vh;
          display: flex;
          flex-direction: column;
          background: #f8fafc;
        }

        /* Top Section */
        .top-section {
          flex: 0.4;
          background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
          position: relative;
          overflow: hidden;
          display: flex;
          align-items: center;
          justify-content: center;
          border-bottom-left-radius: 40px;
          border-bottom-right-radius: 40px;
          box-shadow: 0 10px 30px rgba(79, 70, 229, 0.2);
        }

        .branding {
          text-align: center;
          color: white;
          z-index: 10;
        }

        .logo-text {
          font-size: 2.5rem;
          font-weight: 800;
          letter-spacing: 2px;
          margin: 0;
          text-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .subtitle {
          font-size: 1rem;
          opacity: 0.8;
          margin-top: 5px;
        }

        .decor-circle {
          position: absolute;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.1);
        }

        .circle-1 {
          width: 300px;
          height: 300px;
          top: -100px;
          right: -100px;
        }

        .circle-2 {
          width: 200px;
          height: 200px;
          bottom: -50px;
          left: -50px;
        }

        /* Form Section */
        .form-section {
          flex: 0.6;
          padding: 40px 24px;
          background: #f8fafc;
        }

        .form-header {
          margin-bottom: 30px;
        }

        .form-header h2 {
          font-size: 1.8rem;
          font-weight: 700;
          color: #1e293b;
          margin: 0;
        }

        .form-header p {
          color: #64748b;
          margin-top: 5px;
        }

        .input-group {
          margin-bottom: 20px;
        }

        .custom-input {
          --background: white;
          --border-radius: 16px;
          --padding-start: 16px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.03);
          border: 1px solid #e2e8f0;
          margin-bottom: 15px;
        }

        .custom-input ion-icon {
          color: #94a3b8;
          margin-right: 12px;
        }

        .forgot-link {
          text-align: right;
          margin-top: -5px;
        }

        .forgot-link a {
          color: #4f46e5;
          font-size: 0.9rem;
          text-decoration: none;
          font-weight: 500;
        }

        .login-btn {
          margin-top: 30px;
          --border-radius: 16px;
          --padding-top: 18px;
          --padding-bottom: 18px;
          --background: #4f46e5;
          --background-hover: #4338ca;
          font-weight: 600;
          font-size: 1.1rem;
          box-shadow: 0 10px 25px rgba(79, 70, 229, 0.3);
        }
        
        .quick-login {
          margin-top: 40px;
          text-align: center;
        }
        .quick-login p {
           color: #94a3b8;
           font-size: 0.85rem;
           text-transform: uppercase;
           letter-spacing: 1px;
           margin-bottom: 15px;
        }
        .role-buttons {
           display: flex;
           justify-content: center;
           gap: 10px;
        }
      </style>
    </ion-content>
  `,
  styles: []
})
export class LoginPage implements OnInit {
  username = '';
  password = '';

  constructor(private router: Router) { }

  ngOnInit() { }

  setRole(role: string) {
    this.username = role;
    this.password = role === 'teacher' ? 'teacher123' : 'admin123';
  }

  onLogin(e: Event) {
    e.preventDefault();
    if(this.username && this.password) {
       // Mock route mapping
       this.router.navigate(['/', 'analytics', 'institution']); 
    }
  }
}

