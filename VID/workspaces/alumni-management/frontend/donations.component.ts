import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-donations',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './donations.component.html',
  styleUrls: ['./donations.component.css']
})
export class DonationsComponent implements OnInit {
  campaigns = [
    { name: 'Scholarship Fund 2026', raised: 75000, target: 100000, isActive: true },
    { name: 'Building Renovation', raised: 30000, target: 50000, isActive: true },
    { name: 'Lab Equipment', raised: 20000, target: 25000, isActive: false }
  ];

  recentDonations = [
    { donorName: 'Michael Chen', amount: 500, date: new Date('2026-03-15') },
    { donorName: 'Sarah Johnson', amount: 1000, date: new Date('2026-03-14') },
    { donorName: 'Anonymous', amount: 250, date: new Date('2026-03-13') },
    { donorName: 'David Lee', amount: 750, date: new Date('2026-03-12') }
  ];

  ngOnInit(): void {}
}
