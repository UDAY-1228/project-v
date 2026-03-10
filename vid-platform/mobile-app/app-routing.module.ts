import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
    {
        path: '',
        loadChildren: () => import('./tabs/tabs.module').then(m => m.TabsPageModule)
    },
    {
        path: 'login',
        loadChildren: () => import('./auth/login/login.module').then(m => m.LoginPageModule)
    },
    {
        path: 'virtual-id',
        loadChildren: () => import('./profile/virtual-id/virtual-id.module').then(m => m.VirtualIdPageModule)
    },
    {
        path: 'attendance',
        loadChildren: () => import('./academic/attendance/attendance.module').then(m => m.AttendancePageModule)
    },
    {
        path: 'homework-ai',
        loadChildren: () => import('./lms/homework-assistant/homework-assistant.module').then(m => m.HomeworkAssistantPageModule)
    }
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
    ],
    exports: [RouterModule]
})
export class AppRoutingModule { }
