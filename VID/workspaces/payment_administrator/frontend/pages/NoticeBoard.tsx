import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/payment-administrator/notice-board"
    },

    {
        "label": "Dashboard",
        "icon": "dashboard",
        "path": "/payment-administrator/dashboard"
    },
    {
        "label": "Student Permissions",
        "icon": "security",
        "path": "/payment-administrator/permissions"
    },
    {
        "label": "Academic Fees",
        "icon": "school",
        "path": "/payment-administrator/academic-fees"
    },
    {
        "label": "Exam Fees",
        "icon": "assessment",
        "path": "/payment-administrator/exam-fees"
    },
    {
        "label": "Restrictions",
        "icon": "block",
        "path": "/payment-administrator/restrictions"
    },
    {
        "label": "Open Payments",
        "icon": "credit_card",
        "path": "/payment-administrator/open-payments"
    },
    {
        "label": "Reports",
        "icon": "analytics",
        "path": "/payment-administrator/reports"
    },
    {
        "label": "Configuration",
        "icon": "settings",
        "path": "/payment-administrator/config"
    },
    {
        "label": "Concessions",
        "icon": "money_off",
        "path": "/payment-administrator/concessions"
    },
    {
        "label": "Online Transactions",
        "icon": "online_prediction",
        "path": "/payment-administrator/online"
    },
    {
        "label": "Challans",
        "icon": "receipt",
        "path": "/payment-administrator/challans"
    },
    {
        "label": "Statements",
        "icon": "account_balance",
        "path": "/payment-administrator/statements"
    },
    {
        "label": "Scholarships",
        "icon": "card_membership",
        "path": "/payment-administrator/scholarships"
    },
    {
        "label": "Credit Memos",
        "icon": "note_add",
        "path": "/payment-administrator/credits"
    },
    {
        "label": "Fee Card",
        "icon": "credit_card",
        "path": "/payment-administrator/feecard"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
