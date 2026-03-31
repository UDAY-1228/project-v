import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-attendance',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  records: any[] = [];
  isLoading = true;
  checkedIn = false;

  ngOnInit(): void {
    this.loadAttendanceRecords();
  }

  loadAttendanceRecords() {
    setTimeout(() => {
      this.records = [
        { date: new Date(), checkIn: '09:00', checkOut: '18:00', hoursWorked: 9, status: 'present' },
        { date: new Date(Date.now() - 86400000), checkIn: '09:15', checkOut: '17:45', hoursWorked: 8.5, status: 'present' },
        { date: new Date(Date.now() - 172800000), checkIn: '09:00', checkOut: '18:00', hoursWorked: 9, status: 'present' },
      ];
      this.isLoading = false;
    }, 800);
  }

  checkIn() {
    this.checkedIn = true;
  }

  checkOut() {
    this.checkedIn = false;
  }
}
