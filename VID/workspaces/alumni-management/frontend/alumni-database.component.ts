import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-alumni-database',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './alumni-database.component.html',
  styleUrls: ['./alumni-database.component.css']
})
export class AlumniDatabaseComponent implements OnInit {
  alumniRecords: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadAlumniRecords();
  }

  loadAlumniRecords() {
    setTimeout(() => {
      this.alumniRecords = [
        { id: '1', firstName: 'Sarah', lastName: 'Johnson', email: 'sarah.j@email.com', graduationYear: 2020, degree: 'B.Tech CS', currentCompany: 'Google', isVerified: true },
        { id: '2', firstName: 'Michael', lastName: 'Chen', email: 'mchen@email.com', graduationYear: 2019, degree: 'BBA', currentCompany: 'Deloitte', isVerified: true },
        { id: '3', firstName: 'Emily', lastName: 'Davis', email: 'emily.d@email.com', graduationYear: 2021, degree: 'MBA', currentCompany: 'Amazon', isVerified: false },
        { id: '4', firstName: 'James', lastName: 'Wilson', email: 'jwilson@email.com', graduationYear: 2018, degree: 'B.Tech ME', currentCompany: 'Tesla', isVerified: true },
        { id: '5', firstName: 'Lisa', lastName: 'Anderson', email: 'landerson@email.com', graduationYear: 2022, degree: 'B.Sc', currentCompany: null, isVerified: false }
      ];
      this.isLoading = false;
    }, 500);
  }
}
