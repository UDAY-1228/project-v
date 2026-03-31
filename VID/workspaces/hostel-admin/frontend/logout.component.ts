import { Component } from '@angular/core';
@Component({
  selector: 'app-logout',
  standalone: true,
  template: '<div class="min-h-screen bg-zinc-950 flex items-center justify-center"><p class="text-white">Logging out...</p></div>',
  styles: [':host { display: block; }']
})
export class LogoutComponent {
  constructor() {
    localStorage.clear();
    window.location.href = '/login';
  }
}
