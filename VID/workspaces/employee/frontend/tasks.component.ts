import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employee-tasks',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {
  tasks: any[] = [];
  isLoading = true;

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    setTimeout(() => {
      this.tasks = [
        { id: '1', title: 'Complete project report', priority: 'high', status: 'pending', dueDate: new Date(), category: 'Work' },
        { id: '2', title: 'Team meeting notes', priority: 'medium', status: 'in-progress', dueDate: new Date(), category: 'Admin' },
        { id: '3', title: 'Update documentation', priority: 'low', status: 'completed', dueDate: new Date(), category: 'Work' },
      ];
      this.isLoading = false;
    }, 800);
  }

  getPriorityClass(priority: string): string {
    const classes: any = { high: 'bg-red-500', medium: 'bg-yellow-500', low: 'bg-blue-500' };
    return classes[priority] || 'bg-zinc-500';
  }

  getStatusClass(status: string): string {
    const classes: any = { pending: 'text-yellow-400', 'in-progress': 'text-blue-400', completed: 'text-emerald-400' };
    return classes[status] || 'text-zinc-400';
  }
}
