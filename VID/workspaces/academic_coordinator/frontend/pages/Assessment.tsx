import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Assessment: React.FC = () => {
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
                <div className="flex justify-between items-center text-slate-800">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight tracking-tight uppercase tracking-tight">Assessment Engine</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Configure and track examination schedules and grading</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Upcoming Exams" value="8" icon="event" color="blue" />
                    <Card title="Pending Grading" value="342" icon="grading" color="yellow" />
                    <Card title="Completed Tests" value="1.2k" icon="task_alt" color="green" />
                    <Card title="Re-eval Requests" value="12" icon="error_outline" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8">Assessment Components</h3>
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {['Quiz Management', 'Final Exams', 'Continuous Assessment'].map((item, idx) => (
                            <div key={idx} className="p-8 bg-slate-50 rounded-3xl border border-slate-100 hover:border-indigo-400 transition-all cursor-pointer group">
                                <div className="flex justify-between items-center">
                                    <span className="font-extrabold text-slate-800 tracking-tight group-hover:text-indigo-600 transition-colors uppercase text-sm">{item}</span>
                                    <span className="material-icons text-indigo-500 opacity-0 group-hover:opacity-100 transition-all">east</span>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Assessment;
