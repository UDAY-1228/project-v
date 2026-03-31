import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-health-records',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './health-records.component.html',
  styleUrls: ['./health-records.component.css']
})
export class HealthRecordsComponent implements OnInit {
  records: any[] = [];
  isLoading = true;

  constructor() {}

  ngOnInit(): void {
    this.fetchRecords();
  }

  fetchRecords() {
    setTimeout(() => {
      this.records = [
        { id: '1', student_id: 'STU001', student_name: 'Rahul Sharma', blood_group: 'O+', height_cm: 165, weight_kg: 58, allergies: ['Dust'], last_checkup: new Date('2024-01-15') },
        { id: '2', student_id: 'STU002', student_name: 'Priya Patel', blood_group: 'A+', height_cm: 155, weight_kg: 48, allergies: [], last_checkup: new Date('2024-02-20') },
        { id: '3', student_id: 'STU003', student_name: 'Amit Kumar', blood_group: 'B+', height_cm: 170, weight_kg: 65, allergies: ['Peanuts'], last_checkup: new Date('2024-03-10') }
      ];
      this.isLoading = false;
    }, 800);
  }
}
