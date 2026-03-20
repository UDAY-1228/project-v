import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/admission-officer/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/admission-officer/dashboard" },
        { "label": "Prospects", "icon": "person_search", "path": "/admission-officer/prospects" },
        { "label": "Applications", "icon": "assignment", "path": "/admission-officer/applications" },
        { "label": "Admissions", "icon": "how_to_reg", "path": "/admission-officer/admissions" },
        { "label": "Configuration", "icon": "settings", "path": "/admission-officer/configuration" }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
