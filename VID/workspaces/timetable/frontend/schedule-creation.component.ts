import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-schedule-creation',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './schedule-creation.component.html',
  styleUrls: ['./schedule-creation.component.css']
})
export class ScheduleCreationComponent implements OnInit {
  schedules: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchSchedules();
  }

  fetchSchedules() {
    setTimeout(() => {
      this.schedules = [
        { id: '1', name: 'B.Sc CS Sem 5', course: 'B.Sc Computer Science', semester: '5', sections: 3, status: 'published' },
        { id: '2', name: 'B.Sc Math Sem 3', course: 'B.Sc Mathematics', semester: '3', sections: 2, status: 'draft' },
        { id: '3', name: 'B.Sc Phy Sem 5', course: 'B.Sc Physics', semester: '5', sections: 2, status: 'published' },
      ];
      this.isLoading = false;
    }, 600);
  }

  createSchedule() { console.log('Creating schedule...'); }
  publishSchedule(id: string) { console.log('Publishing:', id); }
}
