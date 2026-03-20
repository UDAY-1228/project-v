import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/course-coordinator/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/course-coordinator/dashboard" },
        { "label": "All Courses", "icon": "library_books", "path": "/course-coordinator/all-courses" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
