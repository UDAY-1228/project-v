import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  monthlyData = [
    { month: 'January 2026', present: 22, absent: 2, percentage: 92 },
    { month: 'February 2026', present: 20, absent: 1, percentage: 95 },
    { month: 'March 2026', present: 15, absent: 0, percentage: 100 }
  ];

  ngOnInit(): void {}
}
