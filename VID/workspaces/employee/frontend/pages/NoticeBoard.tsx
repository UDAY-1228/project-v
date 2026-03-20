import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/employee/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/employee/dashboard" },
        { "label": "Home", "icon": "home", "path": "/employee/home" },
        { "label": "Leaves", "icon": "time_to_leave", "path": "/employee/leaves" },
        { "label": "Attendance", "icon": "how_to_reg", "path": "/employee/attendance" },
        { "label": "Salary", "icon": "account_balance_wallet", "path": "/employee/salary" },
        { "label": "Expenses", "icon": "receipt", "path": "/employee/expenses" },
        { "label": "Shift Requests", "icon": "schedule", "path": "/employee/shift-requests" },
        { "label": "Compensatory Leave", "icon": "event_available", "path": "/employee/compensatory-leave" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
