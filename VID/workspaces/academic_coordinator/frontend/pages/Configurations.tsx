import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Configurations: React.FC = () => {
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
                    <h1 className="text-4xl font-black text-slate-800 tracking-tight">Academic Configurations</h1>
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-10">
                        <div className="space-y-4">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest px-2">Academic Year Setup</label>
                            <select className="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl py-4 px-6 focus:border-indigo-500 focus:bg-white transition-all outline-none font-bold text-slate-700">
                                <option>2023-2024 (Current)</option>
                                <option>2024-2025 (Planning)</option>
                            </select>
                        </div>
                        <div className="space-y-4">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest px-2">Semester Schedule</label>
                            <select className="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl py-4 px-6 focus:border-indigo-500 focus:bg-white transition-all outline-none font-bold text-slate-700">
                                <option>Odd Semester</option>
                                <option>Even Semester</option>
                            </select>
                        </div>
                        <div className="space-y-4">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest px-2">Assessment Threshold (%)</label>
                            <input type="number" defaultValue={40} className="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl py-4 px-6 focus:border-indigo-500 focus:bg-white transition-all outline-none font-bold text-slate-700" />
                        </div>
                        <div className="space-y-4">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest px-2">Auto-Promotion Status</label>
                            <div className="flex items-center gap-4 py-2">
                                <button className="w-14 h-8 bg-indigo-600 rounded-full relative shadow-inner">
                                    <div className="absolute right-1 top-1 w-6 h-6 bg-white rounded-full transition-all"></div>
                                </button>
                                <span className="font-bold text-slate-500 text-sm">Enabled for this term</span>
                            </div>
                        </div>
                    </div>
                    <div className="mt-12 pt-10 border-t border-slate-50">
                        <button className="bg-slate-900 text-white px-10 py-4 rounded-2xl text-xs font-black uppercase tracking-widest hover:bg-slate-800 transition-all shadow-xl shadow-slate-200">Save Configuration</button>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Configurations;
