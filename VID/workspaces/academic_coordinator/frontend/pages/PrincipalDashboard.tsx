import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const PrincipalDashboard: React.FC = () => {
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

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize tracking-tight">Principal Overview Dashboard</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Key metrics for school administration and academic tracking</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Total Students" value="1,240" icon="groups" color="indigo" />
                    <Card title="Avg Attendance" value="94.2%" icon="check_circle" color="green" />
                    <Card title="Avg GP Grade" value="3.41" icon="grade" color="yellow" />
                    <Card title="Fee Collection" value="88%" icon="payments" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Key Academic Performance Indicators
                    </h3>
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
                        <div className="aspect-[16/9] bg-slate-50 rounded-[2.5rem] border-2 border-dashed border-slate-200 flex items-center justify-center text-slate-400 font-bold uppercase tracking-widest text-xs">Academic Progress Chart</div>
                        <div className="aspect-[16/9] bg-slate-50 rounded-[2.5rem] border-2 border-dashed border-slate-200 flex items-center justify-center text-slate-400 font-bold uppercase tracking-widest text-xs">Staff Performance Distribution</div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default PrincipalDashboard;
