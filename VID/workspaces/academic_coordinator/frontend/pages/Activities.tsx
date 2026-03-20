import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Activities: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/academic-coordinator/notice-board" },
        { "label": "Activities", "icon": "event", "path": "/academic-coordinator/activities" },
        { "label": "Principal Dashboard", "icon": "dashboard_customize", "path": "/academic-coordinator/principal-dashboard" },
        { "label": "Academics", "icon": "school", "path": "/academic-coordinator/academics" },
        { "label": "Academic Setup", "icon": "settings_suggest", "path": "/academic-coordinator/setup" },
        { "label": "Courses", "icon": "menu_book", "path": "/academic-coordinator/courses" },
        { "label": "Master Courses", "icon": "library_books", "path": "/academic-coordinator/master-courses" },
        { "label": "Assessment", "icon": "assignment_turned_in", "path": "/academic-coordinator/assessment" },
        { "label": "Data Management", "icon": "storage", "path": "/academic-coordinator/data-management" },
        { "label": "Configurations", "icon": "settings", "path": "/academic-coordinator/config" }
    ];

    const activities = [
        { id: 1, name: "Science Exhibition Planning", date: "2024-04-10", status: "In Progress", type: "Event" },
        { id: 2, name: "Parent Teacher Meeting", date: "2024-03-25", status: "Scheduled", type: "Meeting" },
        { id: 3, name: "Annual Sports Meet", date: "2024-05-15", status: "Draft", type: "Sports" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-8">
                <div>
                    <h1 className="text-4xl font-black text-slate-800 tracking-tight">Academic Activities</h1>
                    <p className="text-slate-500 font-medium tracking-tight">Manage and track institutional events and milestones</p>
                </div>

                <div className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10">
                    <div className="flex justify-between items-center mb-8">
                        <h3 className="text-xl font-black text-slate-800 tracking-tight">Upcoming Activities</h3>
                        <button className="bg-indigo-600 text-white px-6 py-3 rounded-2xl text-xs font-black uppercase tracking-widest hover:bg-indigo-700 transition-all">Create New Activity</button>
                    </div>
                    <div className="space-y-4">
                        {activities.map(act => (
                            <div key={act.id} className="flex items-center justify-between p-6 bg-slate-50 rounded-3xl border border-slate-100 hover:border-indigo-400 transition-all cursor-pointer">
                                <div className="flex items-center gap-6">
                                    <div className="w-12 h-12 bg-white rounded-2xl flex items-center justify-center text-indigo-500 shadow-sm">
                                        <span className="material-icons">{act.type === 'Event' ? 'celebration' : act.type === 'Meeting' ? 'groups' : 'sports_soccer'}</span>
                                    </div>
                                    <div>
                                        <p className="font-bold text-slate-800">{act.name}</p>
                                        <p className="text-xs text-slate-400 font-bold uppercase tracking-widest">{act.date}</p>
                                    </div>
                                </div>
                                <span className={`px-4 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest ${act.status === 'Scheduled' ? 'bg-emerald-50 text-emerald-600' : act.status === 'In Progress' ? 'bg-blue-50 text-blue-600' : 'bg-slate-100 text-slate-500'}`}>{act.status}</span>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Activities;
