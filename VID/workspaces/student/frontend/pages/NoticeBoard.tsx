import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/student/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/student/dashboard" },
        { "label": "Attendance", "icon": "how_to_reg", "path": "/student/attendance" },
        { "label": "Chatbot", "icon": "smart_toy", "path": "/student/chatbot" },
        { "label": "Teacher Communications", "icon": "forum", "path": "/student/teacher-communications" },
        { "label": "Fees", "icon": "payments", "path": "/student/fees" },
        { "label": "Examinations", "icon": "grading", "path": "/student/examinations" },
        { "label": "Co Curricular Activities", "icon": "rowing", "path": "/student/co-curricular-activities" },
        { "label": "Learning Management", "icon": "laptop_chromebook", "path": "/student/learning-management" },
        { "label": "Course Tracking", "icon": "trending_up", "path": "/student/course-tracking" },
        { "label": "Profile", "icon": "person", "path": "/student/profile" },
        { "label": "Payment History", "icon": "history", "path": "/student/payment-history" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} canPost={false} />;
};

export default NoticeBoard;
