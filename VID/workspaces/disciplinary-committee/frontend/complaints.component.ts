import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-complaints',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './complaints.component.html',
  styleUrls: ['./complaints.component.css']
})
export class ComplaintsComponent implements OnInit {
  complaints: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.complaints = [
        { id: '1', title: 'Academic Dishonesty', type: 'academic', priority: 'high', status: 'pending', reporter: 'Dr. Smith', date: new Date() },
        { id: '2', title: 'Harassment Complaint', type: 'conduct', priority: 'urgent', status: 'investigating', reporter: 'Student A', date: new Date() },
        { id: '3', title: 'Infrastructure Damage', type: 'property', priority: 'medium', status: 'resolved', reporter: 'Admin', date: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
