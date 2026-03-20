import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/admission-officer/notice-board"
    },

    {
        "label": "Prospects",
        "icon": "person_search",
        "path": "/admission-officer/prospects"
    },
    {
        "label": "Applications",
        "icon": "assignment",
        "path": "/admission-officer/applications"
    },
    {
        "label": "Admissions",
        "icon": "how_to_reg",
        "path": "/admission-officer/admissions"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
