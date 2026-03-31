import React, { useState } from 'react';

interface Notice {
  id: string;
  title: string;
  content: string;
  createdAt: string;
}

const NoticeBoard: React.FC = () => {
  const [notices] = useState<Notice[]>([
    { id: '1', title: 'System Maintenance', content: 'Scheduled for Saturday', createdAt: new Date().toISOString() },
    { id: '2', title: 'New Feature', content: 'Check out our new dashboard', createdAt: new Date().toISOString() }
  ]);

  return (
    <div className="notice-board-page">
      <h1>Notice Board</h1>
      <div className="notices-list">
        {notices.map((notice) => (
          <div key={notice.id} className="notice-card">
            <h3>{notice.title}</h3>
            <p>{notice.content}</p>
            <small>{new Date(notice.createdAt).toLocaleDateString()}</small>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NoticeBoard;
