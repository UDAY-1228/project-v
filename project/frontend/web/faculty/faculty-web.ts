/**
 * Faculty (Teacher Admin) Web Components
 * This is a TypeScript file (not Angular) as requested.
 */

export interface ClassSchedule {
  class: string;
  section: string;
  subject: string;
  period: number;
  time: string;
}

export interface StudentAtRisk {
  name: string;
  id: string;
  reason: string;
  score: number;
}

export class Faculty {
  constructor(private facultyId: string, private name: string) {}

  public getTodayClasses(): ClassSchedule[] {
    return [
      { class: 'Class 10', section: 'A', subject: 'Mathematics', period: 1, time: '08:30 AM' },
      { class: 'Class 9', section: 'B', subject: 'Physics', period: 2, time: '09:30 AM' },
      { class: 'Class 10', section: 'A', subject: 'Mathematics', period: 4, time: '11:45 AM' }
    ];
  }

  public getAtRiskStudents(): StudentAtRisk[] {
    return [
      { name: 'Nivas Kumar', id: 'STUD-001', reason: 'Attendance < 75%', score: 68 },
      { name: 'Anjali Rani', id: 'STUD-042', reason: 'Declining academic trend', score: 72 }
    ];
  }
}
