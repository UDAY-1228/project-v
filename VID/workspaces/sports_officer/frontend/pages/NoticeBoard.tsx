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
        { "label": "Reports", "icon": "analytics", "path": "/sports-officer/reports" },
        { "label": "Activities List", "icon": "list_alt", "path": "/sports-officer/activities-list" },
        { "label": "Event Calendar", "icon": "event", "path": "/sports-officer/event-calendar" },
        { "label": "Student Participation", "icon": "groups", "path": "/sports-officer/student-participation" },
        { "label": "Achievements", "icon": "emoji_events", "path": "/sports-officer/achievements" },
        { "label": "Certificates", "icon": "workspace_premium", "path": "/sports-officer/certificates" },
        { "label": "Clubs Management", "icon": "category", "path": "/sports-officer/clubs-management" },
        { "label": "Announcements", "icon": "campaign", "path": "/sports-officer/announcements" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
