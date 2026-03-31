import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Model {
  id: string;
  name: string;
  type: string;
  version: string;
  framework: string;
  status: string;
  memory: string;
  uptime: string;
}

@Component({
  selector: 'app-model-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './model-control.component.html',
  styleUrls: ['./model-control.component.css']
})
export class ModelControlComponent implements OnInit {
  models: Model[] = [];
  isLoading = true;

  ngOnInit(): void {
    setTimeout(() => {
      this.models = [
        { id: '1', name: 'GPT-4 Turbo', type: 'text-generation', version: 'v3.5', framework: 'OpenAI', status: 'running', memory: '16GB', uptime: '72h' },
        { id: '2', name: 'Claude 3 Opus', type: 'text-generation', version: 'v2.0', framework: 'Anthropic', status: 'running', memory: '16GB', uptime: '48h' },
        { id: '3', name: 'Stable Diffusion XL', type: 'image-generation', version: 'v1.0', framework: 'Stability AI', status: 'stopped', memory: '8GB', uptime: '0h' },
        { id: '4', name: 'CodeLlama 70B', type: 'code-generation', version: 'v1.0', framework: 'Meta', status: 'running', memory: '32GB', uptime: '120h' }
      ];
      this.isLoading = false;
    }, 800);
  }

  startModel(model: Model): void {
    model.status = 'running';
    model.uptime = '0h';
  }

  stopModel(model: Model): void {
    model.status = 'stopped';
    model.uptime = '0h';
  }

  restartModel(model: Model): void {
    model.status = 'stopped';
    setTimeout(() => {
      model.status = 'running';
      model.uptime = '0h';
    }, 2000);
  }
}
