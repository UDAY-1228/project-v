import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/hostel-admin/notice-board"
    },

    {
        "label": "Dashboard",
        "icon": "dashboard",
        "path": "/hostel-admin/dashboard"
    },
    {
        "label": "Hostelers",
        "icon": "hotel",
        "path": "/hostel-admin/hostelers"
    },
    {
        "label": "Attendance",
        "icon": "check_circle",
        "path": "/hostel-admin/attendance"
    },
    {
        "label": "Gate Pass Requests",
        "icon": "key",
        "path": "/hostel-admin/gatepass"
    },
    {
        "label": "Reports",
        "icon": "analytics",
        "path": "/hostel-admin/reports"
    },
    {
        "label": "Configuration",
        "icon": "settings",
        "path": "/hostel-admin/config"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
