import { Component } from '@angular/core';

@Component({
  selector: 'app-pd-logout',
  standalone: true,
  template: '<div class="min-h-screen bg-zinc-950 flex items-center justify-center"><p class="text-white text-xl">Logging out...</p></div>'
})
export class LogoutComponent {
  constructor() {
    setTimeout(() => { console.log('Logged out'); }, 1000);
  }
}
