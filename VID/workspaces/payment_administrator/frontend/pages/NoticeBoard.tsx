import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/payment-administrator/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/payment-administrator/dashboard" },
        { "label": "Academic Fees", "icon": "school", "path": "/payment-administrator/academic-fees" },
        { "label": "Student Permissions", "icon": "verified_user", "path": "/payment-administrator/student-permissions" },
        { "label": "Exam Fee Restrictions", "icon": "gavel", "path": "/payment-administrator/exam-fee-restrictions" },
        { "label": "Examination Fees", "icon": "grading", "path": "/payment-administrator/examination-fees" },
        { "label": "Open Payments", "icon": "account_balance", "path": "/payment-administrator/open-payments" },
        { "label": "Configuration", "icon": "settings", "path": "/payment-administrator/configuration" },
        { "label": "Reports", "icon": "analytics", "path": "/payment-administrator/reports" },
        { "label": "Concessions", "icon": "discount", "path": "/payment-administrator/concessions" },
        { "label": "Online Transactions", "icon": "payment", "path": "/payment-administrator/online-transactions" },
        { "label": "Challans", "icon": "receipt", "path": "/payment-administrator/challans" },
        { "label": "Statements", "icon": "description", "path": "/payment-administrator/statements" },
        { "label": "Scholarships", "icon": "military_tech", "path": "/payment-administrator/scholarships" },
        { "label": "Credit Memos", "icon": "credit_card", "path": "/payment-administrator/credit-memos" },
        { "label": "Student Fee Card", "icon": "account_box", "path": "/payment-administrator/student-fee-card" },
        { "label": "Transaction Card", "icon": "credit_score", "path": "/payment-administrator/transaction-card" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
