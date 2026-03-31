import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-assignments',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './assignments.component.html',
  styleUrls: ['./assignments.component.css']
})
export class AssignmentsComponent implements OnInit {
  assignments: any[] = [];
  filteredAssignments: any[] = [];
  selectedStatus: string = 'all';
  searchQuery: string = '';
  isLoading = true;
  showCreateModal = false;
  showSubmissionsModal = false;
  selectedAssignment: any = null;
  submissions: any[] = [];

  newAssignment = {
    title: '',
    description: '',
    subject_name: 'Data Structures',
    total_marks: 100,
    passing_marks: 40,
    due_date: '',
    instructions: ''
  };

  ngOnInit(): void {
    this.fetchAssignments();
  }

  fetchAssignments() {
    setTimeout(() => {
      this.assignments = [
        { id: '1', title: 'Database Design Project', subject_name: 'Database Systems', total_marks: 100, passing_marks: 40, due_date: '2026-04-15', posted_date: '2026-03-20', total_submissions: 35, status: 'active' },
        { id: '2', title: 'Sorting Algorithms Implementation', subject_name: 'Data Structures', total_marks: 50, passing_marks: 20, due_date: '2026-04-10', posted_date: '2026-03-18', total_submissions: 38, status: 'active' },
        { id: '3', title: 'Network Protocol Analysis', subject_name: 'Computer Networks', total_marks: 75, passing_marks: 30, due_date: '2026-04-05', posted_date: '2026-03-15', total_submissions: 0, status: 'draft' },
        { id: '4', title: 'Operating System Case Study', subject_name: 'Operating Systems', total_marks: 100, passing_marks: 40, due_date: '2026-03-25', posted_date: '2026-03-01', total_submissions: 42, status: 'completed' }
      ];
      this.applyFilters();
      this.isLoading = false;
    }, 800);
  }

  applyFilters() {
    let filtered = [...this.assignments];
    if (this.selectedStatus !== 'all') {
      filtered = filtered.filter(a => a.status === this.selectedStatus);
    }
    if (this.searchQuery) {
      const query = this.searchQuery.toLowerCase();
      filtered = filtered.filter(a => a.title.toLowerCase().includes(query) || a.subject_name.toLowerCase().includes(query));
    }
    this.filteredAssignments = filtered;
  }

  openCreateModal() {
    this.showCreateModal = true;
  }

  closeCreateModal() {
    this.showCreateModal = false;
  }

  createAssignment() {
    const newData = {
      ...this.newAssignment,
      id: Date.now().toString(),
      posted_date: new Date().toISOString().split('T')[0],
      total_submissions: 0,
      status: 'active'
    };
    this.assignments.unshift(newData);
    this.applyFilters();
    this.closeCreateModal();
  }

  viewSubmissions(assignment: any) {
    this.selectedAssignment = assignment;
    this.submissions = [
      { student_id: 'STU001', student_name: 'Amit Kumar', roll_number: 'CS301001', submitted_date: '2026-04-10', marks_obtained: 85, status: 'evaluated' },
      { student_id: 'STU002', student_name: 'Priya Sharma', roll_number: 'CS301002', submitted_date: '2026-04-12', marks_obtained: 78, status: 'evaluated' },
      { student_id: 'STU003', student_name: 'Rahul Verma', roll_number: 'CS301003', submitted_date: '2026-04-14', marks_obtained: null, status: 'pending' },
      { student_id: 'STU004', student_name: 'Sneha Patel', roll_number: 'CS301004', submitted_date: '2026-04-13', marks_obtained: 92, status: 'evaluated' }
    ];
    this.showSubmissionsModal = true;
  }

  closeSubmissionsModal() {
    this.showSubmissionsModal = false;
  }

  deleteAssignment(id: string) {
    if (confirm('Are you sure you want to delete this assignment?')) {
      this.assignments = this.assignments.filter(a => a.id !== id);
      this.applyFilters();
    }
  }

  getStatusColor(status: string) {
    switch(status) {
      case 'active': return 'bg-emerald-500/10 text-emerald-400';
      case 'draft': return 'bg-amber-500/10 text-amber-400';
      case 'completed': return 'bg-blue-500/10 text-blue-400';
      default: return 'bg-zinc-500/10 text-zinc-400';
    }
  }
}
