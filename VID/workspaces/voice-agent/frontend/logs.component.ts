import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-logs',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {
  logs: any[] = [];
  filteredLogs: any[] = [];
  isLoading = true;
  searchTerm = '';
  selectedLevel = 'all';
  selectedType = 'all';

  ngOnInit(): void {
    this.loadLogs();
  }

  loadLogs() {
    setTimeout(() => {
      this.logs = [
        { id: '1', log_type: 'system', level: 'info', source: 'voice-engine', message: 'Voice recognition activated', timestamp: new Date() },
        { id: '2', log_type: 'command', level: 'info', source: 'command-parser', message: 'Command executed: check attendance', timestamp: new Date() },
        { id: '3', log_type: 'error', level: 'error', source: 'speech-api', message: 'Failed to process audio input', timestamp: new Date() },
        { id: '4', log_type: 'conversation', level: 'info', source: 'ai-engine', message: 'New conversation started', timestamp: new Date() },
        { id: '5', log_type: 'system', level: 'warning', source: 'voice-engine', message: 'High latency detected: 500ms', timestamp: new Date() },
        { id: '6', log_type: 'command', level: 'info', source: 'command-parser', message: 'Command executed: view grades', timestamp: new Date() }
      ];
      this.filterLogs();
      this.isLoading = false;
    }, 600);
  }

  filterLogs() {
    let filtered = this.logs;
    if (this.searchTerm) {
      filtered = filtered.filter(l => l.message.toLowerCase().includes(this.searchTerm.toLowerCase()));
    }
    if (this.selectedLevel !== 'all') {
      filtered = filtered.filter(l => l.level === this.selectedLevel);
    }
    if (this.selectedType !== 'all') {
      filtered = filtered.filter(l => l.log_type === this.selectedType);
    }
    this.filteredLogs = filtered;
  }

  getLevelColor(level: string): string {
    const colors: any = { info: 'bg-blue-500/20 text-blue-400', warning: 'bg-amber-500/20 text-amber-400', error: 'bg-rose-500/20 text-rose-400' };
    return colors[level] || colors.info;
  }
}
