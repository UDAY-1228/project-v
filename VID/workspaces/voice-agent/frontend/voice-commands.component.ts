import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-voice-commands',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './voice-commands.component.html',
  styleUrls: ['./voice-commands.component.css']
})
export class VoiceCommandsComponent implements OnInit {
  commands: any[] = [];
  filteredCommands: any[] = [];
  isLoading = true;
  searchTerm = '';
  selectedFilter = 'all';
  showModal = false;
  editingCommand: any = null;

  newCommand = {
    command_name: '',
    command_phrase: '',
    description: '',
    intent: '',
    module_target: '',
    access_level: 'user',
    enabled: true
  };

  ngOnInit(): void {
    this.loadCommands();
  }

  loadCommands() {
    setTimeout(() => {
      this.commands = [
        { id: '1', command_name: 'Check Attendance', command_phrase: 'check my attendance', intent: 'query', module_target: 'student', usage_count: 234, success_rate: 96.5, enabled: true },
        { id: '2', command_name: 'View Grades', command_phrase: 'show my grades', intent: 'query', module_target: 'student', usage_count: 189, success_rate: 94.2, enabled: true },
        { id: '3', command_name: 'Fee Status', command_phrase: 'check fee status', intent: 'query', module_target: 'payment', usage_count: 156, success_rate: 91.8, enabled: true },
        { id: '4', command_name: 'Library Books', command_phrase: 'search library books', intent: 'search', module_target: 'library', usage_count: 98, success_rate: 88.5, enabled: true },
        { id: '5', command_name: 'Timetable', command_phrase: 'show my timetable', intent: 'query', module_target: 'timetable', usage_count: 145, success_rate: 92.1, enabled: false },
        { id: '6', command_name: 'Exam Schedule', command_phrase: 'when are exams', intent: 'query', module_target: 'examination', usage_count: 112, success_rate: 89.7, enabled: true }
      ];
      this.filterCommands();
      this.isLoading = false;
    }, 600);
  }

  filterCommands() {
    let filtered = this.commands;
    if (this.searchTerm) {
      filtered = filtered.filter(c => 
        c.command_name.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
        c.command_phrase.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    }
    if (this.selectedFilter !== 'all') {
      filtered = filtered.filter(c => c.enabled === (this.selectedFilter === 'enabled'));
    }
    this.filteredCommands = filtered;
  }

  toggleCommand(command: any) {
    command.enabled = !command.enabled;
    this.filterCommands();
  }

  openModal(command?: any) {
    if (command) {
      this.editingCommand = { ...command };
    } else {
      this.editingCommand = null;
      this.newCommand = {
        command_name: '',
        command_phrase: '',
        description: '',
        intent: '',
        module_target: '',
        access_level: 'user',
        enabled: true
      };
    }
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
    this.editingCommand = null;
  }

  saveCommand() {
    if (this.editingCommand) {
      const index = this.commands.findIndex(c => c.id === this.editingCommand.id);
      if (index !== -1) {
        this.commands[index] = { ...this.editingCommand };
      }
    } else {
      const newId = (Math.max(...this.commands.map(c => parseInt(c.id))) + 1).toString();
      this.commands.push({ ...this.newCommand, id: newId, usage_count: 0, success_rate: 0 });
    }
    this.filterCommands();
    this.closeModal();
  }

  deleteCommand(id: string) {
    this.commands = this.commands.filter(c => c.id !== id);
    this.filterCommands();
  }
}
