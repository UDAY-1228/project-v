import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-timetable',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './timetable.component.html',
  styleUrls: ['./timetable.component.css']
})
export class TimetableComponent implements OnInit {
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  timeSlots = ['09:00', '10:00', '11:00', '12:00', '01:00', '02:00', '03:00', '04:00'];
  timetable: any = {};
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.timetable = {
        'Monday': {
          '09:00': { subject: 'Data Structures', lecturer: 'Dr. Neeraj', room: 'R101' },
          '11:00': { subject: 'Database Systems', lecturer: 'Prof. Anjali', room: 'R205' }
        },
        'Wednesday': {
          '10:00': { subject: 'Discrete Mathematics', lecturer: 'Dr. Ramanujan', room: 'R302' },
          '02:00': { subject: 'Operating Systems', lecturer: 'Dr. Tanenbaum', room: 'R105' }
        }
      };
      this.isLoading = false;
    }, 800);
  }

  getEntry(day: string, time: string) {
    return this.timetable[day]?.[time] || null;
  }
}
