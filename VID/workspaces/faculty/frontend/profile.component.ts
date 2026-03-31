import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profile = {
    faculty_id: 'FAC001',
    first_name: 'Rajesh',
    last_name: 'Sharma',
    email: 'rajesh.sharma@university.edu',
    phone: '+91 98765 43210',
    department: 'Computer Science & Engineering',
    designation: 'Associate Professor',
    qualification: 'Ph.D. in Computer Science',
    specialization: 'Machine Learning, Data Structures',
    experience_years: 12,
    date_of_joining: '2014-07-15',
    office_location: 'Room 305, Block C',
    office_hours: 'Mon-Fri, 10:00 AM - 4:00 PM',
    bio: 'Passionate educator with over 12 years of experience in teaching and research. Specialized in algorithms, data structures, and machine learning.',
    profile_image_url: ''
  };

  stats = {
    total_classes: 6,
    total_students: 180,
    papers_published: 28,
    years_experience: 12
  };

  isEditing = false;
  isLoading = false;

  ngOnInit(): void {
    this.fetchProfile();
  }

  fetchProfile() {
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
    }, 500);
  }

  toggleEdit() {
    this.isEditing = !this.isEditing;
  }

  saveProfile() {
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      this.isEditing = false;
      alert('Profile updated successfully!');
    }, 800);
  }
}
