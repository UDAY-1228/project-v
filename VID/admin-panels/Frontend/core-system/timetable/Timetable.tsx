import React from 'react';

interface TimetableEntry {
  id: string;
  subject: string;
  time: string;
  room: string;
}

const Timetable: React.FC = () => {
  const [entries] = useState<TimetableEntry[]>([
    { id: '1', subject: 'Mathematics', time: '09:00 AM', room: 'Room 101' },
    { id: '2', subject: 'Physics', time: '10:00 AM', room: 'Room 102' }
  ]);

  return (
    <div className="timetable-page">
      <h1>Timetable</h1>
      <table>
        <thead>
          <tr><th>Subject</th><th>Time</th><th>Room</th></tr>
        </thead>
        <tbody>
          {entries.map((entry) => (
            <tr key={entry.id}>
              <td>{entry.subject}</td>
              <td>{entry.time}</td>
              <td>{entry.room}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Timetable;
