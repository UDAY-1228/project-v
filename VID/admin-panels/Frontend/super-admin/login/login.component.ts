import { Component } from '@angular/core';

@Component({
  selector: 'app-super-admin-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginData = { username: '', password: '' };
  onSubmit() {
    console.log('Logging in to Super Admin panel...');
  }
}
