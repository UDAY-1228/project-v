import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/common/notice-board"
    },

    {
        "label": "Home",
        "icon": "home",
        "path": "/common/home"
    },
    {
        "label": "Student Central",
        "icon": "school",
        "path": "/common/student-central"
    },
    {
        "label": "My Requests",
        "icon": "rate_review",
        "path": "/common/requests"
    },
    {
        "label": "Payments",
        "icon": "payments",
        "path": "/common/payments"
    },
    {
        "label": "Exams",
        "icon": "assessment",
        "path": "/common/exams"
    },
    {
        "label": "HRMS",
        "icon": "badge",
        "path": "/common/hrms"
    },
    {
        "label": "Configurations",
        "icon": "settings",
        "path": "/common/config"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
