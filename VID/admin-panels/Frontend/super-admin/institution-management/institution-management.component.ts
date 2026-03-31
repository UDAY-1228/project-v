import { Component } from '@angular/core';

@Component({
  selector: 'app-institution-management',
  templateUrl: './institution-management.component.html',
  styleUrls: ['./institution-management.component.css']
})
export class InstitutionManagementComponent {
  institutions = [
    { id: '1', name: 'Example University', code: 'EU001', is_active: true },
    { id: '2', name: 'Global Academy', code: 'GA101', is_active: false }
  ];

  createInstitution() {
    console.log('Creating institution...');
  }

  updateInstitution(id: string) {
    console.log('Updating institution:', id);
  }

  deleteInstitution(id: string) {
    console.log('Deleting institution:', id);
  }

  toggleActivation(id: string) {
    console.log('Toggling activation for institution:', id);
  }
}
