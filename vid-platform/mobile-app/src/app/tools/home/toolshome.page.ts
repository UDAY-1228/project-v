import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-toolshome',
  template: `
    <ion-header [translucent]="true">
      <ion-toolbar color="primary">
        <ion-title>VID Tools Hub</ion-title>
        <ion-buttons slot="end">
            <ion-badge [color]="backendStatus === 'connected' ? 'success' : 'danger'">
                {{ backendStatus }}
            </ion-badge>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content [fullscreen]="true" class="ion-padding">
      <div class="welcome-card ion-margin-bottom">
        <h2 class="ion-no-margin font-bold text-2xl text-primary">Unified System Hub</h2>
        <p class="text-gray-500">Connected to VID Backend v1.0</p>
      </div>

      <ion-list>
        <ion-item-group *ngFor="let module of platformConfig?.modules">
            <ion-item-divider>
                <ion-label>{{ module.name }}</ion-label>
            </ion-item-divider>
            <ion-item [routerLink]="['/', module.id]" detail="true" [disabled]="!module.enabled">
                <ion-label>
                    <h2>Access Module</h2>
                    <p>{{ module.enabled ? 'Ready to use' : 'Under Maintenance' }}</p>
                </ion-label>
            </ion-item>
        </ion-item-group>
      </ion-list>
    </ion-content>
  `,
  styles: []
})
export class ToolsHomePage implements OnInit {
  backendStatus: string = 'loading';
  platformConfig: any;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.apiService.getConfig().subscribe({
      next: (config) => {
        this.platformConfig = config;
        this.backendStatus = 'connected';
      },
      error: () => {
        this.backendStatus = 'offline';
      }
    });
  }
}
