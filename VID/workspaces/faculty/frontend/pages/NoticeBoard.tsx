import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/faculty/notice-board"
    },

    {
        "label": "Notice Board",
        "icon": "announcement",
        "path": "/faculty/notice-board"
    },
    {
        "label": "Activities",
        "icon": "event",
        "path": "/faculty/activities"
    },
    {
        "label": "Discussion",
        "icon": "forum",
        "path": "/faculty/discussion"
    },
    {
        "label": "Calendar",
        "icon": "calendar_month",
        "path": "/faculty/calendar"
    },
    {
        "label": "My Courses",
        "icon": "class",
        "path": "/faculty/courses"
    },
    {
        "label": "Timetable",
        "icon": "schedule",
        "path": "/faculty/timetable"
    },
    {
        "label": "LMS Classroom",
        "icon": "laptop",
        "path": "/faculty/lms"
    },
    {
        "label": "Assessments",
        "icon": "quiz",
        "path": "/faculty/assessments"
    },
    {
        "label": "Assignments",
        "icon": "assignment",
        "path": "/faculty/assignments"
    },
    {
        "label": "Attendance",
        "icon": "task_alt",
        "path": "/faculty/attendance"
    },
    {
        "label": "Students",
        "icon": "groups",
        "path": "/faculty/students"
    },
    {
        "label": "My Mentees",
        "icon": "psychology",
        "path": "/faculty/mentees"
    },
    {
        "label": "Research",
        "icon": "science",
        "path": "/faculty/research"
    },
    {
        "label": "Profile",
        "icon": "person",
        "path": "/faculty/profile"
    },
    {
        "label": "Reports",
        "icon": "analytics",
        "path": "/faculty/reports"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
