import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const AcademicSetup: React.FC = () => {
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
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Academic Infrastructure Setup</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Configure the fundamental building blocks of academics</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-slate-50 text-slate-400 rounded-3xl flex items-center justify-center group-hover:bg-indigo-600 group-hover:text-white transition-all shadow-md group-hover:shadow-indigo-500/20">
                            <span className="material-icons text-3xl">corporate_fare</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight">Batch Management</h3>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-slate-50 text-slate-400 rounded-3xl flex items-center justify-center group-hover:bg-indigo-600 group-hover:text-white transition-all shadow-md group-hover:shadow-indigo-500/20">
                            <span className="material-icons text-3xl">meeting_room</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight">Sections & Classrooms</h3>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-slate-50 text-slate-400 rounded-3xl flex items-center justify-center group-hover:bg-indigo-600 group-hover:text-white transition-all shadow-md group-hover:shadow-indigo-500/20">
                            <span className="material-icons text-3xl">calculate</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight">GPA & Grading Rules</h3>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default AcademicSetup;
