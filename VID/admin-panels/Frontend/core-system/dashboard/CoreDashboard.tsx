import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface UserProfile {
  role: string;
  email: string;
}

interface Workspace {
  name: string;
  description: string;
}

const CoreDashboard: React.FC = () => {
  const navigate = useNavigate();
  const [userProfile] = useState<UserProfile>({
    role: 'Student',
    email: 'user@example.com'
  });
  const [accessList] = useState<Workspace[]>([
    { name: 'Computer Science Dept', description: 'Access to department-specific resources.' },
    { name: 'Student Library Portal', description: 'Search and reserve books.' }
  ]);

  const logout = () => {
    console.log('Logging out of Core System...');
    navigate('/login');
  };

  return (
    <div className="core-dashboard-layout">
      <aside className="sidebar">
        <div className="logo">VID Core System</div>
        <nav>
          <a href="/dashboard">Dashboard</a>
          <a href="/notices">Notice Board</a>
          <a href="/timetable">Timetable</a>
          <a href="/access-panel">User Access Panel</a>
          <a href="/settings">Basic Settings</a>
          <button onClick={logout}>Logout</button>
        </nav>
      </aside>

      <main className="content">
        <header>
          <h1>Dashboard</h1>
        </header>

        <div className="user-overview">
          <div className="card">
            <h3>User Overview</h3>
            <p>User Role: {userProfile.role}</p>
            <p>Email: {userProfile.email}</p>
          </div>
          <div className="card">
            <h3>Quick Access</h3>
            <ul>
              <li><a href="/notices">Notifications</a></li>
              <li><a href="/timetable">Schedule</a></li>
            </ul>
          </div>
        </div>

        <section className="workspace-access">
          <h2>Workspace Access</h2>
          {accessList.map((space, idx) => (
            <div key={idx} className="workspace-card">
              <h3>{space.name}</h3>
              <p>{space.description}</p>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
};

export default CoreDashboard;
