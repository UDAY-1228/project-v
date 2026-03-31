import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface TrendingItem {
  label: string;
  value: number;
}

interface Operation {
  type: string;
  user: string;
  timestamp: string;
}

const AdminDashboard: React.FC = () => {
  const navigate = useNavigate();
  const [institutionOverview] = useState({ total_users: 154, active_workspaces: 8 });
  const [trendingAnalytics] = useState<TrendingItem[]>([
    { label: 'Active Users', value: 85 },
    { label: 'Workspace Usage', value: 92 }
  ]);
  const [recentOperations] = useState<Operation[]>([
    { type: 'USER_CREATED', user: 'admin1', timestamp: '2024-03-31T08:00:00Z' },
    { type: 'WORKSPACE_ASSIGNED', user: 'fac_12', timestamp: '2024-03-31T07:45:00Z' }
  ]);

  const logout = () => {
    console.log('Logging out of Admin Panel...');
    navigate('/login');
  };

  return (
    <div className="admin-dashboard-layout">
      <aside className="sidebar">
        <div className="logo">VID Admin Panel</div>
        <nav>
          <a href="/dashboard">Dashboard</a>
          <a href="/users">User Management</a>
          <a href="/operations">Institution Operations</a>
          <a href="/notices">Notice Board</a>
          <a href="/reports">Reports & Analytics</a>
          <a href="/settings">Settings</a>
          <button onClick={logout}>Logout</button>
        </nav>
      </aside>

      <main className="content">
        <header>
          <h1>Admin Dashboard</h1>
        </header>

        <div className="analytics-overview">
          <div className="stat-card">
            <h3>Trending Analytics</h3>
            <ul>
              {trendingAnalytics.map((item, idx) => (
                <li key={idx}>{item.label}: {item.value}%</li>
              ))}
            </ul>
          </div>
          <div className="stat-card">
            <h3>User Activity</h3>
            <p>{institutionOverview.total_users} total users within institution.</p>
          </div>
        </div>

        <section className="recent-ops">
          <h2>Recent Operations</h2>
          <table>
            <thead>
              <tr><th>Operation</th><th>Performed By</th><th>Timestamp</th></tr>
            </thead>
            <tbody>
              {recentOperations.map((op, idx) => (
                <tr key={idx}>
                  <td>{op.type}</td>
                  <td>{op.user}</td>
                  <td>{new Date(op.timestamp).toLocaleString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
};

export default AdminDashboard;
