import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/employee/notice-board"
    },

    {
        "label": "Home",
        "icon": "home",
        "path": "/employee/home"
    },
    {
        "label": "Leaves",
        "icon": "holiday_village",
        "path": "/employee/leaves"
    },
    {
        "label": "Attendance",
        "icon": "check_circle",
        "path": "/employee/attendance"
    },
    {
        "label": "Salary",
        "icon": "account_balance_wallet",
        "path": "/employee/salary"
    },
    {
        "label": "Expenses",
        "icon": "receipt_long",
        "path": "/employee/expenses"
    },
    {
        "label": "Shift Requests",
        "icon": "schedule",
        "path": "/employee/shifts"
    },
    {
        "label": "Compensatory Leave",
        "icon": "event_available",
        "path": "/employee/comp-leave"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
