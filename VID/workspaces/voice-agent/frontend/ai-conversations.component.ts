import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-ai-conversations',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ai-conversations.component.html',
  styleUrls: ['./ai-conversations.component.css']
})
export class AiConversationsComponent implements OnInit {
  conversations: any[] = [];
  selectedConversation: any = null;
  messages: any[] = [];
  isLoading = true;
  newMessage = '';
  isRecording = false;

  ngOnInit(): void {
    this.loadConversations();
  }

  loadConversations() {
    setTimeout(() => {
      this.conversations = [
        { id: '1', session_id: 'sess_001', user_name: 'John Doe', message_count: 12, duration_seconds: 340, sentiment_score: 0.85, status: 'active', last_message: 'Show my attendance', created_at: new Date() },
        { id: '2', session_id: 'sess_002', user_name: 'Jane Smith', message_count: 8, duration_seconds: 180, sentiment_score: 0.92, status: 'completed', last_message: 'Check fee status', created_at: new Date() },
        { id: '3', session_id: 'sess_003', user_name: 'Bob Wilson', message_count: 5, duration_seconds: 90, sentiment_score: 0.78, status: 'active', last_message: 'Library books', created_at: new Date() },
        { id: '4', session_id: 'sess_004', user_name: 'Alice Brown', message_count: 15, duration_seconds: 420, sentiment_score: 0.88, status: 'completed', last_message: 'Exam schedule', created_at: new Date() }
      ];
      this.isLoading = false;
    }, 600);
  }

  selectConversation(conv: any) {
    this.selectedConversation = conv;
    this.messages = [
      { role: 'user', content: 'Hello, I need help with my attendance', timestamp: new Date() },
      { role: 'assistant', content: 'Hello! I can help you check your attendance. What would you like to know?', timestamp: new Date() },
      { role: 'user', content: conv.last_message, timestamp: new Date() },
      { role: 'assistant', content: 'Processing your request...', timestamp: new Date() }
    ];
  }

  sendMessage() {
    if (!this.newMessage.trim()) return;
    this.messages.push({ role: 'user', content: this.newMessage, timestamp: new Date() });
    this.messages.push({ role: 'assistant', content: 'Processing your request...', timestamp: new Date() });
    this.newMessage = '';
  }

  toggleRecording() {
    this.isRecording = !this.isRecording;
  }
}
