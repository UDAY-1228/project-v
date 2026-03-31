import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-staff-stats',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './staff-stats.component.html',
  styleUrls: ['./staff-stats.component.css']
})
export class StaffStatsComponent implements OnInit {
  departments: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.departments = [
        { name: 'Computer Science', teaching: 45, non_teaching: 12, phd: 20, experience: 8.5 },
        { name: 'Electronics', teaching: 38, non_teaching: 10, phd: 15, experience: 7.2 },
        { name: 'Mechanical', teaching: 42, non_teaching: 15, phd: 12, experience: 6.8 },
        { name: 'Civil', teaching: 30, non_teaching: 8, phd: 8, experience: 9.1 }
      ];
      this.isLoading = false;
    }, 800);
  }
}
