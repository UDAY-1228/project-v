import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-timetable-logout',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="min-h-screen bg-zinc-950 flex items-center justify-center"><h1 class="text-4xl font-black text-white">Logging out...</h1></div>'
})
export class LogoutComponent {
  constructor() { setTimeout(() => { console.log('Logged out'); }, 1000); }
}
