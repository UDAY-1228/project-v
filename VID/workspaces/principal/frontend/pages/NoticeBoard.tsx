import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/principal/notice-board"
    },
    {
        "label": "Activities",
        "icon": "event",
        "path": "/principal/activities"
    },
    {
        "label": "Principal Dashboard",
        "icon": "dashboard",
        "path": "/principal/dashboard"
    },
    {
        "label": "Academics",
        "icon": "school",
        "path": "/principal/academics"
    },
    {
        "label": "Data Management",
        "icon": "storage",
        "path": "/principal/data"
    },
    {
        "label": "Configurations",
        "icon": "settings",
        "path": "/principal/config"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
