import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/team-owner/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/team-owner/dashboard" },
        { "label": "Institutions", "icon": "business", "path": "/team-owner/institutions" },
        { "label": "Organization Settings", "icon": "settings_suggest", "path": "/team-owner/organization-settings" },
        { "label": "User Management", "icon": "manage_accounts", "path": "/team-owner/user-management" },
        { "label": "Apps", "icon": "apps", "path": "/team-owner/apps" },
        { "label": "Data Management", "icon": "storage", "path": "/team-owner/data-management" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
