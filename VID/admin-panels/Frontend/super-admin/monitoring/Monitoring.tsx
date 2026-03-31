import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

interface LogEntry {
  id: string;
  level: string;
  message: string;
  timestamp: string;
}

const Monitoring: React.FC = () => {
  const navigate = useNavigate();
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [systemStatus, setSystemStatus] = useState('Healthy');

  useEffect(() => {
    setLogs([
      { id: '1', level: 'INFO', message: 'System started', timestamp: new Date().toISOString() },
      { id: '2', level: 'INFO', message: 'Database connected', timestamp: new Date().toISOString() }
    ]);
  }, []);

  return (
    <div className="monitoring-page">
      <h1>System Monitoring</h1>
      <div className="status-card">
        <h3>System Status</h3>
        <p>{systemStatus}</p>
      </div>
      <div className="logs-section">
        <h3>System Logs</h3>
        <ul>
          {logs.map((log) => (
            <li key={log.id}>
              <span>[{log.level}]</span> {log.message} - {new Date(log.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Monitoring;
