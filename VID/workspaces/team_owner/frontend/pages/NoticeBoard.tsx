import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Institutions",
        "icon": "business",
        "path": "/team-owner/institutions"
    },
    {
        "label": "Organization Settings",
        "icon": "admin_panel_settings",
        "path": "/team-owner/settings"
    },
    {
        "label": "User Management",
        "icon": "manage_accounts",
        "path": "/team-owner/users"
    },
    {
        "label": "Apps Data Management",
        "icon": "apps",
        "path": "/team-owner/apps"
    },
    {
        "label": "Course Coordinator",
        "icon": "coordinator",
        "path": "/team-owner/coordinator"
    },
    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/team-owner/notice-board"
    },
    {
        "label": "All Courses",
        "icon": "menu_book",
        "path": "/team-owner/courses"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
