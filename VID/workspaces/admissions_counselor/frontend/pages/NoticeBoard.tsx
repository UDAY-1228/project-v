import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/admissions-counselor/notice-board"
    },

    {
        "label": "Prospects",
        "icon": "person_search",
        "path": "/admissions-counselor/prospects"
    },
    {
        "label": "Applications",
        "icon": "assignment",
        "path": "/admissions-counselor/applications"
    },
    {
        "label": "Admissions",
        "icon": "how_to_reg",
        "path": "/admissions-counselor/admissions"
    },
    {
        "label": "Configurations",
        "icon": "settings",
        "path": "/admissions-counselor/config"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
