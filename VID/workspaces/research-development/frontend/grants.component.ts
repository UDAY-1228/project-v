import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-grants',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './grants.component.html',
  styleUrls: ['./grants.component.css']
})
export class GrantsComponent implements OnInit {
  grants: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.grants = [
        { id: '1', title: 'DST Research Grant', agency: 'DST', pi: 'Dr. Kumar', amount: 5000000, status: 'approved', deadline: new Date() },
        { id: '2', title: 'UGC Major Project', agency: 'UGC', pi: 'Dr. Sharma', amount: 3000000, status: 'pending', deadline: new Date() }
      ];
      this.isLoading = false;
    }, 800);
  }
}
