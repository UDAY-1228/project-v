import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-publications',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './publications.component.html',
  styleUrls: ['./publications.component.css']
})
export class PublicationsComponent implements OnInit {
  publications: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.publications = [
        { id: '1', title: 'Deep Learning for Medical Imaging', authors: 'Kumar et al.', journal: 'IEEE Access', impact_factor: 3.2, citations: 45, type: 'journal' },
        { id: '2', title: 'Smart Grid Optimization', authors: 'Sharma et al.', journal: 'Elsevier Energy', impact_factor: 8.1, citations: 120, type: 'journal' }
      ];
      this.isLoading = false;
    }, 800);
  }
}
