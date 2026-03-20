import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/common/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/common/dashboard" },
        { "label": "Home", "icon": "home", "path": "/common/home" },
        { "label": "Student Central", "icon": "hub", "path": "/common/student-central" },
        { "label": "My Requests", "icon": "receipt_long", "path": "/common/my-requests" },
        { "label": "Payments", "icon": "payments", "path": "/common/payments" },
        { "label": "Examination", "icon": "grading", "path": "/common/examination" },
        { "label": "Hrms", "icon": "badge", "path": "/common/hrms" },
        { "label": "Configuration", "icon": "settings", "path": "/common/configuration" },
        { "label": "User Management System", "icon": "manage_accounts", "path": "/common/user-management-system" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
