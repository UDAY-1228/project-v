import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/sports-officer/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/sports-officer/dashboard" },
        { "label": "Sports Events", "icon": "emoji_events", "path": "/sports-officer/sports-events" },
        { "label": "Team Management", "icon": "groups", "path": "/sports-officer/team-management" },
        { "label": "Player Registrations", "icon": "how_to_reg", "path": "/sports-officer/player-registrations" },
        { "label": "Practice Schedules", "icon": "schedule", "path": "/sports-officer/practice-schedules" },
        { "label": "Tournament Management", "icon": "emoji_events", "path": "/sports-officer/tournament-management" },
        { "label": "Performance Tracking", "icon": "trending_up", "path": "/sports-officer/performance-tracking" },
        { "label": "Reports", "icon": "analytics", "path": "/sports-officer/reports" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
