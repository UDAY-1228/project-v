import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-classes',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './classes.component.html',
  styleUrls: ['./classes.component.css']
})
export class ClassesComponent implements OnInit {
  classes: any[] = [];
  filteredClasses: any[] = [];
  selectedDay: string = 'all';
  searchQuery: string = '';
  isLoading = true;
  showCreateModal = false;

  days = ['all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  newClass = {
    class_name: '',
    subject_id: '',
    subject_name: '',
    course_name: '',
    section: 'A',
    room: '',
    schedule_day: 'Monday',
    start_time: '09:00',
    end_time: '10:00'
  };

  ngOnInit(): void {
    this.fetchClasses();
  }

  fetchClasses() {
    setTimeout(() => {
      this.classes = [
        { id: '1', class_name: 'CS301 - Data Structures', subject_name: 'Data Structures', course_name: 'B.Tech CSE', section: 'A', room: 'C-201', building: 'Block C', schedule_day: 'Monday', start_time: '09:00', end_time: '10:30', total_students: 45, status: 'active' },
        { id: '2', class_name: 'CS302 - Database Systems', subject_name: 'Database Systems', course_name: 'B.Tech CSE', section: 'A', room: 'C-202', building: 'Block C', schedule_day: 'Monday', start_time: '11:00', end_time: '12:30', total_students: 40, status: 'active' },
        { id: '3', class_name: 'CS303 - Algorithms', subject_name: 'Algorithms', course_name: 'B.Tech CSE', section: 'B', room: 'C-203', building: 'Block C', schedule_day: 'Tuesday', start_time: '10:00', end_time: '11:30', total_students: 38, status: 'active' },
        { id: '4', class_name: 'CS304 - Operating Systems', subject_name: 'Operating Systems', course_name: 'B.Tech CSE', section: 'A', room: 'C-201', building: 'Block C', schedule_day: 'Wednesday', start_time: '14:00', end_time: '15:30', total_students: 45, status: 'active' },
        { id: '5', class_name: 'CS305 - Computer Networks', subject_name: 'Computer Networks', course_name: 'B.Tech CSE', section: 'A', room: 'C-204', building: 'Block C', schedule_day: 'Thursday', start_time: '09:00', end_time: '10:30', total_students: 42, status: 'active' },
        { id: '6', class_name: 'CS306 - Software Engineering', subject_name: 'Software Engineering', course_name: 'B.Tech CSE', section: 'B', room: 'C-205', building: 'Block C', schedule_day: 'Friday', start_time: '11:00', end_time: '12:30', total_students: 35, status: 'active' }
      ];
      this.applyFilters();
      this.isLoading = false;
    }, 800);
  }

  applyFilters() {
    let filtered = [...this.classes];
    
    if (this.selectedDay !== 'all') {
      filtered = filtered.filter(c => c.schedule_day === this.selectedDay);
    }
    
    if (this.searchQuery) {
      const query = this.searchQuery.toLowerCase();
      filtered = filtered.filter(c => 
        c.class_name.toLowerCase().includes(query) ||
        c.subject_name.toLowerCase().includes(query) ||
        c.course_name.toLowerCase().includes(query)
      );
    }
    
    this.filteredClasses = filtered;
  }

  onDayChange() {
    this.applyFilters();
  }

  onSearch() {
    this.applyFilters();
  }

  openCreateModal() {
    this.showCreateModal = true;
  }

  closeCreateModal() {
    this.showCreateModal = false;
    this.resetNewClass();
  }

  resetNewClass() {
    this.newClass = {
      class_name: '',
      subject_id: '',
      subject_name: '',
      course_name: '',
      section: 'A',
      room: '',
      schedule_day: 'Monday',
      start_time: '09:00',
      end_time: '10:00'
    };
  }

  createClass() {
    const newClassData = { ...this.newClass, id: Date.now().toString(), total_students: 0, status: 'active' };
    this.classes.push(newClassData);
    this.applyFilters();
    this.closeCreateModal();
  }

  viewClass(classId: string) {
    console.log('View class:', classId);
  }

  editClass(classId: string) {
    console.log('Edit class:', classId);
  }

  deleteClass(classId: string) {
    if (confirm('Are you sure you want to delete this class?')) {
      this.classes = this.classes.filter(c => c.id !== classId);
      this.applyFilters();
    }
  }
}
