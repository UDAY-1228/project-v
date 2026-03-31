import React, { useState } from 'react';

interface StatData {
  totalUsers: number;
  activeUsers: number;
  totalInstitutions: number;
  revenue: number;
}

const Statistics: React.FC = () => {
  const [stats] = useState<StatData>({
    totalUsers: 1500,
    activeUsers: 1200,
    totalInstitutions: 25,
    revenue: 150000
  });

  return (
    <div className="statistics-page">
      <h1>Statistics</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Users</h3>
          <p>{stats.totalUsers}</p>
        </div>
        <div className="stat-card">
          <h3>Active Users</h3>
          <p>{stats.activeUsers}</p>
        </div>
        <div className="stat-card">
          <h3>Total Institutions</h3>
          <p>{stats.totalInstitutions}</p>
        </div>
        <div className="stat-card">
          <h3>Revenue</h3>
          <p>${stats.revenue}</p>
        </div>
      </div>
    </div>
  );
};

export default Statistics;
