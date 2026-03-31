import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-examination-logout',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="min-h-screen bg-zinc-950 flex items-center justify-center">
      <div class="text-center">
        <h1 class="text-4xl font-black text-white mb-4">Logging out...</h1>
        <p class="text-zinc-500">Please wait while we securely log you out.</p>
      </div>
    </div>
  `
})
export class LogoutComponent {
  constructor() {
    setTimeout(() => { console.log('Logged out'); }, 1000);
  }
}
