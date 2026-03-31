import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  settings = {
    wake_word: 'hey assistant',
    language: 'en-US',
    voice_id: 'default',
    speech_to_text_model: 'base',
    text_to_speech_enabled: true,
    noise_cancellation: true,
    ambient_noise_adjustment: true,
    conversation_timeout_seconds: 300,
    max_conversation_duration_minutes: 30,
    ai_provider: 'openai',
    ai_model: 'gpt-4',
    context_retention_messages: 10,
    sentiment_analysis_enabled: true,
    logging_level: 'info'
  };
  isLoading = false;

  ngOnInit(): void {}

  saveSettings() {
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      alert('Settings saved successfully!');
    }, 800);
  }

  testVoice() {
    alert('Voice test feature - Coming soon!');
  }
}
