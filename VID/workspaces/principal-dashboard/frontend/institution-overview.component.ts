import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-institution-overview',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './institution-overview.component.html',
  styleUrls: ['./institution-overview.component.css']
})
export class InstitutionOverviewComponent implements OnInit {
  overview = {
    institution_name: 'VID Institute of Technology',
    established_year: 2005,
    accreditation_status: 'NAAC A Grade',
    total_campuses: 2,
    total_buildings: 5,
    total_labs: 25,
    total_libraries: 3,
    total_hostels: 4
  };

  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => { this.isLoading = false; }, 800);
  }
}
