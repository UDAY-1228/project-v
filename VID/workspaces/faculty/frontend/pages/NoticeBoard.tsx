import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/faculty/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/faculty/dashboard" },
        { "label": "Activities", "icon": "event", "path": "/faculty/activities" },
        { "label": "My Courses", "icon": "menu_book", "path": "/faculty/my-courses" },
        { "label": "Class Timetable", "icon": "calendar_month", "path": "/faculty/class-timetable" },
        { "label": "My Mentees", "icon": "groups", "path": "/faculty/my-mentees" },
        { "label": "Question Banks", "icon": "quiz", "path": "/faculty/question-banks" },
        { "label": "My Profile", "icon": "person", "path": "/faculty/my-profile" },
        { "label": "Research Scholar", "icon": "science", "path": "/faculty/research-scholar" },
        { "label": "Lms", "icon": "laptop_chromebook", "path": "/faculty/lms" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
