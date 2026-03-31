import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-exam-schedule',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './exam-schedule.component.html',
  styleUrls: ['./exam-schedule.component.css']
})
export class ExamScheduleComponent implements OnInit {
  exams: any[] = [];
  isLoading = true;
  showModal = false;

  ngOnInit(): void {
    this.fetchExams();
  }

  fetchExams() {
    setTimeout(() => {
      this.exams = [
        { id: '1', exam_name: 'Mathematics Mid-Term', course: 'B.Sc Mathematics', date: '2026-04-15', time: '09:00 - 12:00', venue: 'Hall A', status: 'scheduled' },
        { id: '2', exam_name: 'Physics Final', course: 'B.Sc Physics', date: '2026-04-18', time: '14:00 - 17:00', venue: 'Hall B', status: 'scheduled' },
        { id: '3', exam_name: 'Chemistry Practical', course: 'B.Sc Chemistry', date: '2026-04-20', time: '10:00 - 13:00', venue: 'Lab 1', status: 'pending' },
      ];
      this.isLoading = false;
    }, 600);
  }

  openModal() { this.showModal = true; }
  closeModal() { this.showModal = false; }
}
