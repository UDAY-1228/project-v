import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Academics: React.FC = () => {
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
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Academics Central</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Main hub for academic planning and curriculum management</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-indigo-50 text-indigo-500 rounded-3xl flex items-center justify-center group-hover:bg-indigo-500 group-hover:text-white transition-all shadow-lg shadow-indigo-100/20">
                            <span className="material-icons text-3xl">auto_stories</span>
                        </div>
                        <div>
                            <h3 className="text-xl font-black text-slate-800 tracking-tight mb-2">Curriculum Design</h3>
                            <p className="text-slate-400 font-medium text-xs leading-relaxed">Map institutional educational goals to actionable modules and syllabus benchmarks.</p>
                        </div>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-emerald-50 text-emerald-500 rounded-3xl flex items-center justify-center group-hover:bg-emerald-500 group-hover:text-white transition-all shadow-lg shadow-emerald-100/20">
                            <span className="material-icons text-3xl">history_edu</span>
                        </div>
                        <div>
                            <h3 className="text-xl font-black text-slate-800 tracking-tight mb-2">Lesson Planning</h3>
                            <p className="text-slate-400 font-medium text-xs leading-relaxed">Systematic tracking of faculty lesson plans, teaching materials, and delivery timelines.</p>
                        </div>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-amber-50 text-amber-500 rounded-3xl flex items-center justify-center group-hover:bg-amber-500 group-hover:text-white transition-all shadow-lg shadow-amber-100/20">
                            <span className="material-icons text-3xl">psychology</span>
                        </div>
                        <div>
                            <h3 className="text-xl font-black text-slate-800 tracking-tight mb-2">Self-Learning Paths</h3>
                            <p className="text-slate-400 font-medium text-xs leading-relaxed">Provisioning of additional resources and asynchronous learning materials for advanced students.</p>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Academics;
