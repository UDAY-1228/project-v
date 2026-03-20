import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/student/notice-board"
    },

    {
        "label": "Notice Board",
        "icon": "announcement",
        "path": "/student/notice-board"
    },
    {
        "label": "My Attendance",
        "icon": "check_circle",
        "path": "/student/attendance"
    },
    {
        "label": "Events",
        "icon": "event",
        "path": "/student/events"
    },
    {
        "label": "LMS",
        "icon": "auto_stories",
        "path": "/student/lms"
    },
    {
        "label": "Exams",
        "icon": "assignment",
        "path": "/student/exams"
    },
    {
        "label": "Assessments",
        "icon": "quiz",
        "path": "/student/assessments"
    },
    {
        "label": "Question Bank",
        "icon": "menu_book",
        "path": "/student/questions"
    },
    {
        "label": "Fee Payments",
        "icon": "payments",
        "path": "/student/payments"
    },
    {
        "label": "My Profile",
        "icon": "person",
        "path": "/student/profile"
    },
    {
        "label": "Calendar",
        "icon": "calendar_month",
        "path": "/student/calendar"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
