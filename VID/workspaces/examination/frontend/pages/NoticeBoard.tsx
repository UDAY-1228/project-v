import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/examination/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/examination/dashboard" },
        { "label": "Results", "icon": "score", "path": "/examination/results" },
        { "label": "Previous Exams", "icon": "history", "path": "/examination/previous-exams" },
        { "label": "Tests", "icon": "quiz", "path": "/examination/tests" },
        { "label": "Previous Year Papers", "icon": "library_books", "path": "/examination/previous-year-papers" },
        { "label": "Averages", "icon": "functions", "path": "/examination/averages" },
        { "label": "Class Toppers", "icon": "emoji_events", "path": "/examination/class-toppers" },
        { "label": "Reports", "icon": "analytics", "path": "/examination/reports" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
