import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface Stats {
  institutions: number;
  active_users: number;
  system_monitoring: string;
  recent_registrations: number;
}

const SuperAdminDashboard: React.FC = () => {
  const navigate = useNavigate();
  const [stats] = useState<Stats>({
    institutions: 12,
    active_users: 1450,
    system_monitoring: 'Healthy',
    recent_registrations: 5
  });
  const [totalInstitutions] = useState(12);
  const [activeInstitutions] = useState(10);
  const [inactiveInstitutions] = useState(2);
  const [totalRevenue] = useState(50000);

  const logout = () => {
    console.log('Logging out of Super Admin...');
    navigate('/login');
  };

  return (
    <div className="super-admin-layout">
      <aside className="sidebar">
        <div className="logo">VID Super Admin</div>
        <nav>
          <a href="/dashboard">Dashboard</a>
          <a href="/institutions">Institution Management</a>
          <a href="/statistics">Statistics</a>
          <a href="/terms-policies">Terms & Policies</a>
          <a href="/monitoring">Monitoring</a>
          <a href="/profile">Profile</a>
          <button onClick={logout}>Logout</button>
        </nav>
      </aside>

      <main className="content">
        <header>
          <h1>Dashboard</h1>
        </header>

        <div className="stats-overview">
          <div className="stat-card">
            <h3>Total Institutions</h3>
            <p>{totalInstitutions}</p>
          </div>
          <div className="stat-card">
            <h3>Active Institutions</h3>
            <p>{activeInstitutions}</p>
          </div>
          <div className="stat-card">
            <h3>Inactive Institutions</h3>
            <p>{inactiveInstitutions}</p>
          </div>
          <div className="stat-card">
            <h3>Total Revenue</h3>
            <p>${totalRevenue}</p>
          </div>
        </div>

        <section className="usage-overview">
          <h2>System Usage Overview</h2>
        </section>
      </main>
    </div>
  );
};

export default SuperAdminDashboard;
