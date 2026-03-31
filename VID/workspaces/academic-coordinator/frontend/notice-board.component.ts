import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-notice-board',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './notice-board.component.html',
  styleUrls: ['./notice-board.component.css']
})
export class NoticeBoardComponent implements OnInit {
  notices: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.notices = [
        { id: '1', title: 'Cycle Test Schedule', content: 'Detailed timetable for upcoming cycle tests has been posted.', category: 'exam', priority: 'high', date: '2024-03-22', views: 245, pinned: true },
        { id: '2', title: 'Faculty Meeting', content: 'Urgent meeting regarding the new syllabus rollout plan.', category: 'academic', priority: 'urgent', date: '2024-03-23', views: 89, pinned: false },
        { id: '3', title: 'Tech Fest 2024', content: 'Registrations are now open for the annual technical fest.', category: 'event', priority: 'normal', date: '2024-03-25', views: 1102, pinned: false }
      ];
      this.isLoading = false;
    }, 800);
  }
}
