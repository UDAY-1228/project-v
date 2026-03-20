import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
        { label: "Digital Notice Board", icon: "announcement", path: "/transport-coordinator/notice-board" },
        { label: "Transport Analytics", icon: "bar_chart", path: "/transport-coordinator/analytics" },
        { label: "Transport Registrations", icon: "app_registration", path: "/transport-coordinator/registrations" },
        { label: "Buses", icon: "directions_bus", path: "/transport-coordinator/buses" },
        { label: "Boarding Points", icon: "place", path: "/transport-coordinator/boarding" },
        { label: "Routes", icon: "map", path: "/transport-coordinator/routes" },
        { label: "Route Bus Assignment", icon: "assignment", path: "/transport-coordinator/assignment" },
        { label: "Configuration", icon: "settings", path: "/transport-coordinator/config" },
        { label: "Transport Route", icon: "alt_route", path: "/transport-coordinator/transport-route" }
    ];

    const notices = [
        { id: 1, title: "Morning Bus Schedule Shift", date: "2024-03-21", content: "All morning buses will start 15 minutes earlier due to road construction.", category: "General" },
        { id: 2, title: "New Bus B-402 Added", date: "2024-03-20", content: "A new bus has been added to the North route to accommodate more students.", category: "Updates" },
        { id: 3, title: "Driver Training Session", date: "2024-03-18", content: "Mandatory safety training for all drivers this Saturday at 10 AM.", category: "Staff" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-8">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Digital Notice Board</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage and broadcast transport announcements</p>
                    </div>
                    <button className="px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold shadow-xl shadow-indigo-200 hover:bg-indigo-700 transition-all flex items-center gap-2">
                        <span className="material-icons text-xl">add</span>
                        Create Notice
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {notices.map((notice) => (
                        <div key={notice.id} className="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-xl shadow-slate-100/50 hover:shadow-2xl transition-all group relative overflow-hidden">
                            <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-50/50 rounded-full -mr-16 -mt-16 group-hover:scale-150 transition-transform duration-500" />
                            <div className="relative">
                                <span className="px-3 py-1 bg-indigo-100 text-indigo-600 text-[10px] font-black uppercase tracking-widest rounded-full">{notice.category}</span>
                                <h3 className="text-xl font-bold text-slate-800 mt-4 mb-2">{notice.title}</h3>
                                <p className="text-sm text-slate-500 font-medium mb-6 leading-relaxed">{notice.content}</p>
                                <div className="flex items-center justify-between">
                                    <span className="text-slate-400 text-xs font-bold flex items-center gap-2">
                                        <span className="material-icons text-sm opacity-50">calendar_today</span>
                                        {notice.date}
                                    </span>
                                    <button className="text-indigo-600 font-bold text-sm hover:underline">Edit</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default NoticeBoard;
