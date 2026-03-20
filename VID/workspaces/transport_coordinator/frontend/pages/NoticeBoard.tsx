import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [

    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/transport-coordinator/notice-board"
    },
    {
        "label": "Transport Analytics",
        "icon": "bar_chart",
        "path": "/transport-coordinator/analytics"
    },
    {
        "label": "Transport Registrations",
        "icon": "app_registration",
        "path": "/transport-coordinator/registrations"
    },
    {
        "label": "Buses",
        "icon": "directions_bus",
        "path": "/transport-coordinator/buses"
    },
    {
        "label": "Boarding Points",
        "icon": "place",
        "path": "/transport-coordinator/boarding"
    },
    {
        "label": "Routes",
        "icon": "map",
        "path": "/transport-coordinator/routes"
    },
    {
        "label": "Route Bus Assignment",
        "icon": "assignment",
        "path": "/transport-coordinator/assignment"
    },
    {
        "label": "Configuration",
        "icon": "settings",
        "path": "/transport-coordinator/config"
    },
    {
        "label": "Transport Route",
        "icon": "alt_route",
        "path": "/transport-coordinator/transport-route"
    }
    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
