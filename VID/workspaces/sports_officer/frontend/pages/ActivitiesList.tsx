import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const ActivitiesList: React.FC = () => {
        const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/sports-officer/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/sports-officer/dashboard" },
        { "label": "Sports Events", "icon": "emoji_events", "path": "/sports-officer/sports-events" },
        { "label": "Team Management", "icon": "groups", "path": "/sports-officer/team-management" },
        { "label": "Player Registrations", "icon": "how_to_reg", "path": "/sports-officer/player-registrations" },
        { "label": "Practice Schedules", "icon": "schedule", "path": "/sports-officer/practice-schedules" },
        { "label": "Tournament Management", "icon": "emoji_events", "path": "/sports-officer/tournament-management" },
        { "label": "Performance Tracking", "icon": "trending_up", "path": "/sports-officer/performance-tracking" },
        { "label": "Reports", "icon": "analytics", "path": "/sports-officer/reports" },
        { "label": "Activities List", "icon": "list_alt", "path": "/sports-officer/activities-list" },
        { "label": "Event Calendar", "icon": "event", "path": "/sports-officer/event-calendar" },
        { "label": "Student Participation", "icon": "groups", "path": "/sports-officer/student-participation" },
        { "label": "Achievements", "icon": "emoji_events", "path": "/sports-officer/achievements" },
        { "label": "Certificates", "icon": "workspace_premium", "path": "/sports-officer/certificates" },
        { "label": "Clubs Management", "icon": "category", "path": "/sports-officer/clubs-management" },
        { "label": "Announcements", "icon": "campaign", "path": "/sports-officer/announcements" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize">Activities List</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage and oversee operational activities</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Total Records" value="1,240" icon="groups" color="indigo" />
                    <Card title="Active Status" value="94.2%" icon="check_circle" color="green" />
                    <Card title="Pending Review" value="34" icon="pending" color="yellow" />
                    <Card title="System Alerts" value="2" icon="error_outline" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Activities List Data Interface
                    </h3>
                    <div className="flex items-center justify-center p-20 bg-slate-50 border-2 border-dashed border-slate-200 rounded-[2.5rem]">
                        <p className="text-slate-400 font-bold uppercase tracking-widest text-xs">Module Implementation Area</p>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default ActivitiesList;
