import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/academic-coordinator/notice-board"
    },
    {
        "label": "Activities",
        "icon": "event",
        "path": "/academic-coordinator/activities"
    },
    {
        "label": "Principal Dashboard",
        "icon": "dashboard_customize",
        "path": "/academic-coordinator/principal-dashboard"
    },
    {
        "label": "Academics",
        "icon": "school",
        "path": "/academic-coordinator/academics"
    },
    {
        "label": "Academic Setup",
        "icon": "settings_suggest",
        "path": "/academic-coordinator/setup"
    },
    {
        "label": "Courses",
        "icon": "menu_book",
        "path": "/academic-coordinator/courses"
    },
    {
        "label": "Master Courses",
        "icon": "library_books",
        "path": "/academic-coordinator/master-courses"
    },
    {
        "label": "Assessment",
        "icon": "assignment_turned_in",
        "path": "/academic-coordinator/assessment"
    },
    {
        "label": "Data Management",
        "icon": "storage",
        "path": "/academic-coordinator/data-management"
    },
    {
        "label": "Configurations",
        "icon": "settings",
        "path": "/academic-coordinator/config"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
