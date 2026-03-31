import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-profile',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profile = {
    fullName: 'John Doe',
    email: 'john.doe@company.com',
    phone: '+1 234 567 8900',
    department: 'Engineering',
    designation: 'Senior Developer',
    dateOfJoining: new Date('2022-03-15'),
  };
  isLoading = false;

  ngOnInit(): void {}

  saveProfile() {
    this.isLoading = true;
    setTimeout(() => this.isLoading = false, 1000);
  }
}
