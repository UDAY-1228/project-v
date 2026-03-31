import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Profile {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  bio: string;
  organization: string;
  department: string;
  designation: string;
  location: string;
  website: string;
}

@Component({
  selector: 'app-common-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profile: Profile = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    phone: '+1 234 567 8900',
    bio: 'Software developer passionate about AI and machine learning.',
    organization: 'Tech Corp',
    department: 'Engineering',
    designation: 'Senior Developer',
    location: 'San Francisco, CA',
    website: 'https://johndoe.dev'
  };
  isEditing = false;
  isLoading = false;
  editForm: Profile = { ...this.profile };

  ngOnInit(): void {}

  toggleEdit(): void {
    this.isEditing = !this.isEditing;
    if (this.isEditing) {
      this.editForm = { ...this.profile };
    }
  }

  saveProfile(): void {
    this.isLoading = true;
    setTimeout(() => {
      this.profile = { ...this.editForm };
      this.isEditing = false;
      this.isLoading = false;
    }, 1000);
  }

  cancelEdit(): void {
    this.isEditing = false;
    this.editForm = { ...this.profile };
  }
}
