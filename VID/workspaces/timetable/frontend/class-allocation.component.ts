import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-class-allocation',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './class-allocation.component.html',
  styleUrls: ['./class-allocation.component.css']
})
export class ClassAllocationComponent implements OnInit {
  classes: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.fetchClasses();
  }

  fetchClasses() {
    setTimeout(() => {
      this.classes = [
        { id: '1', name: 'CS-A', course: 'B.Sc CS', semester: '5', students: 60, faculty_advisor: 'Dr. Smith' },
        { id: '2', name: 'CS-B', course: 'B.Sc CS', semester: '5', students: 55, faculty_advisor: 'Prof. Jones' },
        { id: '3', name: 'Math-A', course: 'B.Sc Math', semester: '3', students: 45, faculty_advisor: 'Dr. Brown' },
      ];
      this.isLoading = false;
    }, 600);
  }

  addClass() { console.log('Adding class...'); }
}
