import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-member-records',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './member-records.component.html',
  styleUrls: ['./member-records.component.css']
})
export class MemberRecordsComponent implements OnInit {
  members: any[] = [];

  ngOnInit(): void {
    this.members = [
      { member_id: 'MBR-001', name: 'Priya Sharma', type: 'Student', books_issued: 2, expiry: new Date(), status: 'active' },
      { member_id: 'MBR-002', name: 'Rahul Verma', type: 'Faculty', books_issued: 3, expiry: new Date(), status: 'active' },
      { member_id: 'MBR-003', name: 'Sneha Patel', type: 'Student', books_issued: 1, expiry: new Date(), status: 'active' },
      { member_id: 'MBR-004', name: 'Amit Kumar', type: 'Staff', books_issued: 0, expiry: new Date(), status: 'expired' }
    ];
  }
}
