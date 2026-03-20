import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const DataManagement: React.FC = () => {
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
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Academic Data Management</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Bulk operations and data integrity checks</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-blue-50 text-blue-500 rounded-3xl flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition-all shadow-md">
                            <span className="material-icons text-3xl">upload_file</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Bulk Import Students</h3>
                        <p className="text-slate-400 font-medium text-xs leading-relaxed">Import student records via CSV/XLSX following defined templates.</p>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-emerald-50 text-emerald-500 rounded-3xl flex items-center justify-center group-hover:bg-emerald-600 group-hover:text-white transition-all shadow-md">
                            <span className="material-icons text-3xl">cloud_download</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Export Performance Hub</h3>
                        <p className="text-slate-400 font-medium text-xs leading-relaxed">System-wide export for external monitoring and accreditation.</p>
                    </div>

                    <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 flex flex-col gap-6 group hover:translate-y-[-0.5rem] transition-all duration-300">
                        <div className="w-16 h-16 bg-rose-50 text-rose-500 rounded-3xl flex items-center justify-center group-hover:bg-rose-600 group-hover:text-white transition-all shadow-md">
                            <span className="material-icons text-3xl">cleaning_services</span>
                        </div>
                        <h3 className="text-lg font-black text-slate-800 tracking-tight mb-2">Data Integrity Sanitizer</h3>
                        <p className="text-slate-400 font-medium text-xs leading-relaxed">Scan for inconsistencies in student records, grading schemas, or academic setup.</p>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default DataManagement;
