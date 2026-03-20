import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const MasterCourses: React.FC = () => {
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
                <div className="flex justify-between items-center">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Master Course Catalog</h1>
                        <p className="text-slate-500 font-medium tracking-tight">The immutable source of curriculum definitions</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300 items-center text-center">
                        <div className="w-20 h-20 bg-indigo-50 text-indigo-500 rounded-3xl flex items-center justify-center group-hover:bg-indigo-500 group-hover:text-white transition-all shadow-lg shadow-indigo-100/20">
                            <span className="material-icons text-3xl">psychology_alt</span>
                        </div>
                        <div>
                            <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Program Catalog</h3>
                            <button className="text-[9px] font-black uppercase tracking-widest text-indigo-600 bg-indigo-50 px-5 py-2 rounded-full transition-all">View Program Catalog</button>
                        </div>
                    </div>

                    <div className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300 items-center text-center">
                        <div className="w-20 h-20 bg-emerald-50 text-emerald-500 rounded-3xl flex items-center justify-center group-hover:bg-emerald-500 group-hover:text-white transition-all shadow-lg shadow-emerald-100/20">
                            <span className="material-icons text-3xl">menu_book</span>
                        </div>
                        <div>
                            <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Syllabus Master</h3>
                            <button className="text-[9px] font-black uppercase tracking-widest text-emerald-600 bg-emerald-50 px-5 py-2 rounded-full transition-all">Open Master Repository</button>
                        </div>
                    </div>

                    <div className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300 items-center text-center">
                        <div className="w-20 h-20 bg-pink-50 text-pink-500 rounded-3xl flex items-center justify-center group-hover:bg-pink-500 group-hover:text-white transition-all shadow-lg shadow-pink-100/20">
                            <span className="material-icons text-3xl">calculate</span>
                        </div>
                        <div>
                            <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Credit Scheme</h3>
                            <button className="text-[9px] font-black uppercase tracking-widest text-pink-600 bg-pink-50 px-5 py-2 rounded-full transition-all">Set Credit Policies</button>
                        </div>
                    </div>

                    <div className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300 items-center text-center">
                        <div className="w-20 h-20 bg-slate-50 text-slate-400 rounded-3xl flex items-center justify-center group-hover:bg-slate-800 group-hover:text-white transition-all shadow-lg shadow-slate-100/20">
                            <span className="material-icons text-3xl">tune</span>
                        </div>
                        <div>
                            <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Policy Settings</h3>
                            <button className="text-[9px] font-black uppercase tracking-widest text-slate-600 bg-slate-100 px-5 py-2 rounded-full transition-all">Global Setup</button>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default MasterCourses;
