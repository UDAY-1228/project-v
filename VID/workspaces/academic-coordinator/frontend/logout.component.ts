import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="h-screen w-full bg-zinc-950 flex flex-col items-center justify-center font-sans">
        <div class="relative">
          <div class="w-24 h-24 border-2 border-indigo-500/20 rounded-full animate-ping"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <svg class="w-10 h-10 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          </div>
        </div>
        <h2 class="mt-8 text-2xl font-black text-white tracking-widest uppercase italic">Deauthenticating</h2>
        <p class="mt-2 text-zinc-600 font-medium tracking-wide">Securing institutional session and redirecting...</p>
    </div>
  `,
  styles: [`
    :host { display: block; }
  `]
})
export class LogoutComponent implements OnInit {
  ngOnInit(): void {
    setTimeout(() => {
      console.log('User logged out. Redirecting to login...');
    }, 2000);
  }
}
