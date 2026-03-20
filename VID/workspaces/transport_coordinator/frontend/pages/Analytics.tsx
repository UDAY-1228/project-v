import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Analytics: React.FC = () => {
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

    const stats = [
        { title: "Active Buses", value: "24", icon: "directions_bus", color: "blue" as const },
        { title: "Active Routes", value: "8", icon: "map", color: "green" as const },
        { title: "Registered Students", value: "1,240", icon: "people", color: "indigo" as const },
        { title: "Monthly Revenue", value: "$45k", icon: "payments", color: "yellow" as const }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Transport Analytics</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Real-time data and transport insights</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    {stats.map((stat, idx) => (
                        <Card key={idx} {...stat} />
                    ))}
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100 min-h-[400px]">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-10 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Attendance & Route Efficiency
                    </h3>
                    <div className="flex items-center justify-center py-20 bg-slate-50/50 rounded-3xl border border-dashed border-slate-200">
                        <div className="text-center">
                            <span className="material-icons text-6xl text-slate-200 mb-6 group-hover:scale-110 transition-transform">insights</span>
                            <p className="text-slate-400 font-bold uppercase tracking-widest text-xs">Charts & Graphs Placeholder</p>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Analytics;
