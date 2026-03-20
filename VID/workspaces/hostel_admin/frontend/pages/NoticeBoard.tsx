import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/hostel-admin/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/hostel-admin/dashboard" },
        { "label": "Hostels", "icon": "apartment", "path": "/hostel-admin/hostels" },
        { "label": "Attendance", "icon": "how_to_reg", "path": "/hostel-admin/attendance" },
        { "label": "Gate Pass", "icon": "directions_run", "path": "/hostel-admin/gate-pass" },
        { "label": "Requests", "icon": "question_answer", "path": "/hostel-admin/requests" },
        { "label": "Reports", "icon": "analytics", "path": "/hostel-admin/reports" },
        { "label": "Configuration", "icon": "settings", "path": "/hostel-admin/configuration" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
