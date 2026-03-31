import { Component } from '@angular/core';
@Component({ selector: 'app-rd-logout', standalone: true, template: '<div class="min-h-screen bg-zinc-950 flex items-center justify-center"><p class="text-white">Logging out...</p></div>' })
export class LogoutComponent { constructor() { setTimeout(() => {}, 1000); } }
