import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Courses: React.FC = () => {
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

    const currentCourses = [
        { code: "CS101", name: "Intro to Programming", students: 45, credits: 4 },
        { code: "MATH202", name: "Advanced Calculus", students: 30, credits: 3 },
        { code: "PHY103", name: "Classical Mechanics", students: 28, credits: 4 }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex justify-between items-center">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight tracking-tight">Active Department Courses</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage the current term's curriculum delivery</p>
                    </div>
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-slate-200/40">
                    <div className="overflow-x-auto">
                        <table className="w-full text-left">
                            <thead>
                                <tr className="border-b-2 border-slate-50">
                                    <th className="pb-8 text-[10px] font-black text-slate-400 uppercase tracking-widest pl-4">Course Info</th>
                                    <th className="pb-8 text-[10px] font-black text-slate-400 uppercase tracking-widest text-center">Enrolled</th>
                                    <th className="pb-8 text-[10px] font-black text-slate-400 uppercase tracking-widest text-center">Unit Load</th>
                                    <th className="pb-8 text-[10px] font-black text-slate-400 uppercase tracking-widest text-right pr-4">Commands</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-50">
                                {currentCourses.map((course, idx) => (
                                    <tr key={idx} className="group hover:bg-slate-50/50 transition-colors">
                                        <td className="py-8 pl-4">
                                            <div className="flex items-center gap-5">
                                                <div className="w-12 h-12 bg-indigo-50 text-indigo-500 rounded-2xl flex items-center justify-center font-black text-xs">{course.code}</div>
                                                <p className="font-extrabold text-slate-800 tracking-tight">{course.name}</p>
                                            </div>
                                        </td>
                                        <td className="py-8 text-center text-sm font-black text-slate-500">{course.students}</td>
                                        <td className="py-8 text-center text-sm font-black text-slate-500">{course.credits} Cr.</td>
                                        <td className="py-8 text-right pr-4">
                                            <button className="text-[10px] font-black uppercase tracking-widest text-indigo-600 hover:text-indigo-800 bg-indigo-50 px-5 py-2 rounded-full transition-all">Syllabus Details</button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Courses;
