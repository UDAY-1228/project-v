import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-research-projects',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './research-projects.component.html',
  styleUrls: ['./research-projects.component.css']
})
export class ResearchProjectsComponent implements OnInit {
  projects: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.projects = [
        { id: '1', title: 'AI in Healthcare', pi: 'Dr. Kumar', dept: 'CSE', status: 'in_progress', budget: 5000000 },
        { id: '2', title: 'Renewable Energy Systems', pi: 'Dr. Sharma', dept: 'ECE', status: 'completed', budget: 3000000 },
        { id: '3', title: 'Smart City IoT', pi: 'Dr. Patel', dept: 'CSE', status: 'in_progress', budget: 7500000 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
