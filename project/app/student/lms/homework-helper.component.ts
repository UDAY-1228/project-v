import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { Store } from '@ngxs/store';
import { AuthState } from '../../../../core/state/auth.state';

@Component({
  selector: 'eims-homework-helper',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  template: `
    <div class="hw-helper-page stagger-children">
      <!-- Header -->
      <div class="hw-header">
        <div>
          <h1 class="page-title-text">🤖 AI Homework Helper</h1>
          <p class="page-subtitle">Get instant hints and step-by-step explanations for any subject</p>
        </div>
        <div class="ai-badge">
          <span class="ai-dot"></span>
          <span>AI Powered</span>
        </div>
      </div>

      <div class="hw-layout">
        <!-- Chat interface -->
        <div class="chat-panel card-glass">
          <div class="chat-header">
            <div class="chat-bot-icon">🤖</div>
            <div>
              <div class="chat-bot-name">EIMS AI Tutor</div>
              <div class="chat-bot-sub">Supports Telugu & English</div>
            </div>
            <div class="online-dot"></div>
          </div>

          <div class="chat-messages" #chatMessages id="chat-messages">
            <div class="message bot-msg" *ngFor="let m of messages" [class.user-msg]="m.role === 'user'">
              <div class="msg-avatar" *ngIf="m.role === 'bot'">🤖</div>
              <div class="msg-content">
                <div class="msg-text" [innerHTML]="m.text"></div>
                <div class="msg-time">{{ m.time }}</div>
              </div>
              <div class="msg-avatar" *ngIf="m.role === 'user'">👤</div>
            </div>
            <!-- Loading indicator -->
            <div class="message bot-msg" *ngIf="loading">
              <div class="msg-avatar">🤖</div>
              <div class="msg-content">
                <div class="typing-indicator"><span></span><span></span><span></span></div>
              </div>
            </div>
          </div>

          <form [formGroup]="chatForm" (ngSubmit)="askQuestion()" class="chat-input-area">
            <div class="subject-pills">
              <button
                type="button"
                class="subject-pill"
                *ngFor="let s of subjects"
                [class.active]="selectedSubject === s.value"
                (click)="selectedSubject = s.value"
              >{{ s.icon }} {{ s.label }}</button>
            </div>
            <div class="chat-input-wrapper">
              <textarea
                id="question-input"
                formControlName="question"
                placeholder="Type your question in English or Telugu... (e.g., 'How to solve quadratic equations?')"
                class="form-control-dark chat-textarea"
                rows="2"
                (keydown.enter)="$event.preventDefault(); askQuestion()"
              ></textarea>
              <button type="submit" class="btn-primary-glow send-btn" id="btn-send-question" [disabled]="loading || !chatForm.valid">
                <span *ngIf="!loading">Send ↑</span>
                <span *ngIf="loading">...</span>
              </button>
            </div>
          </form>
        </div>

        <!-- Right panel -->
        <div class="right-panel">
          <!-- Practice questions -->
          <div class="card-glass">
            <h3 class="section-title">📚 Practice Questions</h3>
            <div class="practice-selector">
              <select id="practice-subject" class="form-control-dark" [(ngModel)]="practiceSubject">
                <option value="math">Mathematics</option>
                <option value="science">Science</option>
                <option value="english">English</option>
                <option value="telugu">Telugu</option>
              </select>
              <input id="practice-topic" type="text" class="form-control-dark" placeholder="Topic (e.g. fractions)" [(ngModel)]="practiceTopic">
              <button class="btn-primary-glow" id="btn-generate-practice" (click)="generatePractice()" style="width:100%;justify-content:center">Generate ✨</button>
            </div>
            <div class="practice-list" *ngIf="practiceQuestions.length > 0">
              <div class="practice-item" *ngFor="let q of practiceQuestions; let i = index">
                <div class="q-num">Q{{ i + 1 }}</div>
                <div class="q-content">
                  <div class="q-text">{{ q.q }}</div>
                  <div class="q-marks">{{ q.marks }} marks</div>
                  <button class="reveal-btn" (click)="q.showAnswer = !q.showAnswer" id="btn-reveal-{{i}}">
                    {{ q.showAnswer ? 'Hide' : 'Show' }} Answer
                  </button>
                  <div class="q-answer" *ngIf="q.showAnswer">✅ {{ q.a }}</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Quick topics -->
          <div class="card-glass">
            <h3 class="section-title">⚡ Quick Topics</h3>
            <div class="topic-grid">
              <button
                class="topic-btn"
                *ngFor="let t of quickTopics"
                (click)="quickAsk(t)"
                [id]="'topic-' + t.id"
              >
                <span class="topic-icon">{{ t.icon }}</span>
                <span class="topic-text">{{ t.label }}</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .hw-helper-page { max-width:1200px; }
    .hw-header { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem; }
    .page-title-text { font-size:1.75rem; font-weight:800; color:var(--text-primary); }
    .page-subtitle { color:var(--text-muted); font-size:0.9rem; }
    .ai-badge { display:flex; align-items:center; gap:0.5rem; background:rgba(79,70,229,0.15); border:1px solid rgba(79,70,229,0.3); border-radius:999px; padding:0.5rem 1rem; font-size:0.85rem; color:var(--primary-light); font-weight:600; }
    .ai-dot { width:8px; height:8px; background:#10b981; border-radius:50%; animation:pulse 1.5s infinite; }
    .hw-layout { display:grid; grid-template-columns:1fr 360px; gap:1.5rem; }
    @media (max-width:992px) { .hw-layout { grid-template-columns:1fr; } }
    .chat-panel { display:flex; flex-direction:column; height:600px; overflow:hidden; }
    .chat-header { display:flex; align-items:center; gap:0.75rem; padding-bottom:1rem; border-bottom:1px solid var(--border-color); margin-bottom:0.5rem; }
    .chat-bot-icon { font-size:2rem; }
    .chat-bot-name { font-weight:700; color:var(--text-primary); }
    .chat-bot-sub { font-size:0.75rem; color:var(--text-muted); }
    .online-dot { width:10px; height:10px; background:#10b981; border-radius:50%; margin-left:auto; }
    .chat-messages { flex:1; overflow-y:auto; display:flex; flex-direction:column; gap:1rem; padding:0.5rem 0; }
    .message { display:flex; gap:0.75rem; align-items:flex-start; }
    .user-msg { flex-direction:row-reverse; }
    .msg-avatar { font-size:1.5rem; flex-shrink:0; }
    .msg-content { max-width:80%; }
    .msg-text { background:var(--bg-input); border-radius:var(--border-radius); padding:0.875rem; font-size:0.875rem; color:var(--text-primary); line-height:1.6; }
    .user-msg .msg-text { background:rgba(79,70,229,0.2); border:1px solid rgba(79,70,229,0.3); }
    .msg-time { font-size:0.7rem; color:var(--text-muted); margin-top:0.25rem; }
    .user-msg .msg-time { text-align:right; }
    .typing-indicator { display:flex; gap:0.375rem; padding:1rem; }
    .typing-indicator span { width:8px; height:8px; background:var(--primary); border-radius:50%; animation:bounce 0.6s infinite alternate; }
    .typing-indicator span:nth-child(2) { animation-delay:0.2s; }
    .typing-indicator span:nth-child(3) { animation-delay:0.4s; }
    @keyframes bounce { from{transform:translateY(0);} to{transform:translateY(-8px);} }
    .chat-input-area { border-top:1px solid var(--border-color); padding-top:1rem; }
    .subject-pills { display:flex; flex-wrap:wrap; gap:0.375rem; margin-bottom:0.75rem; }
    .subject-pill { background:var(--bg-input); border:1px solid var(--border-color); border-radius:999px; padding:0.25rem 0.75rem; font-size:0.75rem; color:var(--text-secondary); cursor:pointer; transition:var(--transition-fast); }
    .subject-pill.active { background:rgba(79,70,229,0.2); border-color:var(--primary); color:var(--primary-light); }
    .chat-input-wrapper { display:flex; gap:0.75rem; align-items:flex-end; }
    .chat-textarea { flex:1; resize:none; }
    .send-btn { flex-shrink:0; height:fit-content; }
    .right-panel { display:flex; flex-direction:column; gap:1rem; }
    .section-title { font-size:1rem; font-weight:700; color:var(--text-primary); margin-bottom:1rem; }
    .practice-selector { display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1rem; }
    .practice-list { display:flex; flex-direction:column; gap:0.75rem; max-height:250px; overflow-y:auto; }
    .practice-item { display:flex; gap:0.75rem; align-items:flex-start; padding:0.75rem; background:var(--bg-input); border-radius:var(--border-radius); }
    .q-num { font-weight:800; color:var(--primary-light); min-width:24px; }
    .q-content { flex:1; }
    .q-text { font-size:0.85rem; color:var(--text-primary); margin-bottom:0.25rem; }
    .q-marks { font-size:0.7rem; color:var(--text-muted); margin-bottom:0.5rem; }
    .reveal-btn { background:none; border:1px solid var(--border-color); border-radius:999px; padding:0.2rem 0.5rem; font-size:0.7rem; color:var(--text-secondary); cursor:pointer; }
    .q-answer { background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); color:#10b981; padding:0.5rem; border-radius:var(--border-radius); font-size:0.8rem; margin-top:0.5rem; }
    .topic-grid { display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; }
    .topic-btn { display:flex; align-items:center; gap:0.375rem; padding:0.625rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--border-radius); cursor:pointer; transition:var(--transition-fast); color:var(--text-secondary); font-size:0.8rem; }
    .topic-btn:hover { background:rgba(79,70,229,0.1); border-color:var(--primary); color:var(--primary-light); }
    .topic-icon { font-size:1.1rem; }
  `]
})
export class HomeworkHelperComponent implements OnInit {
  chatForm!: FormGroup;
  loading = false;
  selectedSubject = 'math';
  practiceSubject = 'math';
  practiceTopic = '';
  practiceQuestions: any[] = [];

  messages: { role: string; text: string; time: string }[] = [
    {
      role: 'bot',
      text: '🎓 <strong>Namaste! నమస్కారం!</strong><br><br>I\'m your EIMS AI Tutor. I can help you with:<br>• Mathematics, Science, English, Telugu<br>• Step-by-step explanations<br>• Practice questions<br><br>What would you like to learn today?',
      time: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' }),
    }
  ];

  subjects = [
    { label: 'Math', value: 'math', icon: '🔢' },
    { label: 'Science', value: 'science', icon: '🔬' },
    { label: 'English', value: 'english', icon: '📖' },
    { label: 'Telugu', value: 'telugu', icon: '🔤' },
    { label: 'Social', value: 'social', icon: '🌍' },
  ];

  quickTopics = [
    { id: 'quadratic', icon: '📐', label: 'Quadratic Equations' },
    { id: 'photosynthesis', icon: '🌿', label: 'Photosynthesis' },
    { id: 'grammar', icon: '✍️', label: 'English Grammar' },
    { id: 'fractions', icon: '½', label: 'Fractions' },
    { id: 'newton', icon: '🍎', label: "Newton's Laws" },
    { id: 'telugu-padyalu', icon: '📜', label: 'Telugu Padyalu' },
  ];

  private aiResponses: Record<string, string> = {
    'quadratic': '📐 <strong>Quadratic Equations</strong><br><br>Standard form: <code>ax² + bx + c = 0</code><br><br>Use the <strong>Quadratic Formula</strong>:<br><code>x = (-b ± √(b²-4ac)) / 2a</code><br><br><strong>Step-by-step for x² - 5x + 6 = 0:</strong><br>1. a=1, b=-5, c=6<br>2. Discriminant = 25-24 = 1<br>3. x = (5 ± 1) / 2<br>4. x = 3 or x = 2 ✅',
    'photosynthesis': '🌿 <strong>Photosynthesis</strong><br><br><strong>Equation:</strong><br>6CO₂ + 6H₂O + (sunlight) → C₆H₁₂O₆ + 6O₂<br><br><strong>Key points:</strong><br>• Occurs in chloroplasts<br>• Chlorophyll absorbs sunlight<br>• Produces glucose (food) + oxygen<br>• Light reaction + Calvin cycle',
    'fractions': '½ <strong>Fractions Guide</strong><br><br><strong>Adding:</strong> 1/2 + 1/3 = 3/6 + 2/6 = <strong>5/6</strong><br><strong>Multiplying:</strong> 2/3 × 3/4 = <strong>6/12 = 1/2</strong><br><strong>Dividing:</strong> 1/2 ÷ 1/4 = 1/2 × 4/1 = <strong>2</strong><br><br>💡 Always simplify your answer!',
  };

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.chatForm = this.fb.group({ question: [''] });
  }

  async askQuestion(): Promise<void> {
    const q = this.chatForm.get('question')?.value?.trim();
    if (!q) return;

    const time = new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
    this.messages.push({ role: 'user', text: q, time });
    this.chatForm.reset();
    this.loading = true;

    // Simulate AI response (in production: call backend /lms/homework-helper)
    await new Promise(r => setTimeout(r, 1500));

    const lowerQ = q.toLowerCase();
    let response = '🤔 Good question! ';

    if (lowerQ.includes('quadratic') || lowerQ.includes('equation')) {
      response = this.aiResponses['quadratic'];
    } else if (lowerQ.includes('photosynthesis') || lowerQ.includes('plant')) {
      response = this.aiResponses['photosynthesis'];
    } else if (lowerQ.includes('fraction')) {
      response = this.aiResponses['fractions'];
    } else if (lowerQ.includes('help') || lowerQ.includes('hello') || lowerQ.includes('hi')) {
      response = '👋 Hello! I\'m here to help with your studies. Ask me any question from your textbook — Math, Science, English, or Telugu!';
    } else {
      response = `I understand you\'re asking about: <strong>"${q}"</strong><br><br>💡 <strong>Hint:</strong> Let me break this down step by step:<br>1. First, identify what type of problem this is<br>2. Look for the key formula or rule in your textbook<br>3. Apply it systematically<br><br>🔍 Try to relate it to examples from your textbook. Which subject is this for? (${this.selectedSubject})`;
    }

    this.messages.push({ role: 'bot', text: response, time: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' }) });
    this.loading = false;
  }

  quickAsk(topic: { id: string; label: string }): void {
    this.chatForm.patchValue({ question: `Explain ${topic.label} with examples` });
    this.askQuestion();
  }

  generatePractice(): void {
    this.practiceQuestions = [
      { q: `Practice Q1: ${this.practiceSubject} — ${this.practiceTopic || 'General question'}`, a: 'See your textbook page 42', marks: 3, showAnswer: false },
      { q: `Practice Q2: Solve: 3x + 5 = 14`, a: 'x = 3', marks: 2, showAnswer: false },
      { q: `Practice Q3: Find the area of a rectangle with l=8cm, b=5cm`, a: '40 cm²', marks: 3, showAnswer: false },
      { q: `Practice Q4: What is 25% of 160?`, a: '40', marks: 2, showAnswer: false },
      { q: `Practice Q5: Simplify 18/24`, a: '3/4', marks: 2, showAnswer: false },
    ];
  }
}
