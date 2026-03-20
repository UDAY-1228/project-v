import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Dashboard: React.FC = () => {
    const sidebarItems = [
    {
        "label": "Institutions",
        "icon": "business",
        "path": "/team-owner/institutions"
    },
    {
        "label": "Organization Settings",
        "icon": "admin_panel_settings",
        "path": "/team-owner/settings"
    },
    {
        "label": "User Management",
        "icon": "manage_accounts",
        "path": "/team-owner/users"
    },
    {
        "label": "Apps Data Management",
        "icon": "apps",
        "path": "/team-owner/apps"
    },
    {
        "label": "Course Coordinator",
        "icon": "coordinator",
        "path": "/team-owner/coordinator"
    },
    {
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/team-owner/notice-board"
    },
    {
        "label": "All Courses",
        "icon": "menu_book",
        "path": "/team-owner/courses"
    }
];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize">team owner Dashboard</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Welcome to the VID Portal</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Notifications" value="12" icon="announcement" color="blue" />
                    <Card title="Completed Tasks" value="85%" icon="task_alt" color="green" />
                    <Card title="Pending Review" value="5" icon="pending" color="yellow" />
                    <Card title="System Health" value="Stable" icon="health_and_safety" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Overview & Features
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {sidebarItems.map((item, idx) => (
                            <a 
                                key={idx} 
                                href={item.path}
                                className="group flex items-center gap-6 p-8 bg-slate-50/50 rounded-3xl border border-slate-100 hover:border-indigo-400 hover:bg-white hover:shadow-xl transition-all duration-300"
                            >
                                <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-indigo-500 group-hover:bg-indigo-500 group-hover:text-white transition-all">
                                    <span className="material-icons text-2xl group-hover:scale-110 transition-transform">{item.icon}</span>
                                </div>
                                <div>
                                    <p className="font-extrabold text-slate-800 tracking-tight group-hover:text-indigo-600 transition-colors">{item.label}</p>
                                    <p className="text-[11px] font-bold text-slate-400 uppercase tracking-widest mt-1">Access Module</p>
                                </div>
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Dashboard;
