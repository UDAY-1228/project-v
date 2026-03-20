import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/sports-and-co-curricular/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/sports-and-co-curricular/dashboard" },
        { "label": "Activities List", "icon": "list_alt", "path": "/sports-and-co-curricular/activities-list" },
        { "label": "Event Calendar", "icon": "event", "path": "/sports-and-co-curricular/event-calendar" },
        { "label": "Student Participation", "icon": "groups", "path": "/sports-and-co-curricular/student-participation" },
        { "label": "Achievements", "icon": "emoji_events", "path": "/sports-and-co-curricular/achievements" },
        { "label": "Certificates", "icon": "workspace_premium", "path": "/sports-and-co-curricular/certificates" },
        { "label": "Clubs Management", "icon": "category", "path": "/sports-and-co-curricular/clubs-management" },
        { "label": "Announcements", "icon": "campaign", "path": "/sports-and-co-curricular/announcements" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
