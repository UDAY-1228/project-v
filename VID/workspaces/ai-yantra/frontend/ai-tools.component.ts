import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface AITool {
  id: string;
  name: string;
  description: string;
  category: string;
  status: string;
}

@Component({
  selector: 'app-ai-tools',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './ai-tools.component.html',
  styleUrls: ['./ai-tools.component.css']
})
export class AIToolsComponent implements OnInit {
  tools: AITool[] = [];
  isLoading = true;
  searchQuery = '';
  selectedCategory = 'all';

  categories = ['all', 'text', 'image', 'audio', 'code', 'analysis'];

  ngOnInit(): void {
    setTimeout(() => {
      this.tools = [
        { id: '1', name: 'GPT-4 Turbo', description: 'Advanced text generation model', category: 'text', status: 'active' },
        { id: '2', name: 'Claude 3', description: 'Conversational AI assistant', category: 'text', status: 'active' },
        { id: '3', name: 'DALL-E 3', description: 'Image generation from text', category: 'image', status: 'inactive' },
        { id: '4', name: 'Whisper', description: 'Speech recognition model', category: 'audio', status: 'active' },
        { id: '5', name: 'CodeLlama', description: 'Code generation and completion', category: 'code', status: 'active' },
        { id: '6', name: 'Sentiment Analyzer', description: 'Text sentiment analysis', category: 'analysis', status: 'active' }
      ];
      this.isLoading = false;
    }, 800);
  }

  get filteredTools(): AITool[] {
    return this.tools.filter(tool => {
      const matchesSearch = tool.name.toLowerCase().includes(this.searchQuery.toLowerCase()) || tool.description.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesCategory = this.selectedCategory === 'all' || tool.category === this.selectedCategory;
      return matchesSearch && matchesCategory;
    });
  }

  toggleTool(tool: AITool): void {
    tool.status = tool.status === 'active' ? 'inactive' : 'active';
  }

  deployTool(tool: AITool): void {
    alert(`Deploying ${tool.name}...`);
  }
}
